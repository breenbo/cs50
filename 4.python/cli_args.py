import sys

if len(sys.argv) != 2:
    print("Missing command line argument")
    exit(1) # c return equivalent

print("Hello {} !".format(sys.argv[1]))
exit(0)
