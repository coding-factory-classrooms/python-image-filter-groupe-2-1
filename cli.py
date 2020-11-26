import sys
import main
import configparser

args = sys.argv
print(f"args={args}")

if args[1] == "-h":
    print("usage: imagefilter \n -h,--help \n -i,--img-dir <directory> \n -o,--output-dir <directory> \n -f,--filters")
elif args[1] == "-i" and args[3] == "-o" and args[5] == "-f":
    input_arg = args[2]
    output_arg = args[4]
    filter_arg = args[6]
    main.filter(input_arg, output_arg, filter_arg)
elif args[1] == "--config-file" and args[2] == "image.ini":
    config = configparser.ConfigParser()
    config.read("image.ini")
    with open('image.ini', 'w') as configfile:
        config.write(configfile)
        content = config['filters']['content']
        input = config['general']["input_dir"]
        output = config['general']["output_dir"]
        main.filter(input, output, content)






