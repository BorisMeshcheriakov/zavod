import time
import pyautogui

from constants import CRAFT_GAME_ACTION
from images import BTN_CLOSE, BTN_CRATE, BTN_SELL, BTN_TO_WAREHOUSE, BTN_WAREHOUSE_SUBMIT, MSG_BATCH_DEFECTIVE


def craft_game():
    pyautogui.scroll(-40)
    time.sleep(1)

    game_end_reason = None

    while game_end_reason is None:
        game_end_reason = check_game_ended()
        if game_end_reason is not None:
            break
            

        crates = None

        try: 
            # Wait, until game board is loading or "lvlup" animation is playing
            crates = pyautogui.locateAllOnScreen(BTN_CRATE, grayscale=True, confidence=0.9)
        except pyautogui.ImageNotFoundException:
            time.sleep(1)
            continue

        for pos in crates:
            game_end_reason = check_game_ended()
            if game_end_reason is not None:
                break

            print(f'Clicking crate in position, {pos}')
            crate = pyautogui.center(coords=pos)
            for click in range(0, 3):
                pyautogui.click(crate)
                time.sleep(0.5)
            time.sleep(1)
    
    on_game_end(game_end_reason)

def check_game_ended():
    reason_ended = None
    possible_endings = [BTN_TO_WAREHOUSE, MSG_BATCH_DEFECTIVE]
    for ending in possible_endings:
        try:
            pyautogui.locateCenterOnScreen(ending, grayscale=False, confidence=0.9)
            reason_ended = ending
        except pyautogui.ImageNotFoundException:
            pass
    return reason_ended 

def on_game_end(reason):
    if reason == BTN_TO_WAREHOUSE:
        print('Ready to fill warehouse!')
        send_to_warehouse()

    if reason == MSG_BATCH_DEFECTIVE:
        print('Batch defective! Returning to main screen...')
        quit_craft_game()

def send_to_warehouse():
    try:
        if CRAFT_GAME_ACTION == 'warehouse':
            warehouse = pyautogui.locateCenterOnScreen(BTN_TO_WAREHOUSE, grayscale=False, confidence=0.9)
            pyautogui.click(warehouse)
            time.sleep(1)
            warehouse_submit = pyautogui.locateCenterOnScreen(BTN_WAREHOUSE_SUBMIT, grayscale=False, confidence=0.9)
            pyautogui.click(warehouse_submit)
            

        if CRAFT_GAME_ACTION == 'sell':
            sell = pyautogui.locateCenterOnScreen(BTN_SELL, grayscale=False, confidence=0.9)
            pyautogui.click(sell)

        # Start game again
        time.sleep(1)
        craft_game()
    except pyautogui.ImageNotFoundException:
        print('Can`t sent to warehouse!')

def quit_craft_game():
    close = pyautogui.locateCenterOnScreen(BTN_CLOSE, grayscale=True, confidence=0.9)
    pyautogui.click(close)