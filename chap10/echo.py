import sys

def echo(in_, out):
    for line in in_:
        out.write(line)

def echo2(in_, out):
    for line in in_:
        out.write("{0} {1}".format(len(line), line))

echo2(sys.stdin, sys.stdout)
