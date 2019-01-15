import py_compile
from glob import glob

#fout = open("make.py","w")
for n in glob("*.py"):
    if n != "comp.py":
        #fout.write("import " + n[:-3]+"\n")
        py_compile.compile(n)
#fout.close()
