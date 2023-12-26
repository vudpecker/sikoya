"""with exception handling"""

from pathlib import Path


path =  Path('pi_value.txt') # if relative path ..\..\pi_value.txt possible?

def print_path(path):
        

    try:
        contents = path.read_text()

    except FileNotFoundError:
        print(f"The file {path} does not exist")
        #pass #fail silently!

    else:    
        print(contents.rsplit())

if __name__ == '__main__':
    print("printing the patch...")
    print_path(path)
