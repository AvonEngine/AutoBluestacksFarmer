import pyautogui


def screenshot(name):
    myScreenshot = pyautogui.screenshot()
    return myScreenshot.save(r'F:\Documents\Python Scripts\Bluestacks\temp screenshots\\'+name+'.jpg')
