'''Opens game from vscode, takes screenshot, calcuates score from screenshot'''
import os
import shutil
import sys
import time

import numpy as np
import pyautogui as pyag
import PIL.ImageGrab


def initialize_game_mac():
    '''Command tabs back into game'''

    #* MAC *#
    pyag.hotkey('command', 'tab')
    pyag.press('space')
    time.sleep(1)
    pyag.press('c')


def initialize_game_win(filename):
    print("initialize_game_win()")
    #* WINDOWS *#
    pyag.hotkey('alt', 'tab')
    load_save(filename)
    # load_save("train_0_1")
    pyag.press('space')
    time.sleep(1)
    operate_machine()


def operate_machine():
    pyag.typewrite("cykt")  # Various key bindings for all weapons


def copy_screen_mac():
    '''Copies screenshot to clipboard, then command tabs back to vscode - MAC SPECIFIC CURRENTLY'''

    #* MAC *#
    pyag.hotkey('command', 'ctrl', 'shift', '4')
    pyag.press('space')
    pyag.keyDown('option')
    pyag.click(x=700, y=500)
    pyag.keyUp('option')
    pyag.press('space')
    pyag.hotkey('command', 'tab')


def copy_screen_win():
    #* WINDOWS *#
    print("copy_screen_win()")
    pyag.hotkey('printscreen', 'alt')  #? Check that this works
    pyag.press('space')


def process_image():
    '''Grabs image and calculates score from pixels'''
    print(f"process_image()")

    # im = Image.open('./example_scrnsht.png')
    img_ = PIL.ImageGrab.grabclipboard() # Windows and Mac friendly

    # img_.show()

    np_im = np.array(img_) # Shape: (1772, 2304, 3) #! Not windows friendly
    max_score = 1877
    # print("Shape: ", np_im.shape)
    # print(max_score)
    target_slice = np_im[1060, 21:1898, 0]

    result = np.where(target_slice < 100)[0][0]
    score = 100*result/max_score
    print(f"\nScore: {score:.1f}")
    return score
    # print(target_slice[result-3:result+3])


def retard_click(x, y):
    print(f"A very retarded click: retard_click({x}, {y})")
    pyag.moveTo(x, y)
    pyag.mouseDown()
    time.sleep(0.1)
    pyag.mouseUp()


def load_save(filename):
    print(f"load_save({filename})")

    retard_click(432, 60)

    for _ in range(20):
        pyag.press('backspace')

    pyag.typewrite(filename)
    retard_click(x=1226, y=194)


def reset_game():
    print('reset_game()')
    time.sleep(1)
    load_save("scorpion_mess")


def get_score():
    print("score_function()")
    time.sleep(5) # Should be killing people
    copy_screen_win()
    process_image()


def sandbox():
    save_candidate()


def print_mouse_pos():
    while True:
        print(pyag.position())
        time.sleep(2)


def score_function(filename):
    print(f"score_function({filename})")
    np.set_printoptions(threshold=sys.maxsize)
    initialize_game_win(filename)
    get_score()
    reset_game()


def parse_args():
    try:
        time_limit = float(sys.argv[1])
        return time_limit
    except:
        print('Execute in following format:')
        print('python solver.py [time limit in seconds]')
        sys.exit()


def generate_candidate():
    pass


def save_candidate():
    directory = r"D:\Games\steamapps\common\Besiege\Besiege_Data\SavedMachines"
    candidate = os.path.join(directory, "candidate.bsg")
    best = os.path.join(directory, "best.bsg")
    shutil.copyfile(candidate, best)


def main():
    '''Your most beloved random search <3'''
    time_limit = parse_args()
    execution_start = time.time()
    cand_score = 0
    while time.time() - execution_start < time_limit:
        generate_candidate()
        cand_score = score_function('candidate')
        if cand_score > best_score:
            best_score = cand_score
            save_candidate()
        break


if __name__ == '__main__':
    # main()
    sandbox()
