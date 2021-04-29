import os
import os.path
import sys

sys.path.append(__path__[0])

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


this_path = __path__[0]
scripts = getScripts(this_path)

# import the scripts
for s in scripts:
    # filter out any folders with names in parentheses, like in AE
    if len(s) > 2:
        if (s[0] == '(') and (s[int(len(s)-1)] == ')'):
            continue

    str = "import " + s
    try:
        exec(str)
        print(s,)
    except:
        import traceback
        sys.stderr.write("Could not import %s module:" % s)
        info = sys.exc_info()
        type = info[0]
        param = info[1]
        tb = info[2]
        traceback.print_exception(type, param, tb, file=sys.stderr)

# import the user_keybinds on the end to avoid issues with modules not loading
try:
    import user_keybinds
except:
    pass
print("\n")
