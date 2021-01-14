import fx
from fx import *
from tools.objectIterator import getObjects

class KMFXkeyframeVisibility(Action):
	"""Creates keyframes without clicking on the visibility icon"""

	def __init__(self):
		Action.__init__(self, "KMFX|Keyframe Visibility")

	def available(self):
		shapes = getObjects(selection(), types=[Shape])
		assert len(shapes) > 0, "There must be one or more selected shapes"

	def execute(self,**kwargs):
		shapes = getObjects(selection(), types=[Shape])
		optype= kwargs["mode"] if "mode" in kwargs.keys() else "default"

	
		beginUndo("Keyframe Visibility ON/OFF") 
		node = activeNode()
		session = node.session
		startFrame = session.startFrame

		actualframe = player.frame
		wasConstant = False
		for shape in shapes:			
			opacity = shape.property("opacity")
			if opacity.constant:
				opacity.constant = False		
				wasConstant = True
				
			if optype == "default":	
				if opacity.getValue(actualframe) > 0:
					opacity.setValue(0, actualframe)
				else:
					opacity.setValue(100, actualframe)
				if wasConstant and actualframe != 0:
					editor = PropertyEditor(opacity)				
					editor.deleteKey(0)
					editor.execute()
						
			if optype == "singleframe":
				if actualframe not in (0,session.duration):
					if opacity.getValue(actualframe) > 0:
						opacity.setValue(0, actualframe-1)
						opacity.setValue(100, actualframe)
						opacity.setValue(0, actualframe+1)
						if actualframe != 1 and wasConstant:
							editor = PropertyEditor(opacity)				
							editor.deleteKey(0)
							editor.execute()
				elif actualframe == 0:
					if opacity.getValue(actualframe) > 0:
						opacity.setValue(100, actualframe)
						opacity.setValue(0, actualframe+1)
				elif actualframe == session.duration:
					if opacity.getValue(actualframe) > 0:
						opacity.setValue(0, actualframe-1)
						opacity.setValue(100, actualframe)
						editor = PropertyEditor(opacity)				
						editor.deleteKey(0)
						editor.execute()


		endUndo()
addAction(KMFXkeyframeVisibility())


