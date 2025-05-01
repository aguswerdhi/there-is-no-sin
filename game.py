from engine.story_loader import load_story
from engine.game_logic import run_game
from engine.endings import show_ending
from engine.randomizer import randomize_scene
from engine.philosophy import get_philosophical_quote
from time import sleep

def display_intro():
    with open("assets/intro.txt", "r") as f:
        for line in f:
            print(line.strip())
            sleep(1.5)

if __name__ == "__main__":
    display_intro()
    story = load_story("story/main_story.json")
    karma = run_game(story)
    show_ending(karma)
