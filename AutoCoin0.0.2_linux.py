#Packages
import time
from PIL import ImageGrab
import numpy as nm
import pytesseract
import cv2
import argparse
import imutils
from pynput.mouse import Button, Controller
import os
#Configurations
detect = "null"
mouse = Controller()

#coinGameDetector
def coinGameDetector():
    while(True):
        cap = ImageGrab.grab(bbox =(860, 190, 1056, 218))
        detection = pytesseract.image_to_string(
                cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),
                lang ='eng')
        if 'Drag' in detection:
            print('Drag To Align Selected!\n')
            detect = "DragToAlign"
            break
        elif 'Pair' in detection:
            print('Tap The Pair Selected!\n')
            detect = "TapThePair"
            break
        elif 'Swipe' in detection:
            print('Swipe To Match Selected!\n')
            detect = "SwipeToMatch"
            break
        elif 'Tap' in detection:
            print('Tap The Colors Selected!\n')
            detect = "TapTheColors"
            break
    if "SwipeToMatch" in detect:
        print("detection completed, solving.\n")
        SwipeToMatch()
    elif "TapTheColors" in detect:
        print("detection completed, solving.\n")
        TapTheColors()
    elif "DragToAlign" in detect:
        print("detection completed, solving.\n")
    elif 'TapThePair' in detect:
        print("detection completed, solving.\n")

#SwipeToMatch Optimizes(ationz(s({value for value in variable})))
# def stmOptimize():
#     os.system("xdotool search --name user@system windowactivate %@")
#     print("Yay, ;; Terminal brought to front!")

#SwipeToMatch Quick Rematcher * Used By SwipeToMatch
def stmQuick():
    stmQuickGrab = ImageGrab.grab(bbox =(860, 190, 1056, 218))
    stmQuickDetection = pytesseract.image_to_string(
            cv2.cvtColor(nm.array(stmQuickGrab), cv2.COLOR_BGR2GRAY),
            lang ='eng')
    if 'Swipe' in stmQuickDetection:
        print('Swipe To Match Requed!\n')
        os.system("xdotool search --name user@system windowactivate %@")
        SwipeToMatch()

#SwipeToMatch
def SwipeToMatch():
    svol = 0
    stemp = 0
    scoords = [(781, 455, 783, 457), (1015, 292, 1017, 294), (789, 859, 791, 861), (1134, 510, 1136, 512), (953, 507, 955, 509)]
    stcolorlist = []
    roundnum = 0
    for x in range(5 + svol):
        stb = ImageGrab.grab(bbox =(scoords[stemp]) )
        stcolor = stb.getcolors(1)
        if stcolor != "None":
            stcolorlist.append(stcolor)
            stemp = stemp + 1
            continue
        else:
            svol = svol + 1
            continue

#LeftTopBottomRightMiddle

        # imgTwoByTwoLeft = ImageGrab.grab(bbox =(781, 455, 783, 457) )
        # swipeColorsLeft = imgTwoByTwoLeft.getcolors(1)
        # print(swipeColorsLeft)
        # if swipeColorsLeft == "none":
        #     print("Error, looping!")
        #     continue
        # imgTwoByTwoTop = ImageGrab.grab(bbox =(1015, 292, 1017, 294) )
        # swipeColorsTop = imgTwoByTwoTop.getcolors(1)
        # print(swipeColorsTop)
        # if swipeColorsTop == "none":
        #     print("Error, looping!")
        #     continue
        # imgTwoByTwoBottom = ImageGrab.grab(bbox =(789, 859, 791, 861) )
        # swipeColorsBottom = imgTwoByTwoBottom.getcolors(1)
        # print(swipeColorsBottom)
        # if swipeColorsBottom == "none":
        #     print("Error, looping!")
        #     continue
        # imgTwoByTwoRight = ImageGrab.grab(bbox =(1134, 510, 1136, 512) )
        # swipeColorsRight = imgTwoByTwoRight.getcolors(1)
        # print(swipeColorsRight)
        # if swipeColorsRight == "none":
        #     print("Error, looping!")
        #     continue
        # imgTwoByTwoMiddle = ImageGrab.grab(bbox =(953, 507, 955, 509) )
        # swipeColorsMiddle = imgTwoByTwoMiddle.getcolors(1)
        # print(swipeColorsMiddle)
        # print("\n")
        # if swipeColorsMiddle == "none":
        #     print("Error, looping!")
        #     continue
        # roundnum = 0
        # break

    if stcolorlist[4] == stcolorlist[0]:
        print("Swiping Left!")
        mouse.position = (783, 618)
        time.sleep(0.1)
        mouse.press(Button.left)
        #time.sleep(0.1)
        mouse.release(Button.left)
        print("Completed!" + " Round " + str(roundnum) + "!")
        roundnum = roundnum + 1
        time.sleep(3)
        stmQuick()

    elif stcolorlist[4] == stcolorlist[1]:
        print("Swiping Up!")
        mouse.position = (904, 289)
        time.sleep(0.1)
        mouse.press(Button.left)
        #time.sleep(0.1)
        mouse.release(Button.left)
        print("Completed!" + " Round " + str(roundnum) + "!")
        roundnum = roundnum + 1
        time.sleep(3)
        stmQuick()

    elif stcolorlist[4] == stcolorlist[2]:
        print("Swiping Down!")
        mouse.position = (983, 853)
        time.sleep(0.1)
        mouse.press(Button.left)
        #time.sleep(0.1)
        mouse.release(Button.left)
        print("Completed!" + " Round " + str(roundnum) + "!")
        roundnum = roundnum + 1
        time.sleep(3)
        stmQuick()

    elif stcolorlist[4] == stcolorlist[3]:
        print("Swiping Right!")
        mouse.position = (1133, 530)
        time.sleep(0.1)
        mouse.press(Button.left)
        #time.sleep(0.1)
        mouse.release(Button.left)
        print("Completed!" + " Round " + str(roundnum) + "!")
        roundnum = roundnum + 1
        stmQuick()

#TapTheColors Quick Rematcher
def ttcQuick():
    ttcQuickGrab = ImageGrab.grab(bbox =(860, 190, 1056, 218))
    ttcQuickDetection = pytesseract.image_to_string(
            cv2.cvtColor(nm.array(ttcQuickGrab), cv2.COLOR_BGR2GRAY),
            lang ='eng')
    if 'Tap' in ttcQuickDetection:
        print('TapTheColors Requed!\n')
        mouse.position = (960, 540)
        TapTheColors()

#TapTheColors
def TapTheColors():
    tbc = [(770, 380, 772, 382), (910, 381, 912, 383), (1050, 380, 1052, 382), (771, 529, 773, 531), (906, 523, 908, 525), (1050, 519, 1052, 521), (765, 666, 767, 668), (905, 665, 907, 667), (1056, 672, 1058, 674)]
    ttcolorlist = []
    bn = 0
    tvol = 0
    for x in range(9 + tvol):
        ttb = ImageGrab.grab(bbox=tbc[bn])
        ttcolor = ttb.getcolors(1)
        if ttcolor != "None":
            ttcolorlist.append(ttcolor)
            bn = bn + 1
            continue
        else:
            tvol = tvol + 1
            continue

    lallpos = [(772, 382), (912, 383), (1052, 382), (773, 531), (908, 525), (1052, 521), (767, 668), (907, 667), (1058, 674)]
    ycurrentpos = 0
    for x in range(9):
        if ttcolorlist[ycurrentpos] != [(4, (85, 85, 87))]:
            print(ttccolorlist[ycurrentpos])
            mouse.position = (lallpos[ycurrentpos])
            time.sleep(0.1)
            mouse.press(Button.left)
            time.sleep(0.3)
            mouse.release(Button.left)
            ttcQuick()
        else:
            ycurrentpos = ycurrentpos + 1
            continue #TTC Solver


coinGameDetector()
