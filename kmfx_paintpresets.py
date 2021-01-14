import fx, sys, json, glob, os
from fx import *

fx.prefs.add("KMFX.Paint Presets Path","")

class GenericJSONEncoder(json.JSONEncoder):
	def default(self, obj):
		try:
			return super().default(obj)
		except TypeError:
			pass
		cls = type(obj)

		result = {
			'__custom__': True,
			'__name__': cls.__name__}

		if cls == Point3D:
			result["data"] = {"x":obj.x,"y":obj.y,"z":obj.z}
		elif cls == Rect:
			result["data"] = {"size":obj.size}

		else:
			result["data"] = obj.__dict__ if not hasattr(cls, '__json_encode__') else obj.__json_encode__
	
		return result


class GenericJSONDecoder(json.JSONDecoder):
	def simpledecode(self,t):
			if t['__name__'] == "Point3D":
				return Point3D(t["data"]["x"],t["data"]["y"],t["data"]["z"])
			elif t['__name__'] == "Rect":
				temp = Rect(0,0,0,0)
				temp.setSize(t["data"]["size"][0],t["data"]["size"][1])	
				return temp	
			else:
				return t


	def decode(self, str):
		result = super().decode(str)

		mresult = {}
		
		for key in result.keys():

			if isinstance(result[key],list):
				#print(result[key],"\n")
				mresult[key] = []
				for n in range(0,len(result[key])):
					mresult[key].append(self.simpledecode(result[key][n]))

			else:
				if not isinstance(result[key], dict) or not result[key].get('__custom__', False):
				#print("regular",result)
					mresult[key] = result[key]
				else:
					#print(result[key],type(result[key]),"\n")
					if isinstance(result[key],list):
						#print(result[key],"\n")
						for n in range(0,len(result[key])):
							mresult[key][n] = simpledecode(result[key][n])
								
					else:
	
						if result[key]['__name__'] == "Point3D":
	
					#print("x",result[key]["data"][0])
							mresult[key] = Point3D(result[key]["data"]["x"],result[key]["data"]["y"],result[key]["data"]["z"])
						elif result[key]['__name__'] == "Rect":
							mresult[key] = Rect(0,0,0,0)
							# print(result[key]["data"]["size"])
							mresult[key].setSize(result[key]["data"]["size"][0],result[key]["data"]["size"][1])
						#instance.__dict__.update(result['data'])
	

		return mresult

		



class KMFXpaintPresets(Action):
	"""this will save/load the actual state of the paint node to/from disk"""
	def __init__(self,):
		Action.__init__(self, "KMFX|Paint Presets")

	def available(self):
			pass # verification on execution


	def execute(self,**kwargs):
		# fx.beginUndo("KMFX Paint Presets") # undo is not working on this

		paint_presets_path = fx.prefs["KMFX.Paint Presets Path"] if fx.prefs["KMFX.Paint Presets Path"]!= "" else os.environ["SFX_SCRIPT_PATH"] + "/KMscripts/paint_presets/"
		mode = kwargs["mode"] if "mode" in kwargs.keys() else "save"

		node = activeNode()
		
		if node.type == "PaintNode":
			'''
			the actual brush used it saved on the <item type="string" id="brush"> on the preset.
			looks like the settings for the rest of the preset are not necessary
			'''
			fx.activeProject().save() ##small hack to force the state to update

			if mode == "save":

				fname = { "id" : "fname", "label" : "Filename", "value" : "Default"}
				result = getInput(fields=[fname])
				current = fx.paint.preset
				override = False

				if result != None:
					dpath = paint_presets_path+"/"+result["fname"]+"/"
					directory = os.path.dirname(dpath)

					if os.path.exists(directory):
						ov=askQuestion("Preset already exists, override?")
						if ov == False:
							return # do not use this with UNDO
					try:
						if not os.path.exists(directory):
							os.makedirs(directory)
					except:
						print("Error creating preset directory, check folder write permissions?\n %s" % directory)			
					for i in range(0,10):
						fpath = paint_presets_path+"/"+result["fname"]+"/"+result["fname"]+"_"+str(i)+'.json'
						try:
							fx.paint.preset= i
							if len(node.state["preset"+str(i)]) > 0:
								dic = node.state["preset"+str(i)]
								ppreset = json.dumps(dic,cls=GenericJSONEncoder)
								with open(fpath, 'w') as file:
									file.write(ppreset)

							print("Saved preset %s @ %s" % (i,fpath))

						except:
							print("Preset %s skipped"% i)
							if os.path.exists(fpath):
								os.remove(fpath)
								print("Old Preset %s removed"% i)
							# e = sys.exc_info()
							# print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
				try:
					fx.paint.preset = current ## go back to original active preset
				except:
					pass


			elif mode == "load":
				jsonFiles = glob.glob(paint_presets_path+"/**/*.json",recursive=True)
				filelist = {}
				namecollection = []
				presetsfound = False
				if len(jsonFiles) > 0:
					for f in jsonFiles:
						name = os.path.basename(f)
						name = str(name).rsplit("_",1)[0]
						namecollection.append(name)
					namecollection= list(set(namecollection))
					presetsfound = True
				else:
					resulterror = getInput(title="Error", msg="No presets found")
					
				if presetsfound:
					lista = { "id" : "list", "label" : "List", "value" : namecollection[0], "items" : namecollection }
					result = getInput(fields=[lista])
					loadedpresets = []
					if result != None:
						for i in range(0,10):
							try:
								with open(paint_presets_path+"/"+result["list"]+"/"+result["list"]+"_"+str(i)+'.json') as complex_data:
									data = complex_data.read()
									b = json.loads(data, cls=GenericJSONDecoder)
									fx.paint.preset = i
									for ii in b.keys():
										fx.paint.setState(ii,b[ii])
									fx.paint.savePreset(i)
									loadedpresets.append(i)


							except:
								pass
						fx.paint.preset = min(loadedpresets) ## loads the first available preset
								# e = sys.exc_info()
								# print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)

		# fx.endUndo()  # undo is not working on this

addAction(KMFXpaintPresets())

