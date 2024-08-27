import pyautogui
import time

from constants import MAIN_INTERVAL
import craft_game
from images import BTN_CLAIM, BTN_START_GAME

pyautogui.FAILSAFE = True

def main_cycle():
    is_running = True
    while is_running:
        check_craft_game()
        check_claim()
        time.sleep(MAIN_INTERVAL)


def check_craft_game():
    try:
        start_game = pyautogui.locateCenterOnScreen(BTN_START_GAME, grayscale=False, confidence=0.9)
        pyautogui.click(start_game)
        time.sleep(2)
        craft_game.craft_game()
    except pyautogui.ImageNotFoundException:
        print('Craft game is not ready yet!')

def check_claim():
    try:
        claim = pyautogui.locateCenterOnScreen(BTN_CLAIM, grayscale=False, confidence=0.9)
        pyautogui.click(claim)
    except pyautogui.ImageNotFoundException:
        print('Claim is not ready yet!')

main_cycle()