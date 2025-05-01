import json

def load_story(filepath):
    with open(filepath, "r") as f:
        return json.load(f)
