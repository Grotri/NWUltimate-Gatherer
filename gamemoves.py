import pyautogui

import detect
import mousetest
import time

def coordCorrect(pic, i):
    hempposesx = [196, 212, 215, 215, 221, 224, 224, 531, 533, 536, 540, 585, 587, 594, 594, 587, 657, 650, 646,
                  655, 656, -407, -399, -405, -398, -357, -348, -347, -340, -291, -291, -288, -285, -286, -225,
                  -228, -223, -225, -172, -162, -172, -173, -179, 417, 420, 417, 428, 425, 548, 550, 546, 560,
                  652, 663, 662, 668, 597, 597, 605, 604, 613, 721, 721, 718, 728, -235, -229, -227, -222, -124,
                  -117, -112, -108, 435, 435, 442, 445, 445, 314, 315, 313, 320, 307, 300, 298, 304, 309, 301,
                  305, 443, 445, 450, 445, 378, 374, 371, 264, 263, 257, 252, 251, 198, 191, 198, 199, 202,
                  309, 313, 310, 307, 325, 327, 334, 336, 331, 327, 331, 385, 381, 375, 376, 553, 557, 559,
                  556, 561, 612, 619, 618, 622, 564, 556, 559, 561, 608, 614, 614, 622, 620, 667, 670, 675,
                  678, 682, -660, -657, -662, -661, -656, -549, -545, -550, -545, -546, -599, -608, -608, -603,
                  -600, -693, -695, -695, -689, -686, -644, -642, -644, -637, -566, -572, -572, -576, -570,
                  -514, -511, -504, -505, -465, -461, -460, -456, -342, -331, -338, -342, -335, -284, -277, -272,
                  -268, -276, -163, -161, -159, -156, -152, -170, -174, -180, -177, -294, -302, -301, -304]
    hempposesy = [-215, -208, -211, -207, -198, -202, -197, -160, -157, -152, -158, -61, -57, -56, -48, -47, 46, 48,
                  55, 52, 58, 348, 343, 342, 335, 229, 233, 239, 238, 132, 126, 117, 123, 130, 228, 234, 235,
                  244, 324, 332, 333, 340, 335, -169, -167, -163, -160, -166, -175, -164, -158, -165, -166, -163,
                  -169, -170, -260, -266, -262, -268, -273, -270, -277, -281, -281, -299, -292, -299, -299, -289,
                  -289, -283, -293, 344, 339, 336, 342, 332, 336, 329, 324, 323, 298, 298, 294, 294, 292, 290,
                  288, 137, 130, 126, 123, 17, 14, 20, 15, 21, 18, 21, 15, -74, -81, -83, -88, -91,
                  -89, -92, -85, -78, -77, -72, -73, -79, -82, -80, -77, -181, -189, -193, -198, -288, -293, -286,
                  -279, -276, -198, -196, -185, -186, -77, -75, -73, -70, 15, 19, 26, 18, 15, -84, -87, -82,
                  -79, -77, 162, 154, 150, 145, 148, 143, 142, 150, 148, 154, 254, 256, 265, 259, 264, -206,
                  -200, -192, -197, -191, -101, -94, -88, -98, -188, -189, -196, -200, -204, -306, -301,
                  -307, -301, -212, -214, -199, -206, -209, -207, -203, -197, -198, -89, -89, -88, -93, -96,
                  -304, -310, -315, -305, -314, 144, 154, 156, 147, 149, 155, 147, 138]
    forward_time = 0.078
    back_time = 0.127

    testx, testy = pyautogui.locateCenterOnScreen(pic, confidence=0.7)
    posx, posy = pyautogui.locateCenterOnScreen('position.jpg', confidence=0.7)
    finderx = testx - posx
    findery = testy - posy
    difx = finderx - hempposesx[i]
    dify = findery - hempposesy[i]

    print(difx, dify)

    if not(-1 <= dify <= 1) or not(-1 <= difx <= 1):
        if abs(difx) > 45 or abs(dify) > 45:
            pyautogui.keyDown('w')
            time.sleep(forward_time * 5)
            pyautogui.keyUp('w')
            time.sleep(5)
            coordCorrect(pic, i)
        else:
            if difx > 1:
                pyautogui.keyDown('s')
                time.sleep(back_time * difx)
                pyautogui.keyUp('s')
                time.sleep(0.1)
            elif difx < -1:
                pyautogui.keyDown('w')
                time.sleep(forward_time * abs(difx))
                pyautogui.keyUp('w')
                time.sleep(0.1)

            if dify > 1:
                pyautogui.keyDown('a')
                time.sleep(forward_time * dify)
                pyautogui.keyUp('a')
                time.sleep(0.1)
            elif dify < -1:
                pyautogui.keyDown('d')
                time.sleep(forward_time * abs(dify))
                pyautogui.keyUp('d')
                time.sleep(0.2)
            coordCorrect(pic, i)

def addCords(pic):
    testx, testy = pyautogui.locateCenterOnScreen(pic, confidence=0.9)
    posx, posy = pyautogui.locateCenterOnScreen('position.jpg', confidence=0.7)
    posx2 = 960
    posy2 = 540
    finderx = testx - posx
    findery = testy - posy
    finderx2 = testx - posx2
    findery2 = testy - posy2

    print(finderx, findery)
    print(finderx2, findery2)

def mousehalfdeg(x):
    init_x = int(x / 10)
    for i in range(0, init_x):
        mousetest.MouseMoveTo(10, 0)
        time.sleep(0.01)

def mousemove(x):
    init_x = int(x / 20)
    for i in range(0, init_x):
        mousetest.MouseMoveTo(20, 0)
        time.sleep(0.01)

def mousemovefif(x):
    init_x = int(x / 30)
    for i in range(0, init_x):
        mousetest.MouseMoveTo(30, 0)
        time.sleep(0.01)

def backmousemove(x):
    init_x = int(x / 20)
    for i in range(0, init_x):
        mousetest.MouseMoveTo(-20, 0)
        time.sleep(0.01)

def backmousemovefif(x):
    init_x = int(x / 30)
    for i in range(0, init_x):
        mousetest.MouseMoveTo(-30, 0)
        time.sleep(0.01)

def fifteendegreesmove():
    mousemovefif(300)

def backfifteendegreesmove():
    backmousemovefif(300)

def sevandfivedegreesmove():
    mousemovefif(150)

def backsevandfivedegreesmove():
    backmousemovefif(150)

def onedegreemove():
    mousemove(20)

def backonedegreemove():
    backmousemove(20)

def hemptpfrompoint():
    pyautogui.press('m')
    time.sleep(1)
    pyautogui.moveTo(1855, 950, 0.2)
    time.sleep(0.3)
    pyautogui.click()
    time.sleep(0.15)
    pyautogui.click()
    time.sleep(0.15)
    pyautogui.click()
    time.sleep(0.15)
    pyautogui.click()
    time.sleep(0.15)
    pyautogui.moveTo(1860, 1010, 0.1)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(965, 425, 0.25)
    time.sleep(0.5)
    pyautogui.moveTo(770, 550, 0.2)
    time.sleep(0.15)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(1100, 650, 0.2)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(30)

def hemplilbush(pic, i):
    coordCorrect(pic, i)
    pyautogui.press('m')
    time.sleep(0.2)
    flag = detect.hempdetect()
    if flag == True:
        pyautogui.press('e')
        time.sleep(1.5)
    pyautogui.press('m')
    time.sleep(0.2)
    i += 1

    return i

def hempbigbush(pic, i):
    coordCorrect(pic, i)
    pyautogui.press('m')
    time.sleep(0.2)
    flag = detect.hempdetect()
    if flag == True:
        pyautogui.press('e')
        time.sleep(3)
    pyautogui.press('m')
    time.sleep(0.2)
    i += 1

    return i