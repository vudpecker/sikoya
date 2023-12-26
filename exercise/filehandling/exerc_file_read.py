import logging
from pathlib import Path


#path =  Path("\WorkHome\Raaj\PyProject\sikoya\exercise\filehandling\pi_value.txt") # absolute path 
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
            pi_string += line.lstrip()
        
        print(pi_string)

        
if __name__ == '__main__':
    print("printing the value of pi...")
    print_path(path)
