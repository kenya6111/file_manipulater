pathname = '/home/kenya/recursion/python_practice/test.txt'
import sys

with open(pathname) as f:
    contents = f.read()


with open(pathname ,'w') as f:
    f.write(contents+"\nAppending more text to fileeeeeeee")


def reverse(inputpath,outputpath ):
    with open(inputpath,'r') as f:
        data = f.read()

    with open(outputpath,'w') as f:
        f.write(data[::-1])

def copy(inputpath,outputpath):
    with open(inputpath,'r') as f:
        data = f.read()

    with open(outputpath,'w') as f:
        f.write(data)

def duplicate(inputpath,n ):
    with open(inputpath,'r') as f:
        data = f.read()

    with open(inputpath,'w') as f:
        f.write(data*int(n))

def replace_string(inputpath, needle, newstring):
    with open(inputpath, 'r') as f:
        data = f.read()
    with open(inputpath, 'w') as f:
        f.write(data.replace(needle, newstring))

if __name__ == "__main__":

    cmd = sys.argv[1]
    if cmd == "reverse":
        reverse(sys.argv[2], sys.argv[3])
    elif cmd == "copy":
        copy(sys.argv[2], sys.argv[3])
    elif cmd == "duplicate":
        duplicate(sys.argv[2], sys.argv[3])
    elif cmd == "replace-string":
        replace_string(sys.argv[2], sys.argv[3], sys.argv[4])
    




