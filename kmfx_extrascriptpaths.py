import fx
from fx import *
import os
import os.path
import sys

'''enables autoload of scripts from additional
 disk paths on silhouette preferences '''


fx.prefs.add("KMFX.ExtraScriptPath1", "")
fx.prefs.add("KMFX.ExtraScriptPath2", "")

# you can add more paths using the same logic, just increase the numbers
# fx.prefs.add("KMFX.ExtraScriptPath3","")
# fx.prefs.add("KMFX.ExtraScriptPath4","")


skip_files = ["__init__", "__pycache__", "CVS", "tags", "user_keybinds"]


def getScripts(path, package=None):
    scripts = []
    possible = []
    dir = os.listdir(path)

    for file in dir:
        f = os.path.splitext(file)
        name = f[0]
        ext = f[1]

        if name == "":
            continue

        if name in skip_files:
            continue

        if os.path.isdir(os.path.join(path, file)):
            if name[0] != '.':
                scripts.append(file)
            continue

        if ext == ".py":
            scripts.append(name)
        elif ext == ".pyc" or ext == ".pyo":
            possible.append(name)

    # merge the lists
    for s in possible:
        if s not in scripts:
            scripts.append(s)
    print("\nLoading remote/user scripts folder (", path, "):")
    return scripts


for p in fx.prefs.keys():
    if "KMFX.ExtraScript" in p:
        this_path = fx.prefs[p]
        if this_path != "":

            try:

                sys.path.append(fx.prefs[p])
                print("trying to import extra script path: %s" % this_path)
                scripts = getScripts(this_path)

                # import the scripts
                for s in scripts:
                    if len(s) > 2:
                        if (s[0] == '(') and (s[int(len(s)-1)] == ')'):
                            continue

                    str = "import " + s
                    try:
                        exec(str)
                        print(s,)
                    except Exception:
                        import traceback
                        sys.stderr.write("Could not import %s module:" % s)
                        info = sys.exc_info()
                        type = info[0]
                        param = info[1]
                        tb = info[2]
                        traceback.print_exception(
                            type, param, tb, file=sys.stderr)

                # import the user_keybinds on the end to avoid
                # issues with modules not loading
                try:
                    import user_keybinds
                except Exception:
                    pass

            except Exception:
                e = sys.exc_info()
                print('Error on line %s %s %s ' %
                      (sys.exc_info()[-1].tb_lineno, type(e).__name__, e))
