import csv
import json


class FileModule:
    def __init__(self):
        self.butt = ""

    @staticmethod
    def load_credentials():
        """
        Reads credentials from a json file
        :return: Credential Dictionary Object
        """
        with open('credentials.json', 'r') as cred_file:
            json_dump = json.load(cred_file)
        return json_dump

    @staticmethod
    def load_names():
        """
        Reads in a full file
        :return: File Contents
        """
        with open('useful_stuff/names.txt', 'r') as name_file:
            names = name_file.read()
        return list(names.split('\n'))
