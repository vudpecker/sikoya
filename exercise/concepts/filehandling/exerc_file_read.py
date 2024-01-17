import logging
from pathlib import Path

choice = input("Do you want to access pi full value?\n")

#path =  Path("\WorkHome\Raaj\PyProject\sikoya\exercise\filehandling\pi_value.txt") # absolute path 
if choice.lower() == "yes":
    path = Path("exercise\\filehandling\pi_value_full.txt") #relative path
else:
    path =  Path("exercise\\filehandling\pi_value.txt") #relative path


def print_path(path):     
    """file operations with exception handling"""

    logging.basicConfig(level = "DEBUG")
    try:
        #contents = path.read_text()
        contents = path.read_text().rstrip() # to strip trailing newline characters

    except FileNotFoundError:
        print(f"The file {path} does not exist")
        #pass #fail silently!

    else:

        logging.debug(f"The file content is {contents}")
        #print(contents.rstrip()) #to strip trailing newline characters
        
        lines = contents.splitlines()
        logging.debug(f"The file content is {lines}")
        pi_string = ""
        for line in lines:
            line = line.rstrip()
            pi_string += line.lstrip()
        
        print(pi_string)

        if choice:
            print(f"{pi_string[:52]}...")

        
if __name__ == '__main__':
    print("printing the value of pi...")
    print_path(path)
