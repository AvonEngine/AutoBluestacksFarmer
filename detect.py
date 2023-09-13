import cv2
import numpy as np
import pytesseract
import time
import pyautogui
from screenshot import screenshot
import datetime
import os



pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files\Tesseract-OCR\tesseract.exe"



def is_bluestacks_open():
    screenshot("is_bluestacks_open")
    img = cv2.imread(r"F:\Documents\Python Scripts\Bluestacks\temp screenshots\is_bluestacks_open.jpg")
    img = img[0:1440, 0:2560]
    width, height = 1920, 1080
    img_resize = cv2.resize(img, (width, height))
    crop_img = img_resize[0:20, 30:140]
    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(gray)
    found_text = pytesseract.image_to_string(invert)
    #cv2.imshow("invert", invert)
    t = datetime.datetime.now()
    t = str(t)[:-7]
    complete_text = "BlueStacks"
    if str(found_text).find(complete_text) != -1:
        return True
    else:
        print("["+ str(t) + "]" + "error_not_open: " + found_text )
        return False



def is_bihourly_complete():
    screenshot("is_bihourly_complete")
    img = cv2.imread(r"F:\Documents\Python Scripts\Bluestacks\temp screenshots\is_bihourly_complete.jpg")
    img = img[0:1440, 0:2560]
    width, height = 1920, 1080
    img_resize = cv2.resize(img, (width, height))
    crop_img = img_resize[640:700, 1200:1600]
    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    found_text = pytesseract.image_to_string(gray)
    #cv2.imshow("gray", gray)
    t = datetime.datetime.now()
    t = str(t)[:-7]
    complete_text = "You have earned a sweepstake ticket"
    if str(found_text).find(complete_text) != -1:
        print("["+ str(t) + "]" + "is_bihourly_complete: True - " + found_text )
        return True
    else:
        print("["+ str(t) + "]" + "is_bihourly_complete: False - " + found_text )
        return False


def game_name():
    screenshot("game_name")
    img = cv2.imread(r"F:\Documents\Python Scripts\Bluestacks\temp screenshots\game_name.jpg")
    img = img[0:1440, 0:2560]
    width, height = 1920, 1080
    img_resize = cv2.resize(img, (width, height))
    crop_img = img_resize[610:660, 1200:1480]
    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    found_text = pytesseract.image_to_string(gray)
    #cv2.imshow("gray", gray)
    t = datetime.datetime.now()
    t = str(t)[:-7]
    print("["+ str(t) + "]" + "game_name: " + found_text)
    return(found_text)



def next_time_bihourly():
    directory = r'F:\Documents\Python Scripts\Bluestacks\temp screenshots'
    o_directory = r'F:\Documents\Python Scripts\Bluestacks'
    screenshot("next_time_bihourly")
    img = cv2.imread(r"F:\Documents\Python Scripts\Bluestacks\temp screenshots\next_time_bihourly.jpg")
    img = img[0:1440, 0:2560]
    width, height = 1920, 1080
    img_resize = cv2.resize(img, (width, height))
    crop_img = img_resize[710:750, 1200:1400]
    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    os.chdir(directory)
    filename = 'next_time_biFINAL.jpg'
    cv2.imwrite(filename, gray)
    os.chdir(o_directory)
    found_text = pytesseract.image_to_string(gray)
    #cv2.imshow("gray", gray)
    k = found_text.split(':')
    seconds = int(k[0])*3600 + int(k[1])*60 + int(k[2])
    t = datetime.datetime.now()
    t = str(t)[:-7]
    print("["+ str(t) + "]" + "next_time_bihourly: " + str(seconds) + "s")
    return seconds


def did_i_win():
    screenshot("did_i_win")
    img = cv2.imread(r"F:\Documents\Python Scripts\Bluestacks\temp screenshots\did_i_win.jpg")
    img = img[0:1440, 0:2560]
    width, height = 1920, 1080
    img_resize = cv2.resize(img, (width, height))
    crop_img = img_resize[980:1020, 700:1000]
    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    found_text = pytesseract.image_to_string(gray)
    #cv2.imshow("gray", gray)
    t = datetime.datetime.now()
    t = str(t)[:-7]
    complete_text = "You have unclaimed rewards"
    if str(found_text).find(complete_text) != -1:
        print("["+ str(t) + "]" + "did_i_win: True - " + found_text )
        return True
    else:
        print("["+ str(t) + "]" + "did_i_win: False - " + found_text )
        return False





def click_reload():
    time.sleep(2)
    pyautogui.moveTo(240, 180, duration=2, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    time.sleep(2)
    return None

def shuffle_game():
    time.sleep(2)
    pyautogui.moveTo(1700, 1070, duration=2, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    time.sleep(2)
    return None


def click_play():
    time.sleep(2)
    pyautogui.moveTo(1700, 970, duration=2, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    time.sleep(2)
    return None


def fake_play_and_close():
    time.sleep(5)
    for i in range(0, 15):
        pyautogui.moveTo(900, 1370, duration=5, tween=pyautogui.easeInOutQuad)
        pyautogui.click()
        time.sleep(6)
        pyautogui.moveTo(1600, 1370, duration=5, tween=pyautogui.easeInOutQuad)
        pyautogui.click()
        time.sleep(5)
        pyautogui.moveTo(900, 70, duration=5, tween=pyautogui.easeInOutQuad)
        pyautogui.click()
        time.sleep(5)
        pyautogui.moveTo(1600, 70, duration=5, tween=pyautogui.easeInOutQuad)
        pyautogui.click()
        time.sleep(5)
    pyautogui.moveTo(897, 12, duration=2, tween=pyautogui.easeInOutQuad)
    time.sleep(1)
    pyautogui.click()
    time.sleep(5)
    return None



def winclicks():
    time.sleep(5)
    pyautogui.moveTo(1490, 1350, duration=5, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    pyautogui.moveTo(1647, 400, duration=5, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    pyautogui.moveTo(1580, 440, duration=5, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    pyautogui.moveTo(1580, 430, duration=5, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    pyautogui.moveTo(1655, 175, duration=5, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    t = datetime.datetime.now()
    t = str(t)[:-7]
    print("["+ str(t) + "]" + "collecting reward")
    time.sleep(5)
    return None



def apps():
    a = []
    with open('apps.txt', 'r') as f:
        for line in f:
            k = line.strip('\n')
            a.append(k)
        return a


def yes_no():
    k = game_name()
    for i in range(len(apps())):
        if k.find(apps()[i]) != -1:
            return True
            break
    return False


def is_daily_complete():
    screenshot("is_daily_complete")
    img = cv2.imread(r"F:\Documents\Python Scripts\Bluestacks\temp screenshots\is_daily_complete.jpg")
    img = img[0:1440, 0:2560]
    width, height = 1920, 1080
    img_resize = cv2.resize(img, (width, height))
    crop_img = img_resize[600:700, 1200:1600]
    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(gray)
    found_text = pytesseract.image_to_string(invert)
    #cv2.imshow("invert", invert)
    t = datetime.datetime.now()
    t = str(t)[:-7]
    complete_text = "You have completed today"
    if str(found_text).find(complete_text) != -1:
        print("["+ str(t) + "]" + "is_daily_complete: True - " + found_text )
        return True
    else:
        print("["+ str(t) + "]" + "is_daily_complete: False - " + found_text )
        return False



def am_i_on_daily():
    screenshot("am_i_on_daily")
    img = cv2.imread(r"F:\Documents\Python Scripts\Bluestacks\temp screenshots\am_i_on_daily.jpg")
    img = img[0:1440, 0:2560]
    width, height = 1920, 1080
    img_resize = cv2.resize(img, (width, height))
    crop_img = img_resize[50:80, 970:1090]
    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(gray)
    found_text = pytesseract.image_to_string(invert)
    #cv2.imshow("invert", invert)
    t = datetime.datetime.now()
    t = str(t)[:-7]
    complete_text = "GRAND PRIZE"
    if str(found_text).find(complete_text) != -1:
        print("["+ str(t) + "]" + "am_i_on_daily: True - " + found_text )
        return True
    else:
        print("["+ str(t) + "]" + "am_i_on_daily: False - " + found_text )
        return False



def do_daily():
    t = datetime.datetime.now()
    t = str(t)[:-7]
    print("["+ str(t) + "]" + "doing daily")
    time.sleep(5)
    pyautogui.moveTo(1100, 1350, duration=5, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    time.sleep(5)
    if is_daily_complete() == True:
        click_reload()
        return None
    else:
        n = 0
        while True:
            if yes_no() == True:
                click_play()
                time.sleep(10)
                fake_play_and_close()
                time.sleep(10)
                pyautogui.moveTo(1100, 1350, duration=5, tween=pyautogui.easeInOutQuad)
                pyautogui.click()
                pyautogui.moveTo(1900, 1040, duration=5, tween=pyautogui.easeInOutQuad)
                pyautogui.click()
                break
            else:
                n = n + 1
                if n > 15:
                    t = datetime.datetime.now()
                    t = str(t)[:-7]
                    print("["+ str(t) + "]" + "error no new games")
                    time.sleep(60 * 60 * 2)
                    n = 0
                    break
                else:
                    t = datetime.datetime.now()
                    t = str(t)[:-7]
                    print("["+ str(t) + "]" + str(n) + "th " + "shuffle")
                    shuffle_game()
        time.sleep(5)
        return None



def start():
    time.sleep(10)
    n = 0
    while True:
        if is_bluestacks_open() == False:
            break
        while True:
            click_reload()
            if did_i_win() == True:
                winclicks()
                time.sleep(5)
            if is_bihourly_complete() == True:
                t = datetime.datetime.now()
                t = str(t)[:-13]
                t = t[-2:]
                if t == "06":
                    do_daily()
                    time.sleep(60 * 60 * 2)
                else:    
                    time.sleep(next_time_bihourly() + (60 * 5))
                break
            else:
                if yes_no() == True:
                    n = 0
                    click_play()
                    time.sleep(10)
                    fake_play_and_close()
                    time.sleep(10)
                    break
                else:
                    n = n + 1
                    if n > 15:
                        t = datetime.datetime.now()
                        t = str(t)[:-7]
                        print("["+ str(t) + "]" + "error no new games")
                        time.sleep(60 * 60 * 2)
                        n = 0
                        break
                    else:
                        t = datetime.datetime.now()
                        t = str(t)[:-7]
                        print("["+ str(t) + "]" + str(n) + "th " + "shuffle")
                        shuffle_game()
                        break
            
        
    


#img = cv2.imread(r"C:\Users\adamh\Documents\Python Scripts\Bluestacks\temp screenshots\Win1.png")

#width, height = 1280, 720
#img_resize = cv2.resize(img, (width, height))
#crop_img = img_resize[430:480, 760:1050]
#gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
#adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 91, 11)





#text = pytesseract.image_to_string(crop_img)
#print(text)

#cv2.imshow("resized", img_resize)
#cv2.imshow("Cropped", crop_img)
#cv2.imshow("gray", gray)
#cv2.imshow("adaptive", adaptive_threshold)
#cv2.waitKey(0)
