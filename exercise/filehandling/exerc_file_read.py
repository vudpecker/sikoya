"""with exception handling"""

from pathlib import Path

path =  Path('pi_value.txt')

try:
    contents = path.read_text()

except FileNotFoundError:
    #print(f"The file {path} does not exist")
    pass #fail silently!

else:    
    print(contents.rsplit())
