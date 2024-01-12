import sys

if len(sys.argv) == 1:
    print("missing command line arguments")
    sys.exit(1)
else:
    print(f"Hello {sys.argv[1]}") # use echo $? for echocing the exit code
    sys.exit(0)