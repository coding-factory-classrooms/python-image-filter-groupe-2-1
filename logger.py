from datetime import datetime

def dump_log():
    """
    Open and read a file.
    """
    try:
        with open("imagefilter.log", "r") as r:
            content = r.read()
            print(content)
    except IOError as e:
        print(f"Ouverture du fichier impossible. Erreur {e}")


def write_log(message):
    """
    Saves the message in a log file and prints it in the console.
    :param message: the message o be append in the log file
    """
    now = datetime.now()
    timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
    formatted = f"{timestamp} - {message}"
    with open("imagefilter.log", "a") as w:
        w.write(formatted + "\n")
        print(formatted + "\n")