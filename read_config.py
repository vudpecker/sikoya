
import configparser
import logging.config

class PersistData:
    config = configparser.ConfigParser()
    config.read("resources/fileprocessor.ini")

    def __init__(self) -> None:
        self.logging.getLogger(f"Log is {config}")