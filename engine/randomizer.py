import random

def randomize_scene(story):
    # Menambahkan elemen acak untuk replayability
    random.shuffle(story["scenes"])
    return story
