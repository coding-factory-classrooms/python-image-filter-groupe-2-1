import os
import sys


args = sys.argv
print(f"args={args}")

first_arg = args[1]

if first_arg == "-h":
    print("usage: imagefilter \n -h,----help \n -i,--img-dir <directory> \n -o,--output-dir <directory>")
elif first_arg == "-i":
    second_arg = args[2]
    with os.scandir(second_arg) as entries:
        if os.path.exists(second_arg):
            for entry in entries:
                print(entry.name)
elif first_arg == "-o":
    second_arg = args[2]
    with os.scandir(second_arg) as entries:
        if os.path.exists(second_arg):
            for entry in entries:
                print(entry.name)
