import pyautogui
import time

import craft_game
from images import BTN_START_GAME

pyautogui.FAILSAFE = True

start_game = pyautogui.locateCenterOnScreen(BTN_START_GAME, grayscale=True, confidence=0.9)
pyautogui.click(start_game)
time.sleep(2)

craft_game.craft_game()