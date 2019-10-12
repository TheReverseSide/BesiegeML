'''Opens game from vscode, takes screenshot, calcuates score from screenshot'''
import sys
import time

import numpy as np
import pyautogui as pyag
import PIL.ImageGrab


def back_to_game():
    '''Command tabs back into game - MAC SPECIFIC CURRENTLY'''
    pyag.hotkey('command', 'tab')
    pyag.press('space')
    time.sleep(1)
    pyag.press('c')


def copy_screen():
    '''Copies screenshot to clipboard, then command tabs back to vscode - MAC SPECIFIC CURRENTLY'''
    pyag.hotkey('command', 'ctrl', 'shift', '4')
    pyag.press('space')
    pyag.keyDown('option')
    pyag.click(x=700, y=500)
    pyag.keyUp('option')
    pyag.press('space')
    pyag.hotkey('command', 'tab')


def process_image():
    '''Grabs image and calculates score from pixels'''
    # im = Image.open('./example_scrnsht.png')
    img_ = PIL.ImageGrab.grabclipboard()

    np_im = np.array(img_) # Shape: (1772, 2304, 3)
    _, max_score, _ = np_im.shape
    target_slice = np_im[-5, :, 0]

    result = np.where(target_slice < 100)[0][0]
    score = 100*result/max_score
    print(f"Score: {score:.1f}")
    # print(target_slice[result-3:result+3])


def main():
    '''Main. Pylint leave me alone.'''
    np.set_printoptions(threshold=sys.maxsize)
    back_to_game()
    time.sleep(5)
    copy_screen()
    process_image()


if __name__ == '__main__':
    main()
