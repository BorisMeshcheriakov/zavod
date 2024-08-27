import time
import pyautogui

from images import BTN_CLOSE, BTN_CRATE, BTN_TO_WAREHOUSE, BTN_WAREHOUSE_SUBMIT, MSG_BATCH_DEFECTIVE


def craft_game():
    pyautogui.scroll(-40)
    time.sleep(1)

    game_over = False

    while not game_over:
        crates = pyautogui.locateAllOnScreen(BTN_CRATE, grayscale=True, confidence=0.9)

        for pos in crates:
            try:
                pyautogui.locateOnScreen(MSG_BATCH_DEFECTIVE, grayscale=True, confidence=0.9)
                print('Batch defective! Returning to main screen...')
                game_over = True
                break
            except pyautogui.ImageNotFoundException:
                print(f'Clicking crate in position, {pos}')
                crate = pyautogui.center(coords=pos)
                for click in range(0, 3):
                    pyautogui.click(crate)
                    time.sleep(0.5)
                time.sleep(1)

                try:
                    warehouse = pyautogui.locateCenterOnScreen(BTN_TO_WAREHOUSE, grayscale=False, confidence=0.9)
                    pyautogui.click(warehouse)
                    time.sleep(1)
                    warehouse_submit = pyautogui.locateCenterOnScreen(BTN_WAREHOUSE_SUBMIT, grayscale=False, confidence=0.9)
                    pyautogui.click(warehouse_submit)
                    time.sleep(1)
                except pyautogui.ImageNotFoundException:
                    continue

    close = pyautogui.locateCenterOnScreen(BTN_CLOSE, grayscale=True, confidence=0.9)
    pyautogui.click(close)

