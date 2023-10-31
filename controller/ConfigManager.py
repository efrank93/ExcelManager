import json
import os


def read_config():
    if not os.getcwd().endswith("/config"):
        os.chdir(os.getcwd() + "/config")
    with open("config.json") as json_data_file:
        return json.load(json_data_file)


def write_config(data):
    if not os.getcwd().endswith("/config"):
        os.chdir(os.getcwd() + "/config")
    with open("config.json", "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
