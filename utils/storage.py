import json
import os

FILE_PATH = "user_data/profile.json"


def save_profile(profile):

    with open(FILE_PATH, "w") as file:
        json.dump(profile, file, indent=4)


def load_profile():

    if not os.path.exists(FILE_PATH):
        return {}

    with open(FILE_PATH, "r") as file:
        return json.load(file)