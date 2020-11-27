import os
import sys

import main
import configparser

"""
The first condition can show a information menu.
The second condition can check arguments and retrieve others arguments who will them send in the file main.py
The third condition can check arguments, manage configuration file "image.ini" and retrieve arguments file
    who will them send in the file main.py
"""

args = sys.argv
menu_help = "usage: imagefilter \n -h,--help \n -i,--img-dir <directory> \n -o,--output-dir <directory> \n -f, " \
            "--filters \n --config-file, <file> \n --list-filters"

if args[1] == "-h":
    print(menu_help)
elif args[1] == "-i" and args[3] == "-o" and args[5] == "-f":
    input_arg = args[2]
    output_arg = args[4]
    filter_arg = args[6]
    main.filter(input_arg, output_arg, filter_arg)
elif args[1] == "--config-file":
    ini_file = args[2]
    if not os.path.isfile(ini_file):
        print(f"The file does not exist : {ini_file}")
    elif not ini_file.endswith(".ini"):
        print(f"The file is not in good format : {ini_file.split('.')[1]} !")
    else:
        config = configparser.ConfigParser()
        config.read(ini_file)
        with open(ini_file, 'w') as configfile:
            config.write(configfile)
            content = config['filters']['content']
            input = config['general']["input_dir"]
            output = config['general']["output_dir"]
            main.filter(input, output, content)
elif args[1] == "--list-filters":
    print("Filters :")
    with os.scandir("filtres") as entries:
        if os.path.exists("filtres"):
            for entry in entries:
                if not entry.name.startswith("__"):
                    print(f"{entry.name}")
else:
    print("YOU MADE A MISTAKE IN THE ORDER !")
    print(menu_help)







