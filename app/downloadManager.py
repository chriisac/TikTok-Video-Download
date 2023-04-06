import json


class Download:
    def __init__(self, id, file_name):
        self.id = id
        self.fileName = file_name
        self.progress = 0
        self.status = "Initializing"

    def update_file_name(self, name):
        self.fileName = name

    def update_progress(self, new_progress):
        self.progress = new_progress

    def update_status(self, new_status):
        self.status = new_status


class DownloadList:
    def __init__(self):
        self.id = 0
        self.list = {}

    def add(self, filename):
        self.id += 1
        self.list[self.id] = Download(self.id, filename)
        return True

    def get(self):
        list_to_json = {}
        for item in self.list:
            list_to_json[item] = self.list[item].__dict__
        return list_to_json

