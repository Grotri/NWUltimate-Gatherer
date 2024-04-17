import pyautogui
import cv2
import numpy as np
import gamemoves as gm


def hempdetect():
    pyautogui.screenshot(region=(0, 0, 1920, 1080), imageFilename='test.jpg')
    hemp = cv2.imread('hemp.jpg')
    screen = cv2.imread('test.jpg')

    colormin = np.array((230, 230, 230), np.uint8)
    colormax = np.array((255, 255, 255), np.uint8)
    check = cv2.inRange(hemp, colormin, colormax)
    res = cv2.inRange(screen, colormin, colormax)

    answ = cv2.matchTemplate(res, check, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(answ)
    top_left = max_loc
    bottom_right = (top_left[0] + 100, top_left[1] + 30)
    cv2.rectangle(screen, top_left, bottom_right, (0, 255, 0), 2)

    threshold = 0.8
    flag = False
    if np.amax(answ) > threshold:
        flag = True
        print('Hemp detected')
    else:
        print('Hemp not detected')
    return flag

def inits():
    pyautogui.screenshot(region=(953, 19, 12, 23), imageFilename='test.jpg')
    hemp = cv2.imread('spic.jpg')
    screen = cv2.imread('test.jpg')

    colormin = np.array((215, 215, 215), np.uint8)
    colormax = np.array((255, 255, 255), np.uint8)
    check = cv2.inRange(hemp, colormin, colormax)
    res = cv2.inRange(screen, colormin, colormax)

    answ = cv2.matchTemplate(res, check, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(answ)
    top_left = max_loc
    bottom_right = (top_left[0] + 100, top_left[1] + 30)
    cv2.rectangle(screen, top_left, bottom_right, (0, 255, 0), 2)

    threshold = 0.5
    flag = False
    if np.amax(answ) > threshold:
        flag = True
    return flag

def finalinit():
    flag = inits()
    while flag != True:
        gm.mousehalfdeg(10)
        flag = inits()