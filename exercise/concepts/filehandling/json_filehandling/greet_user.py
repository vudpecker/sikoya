from pathlib import Path
import json


def greet_user():
    
    my_file = Path("exercise\\json_filehandling\\users.json")
    if my_file.exists():
        #username = "raaj"
        #content = json.dumps(username)
        #my_file.write_text(content)

        content = my_file.read_text()
        username_read = json.loads(content)
        print(username_read)

greet_user()
