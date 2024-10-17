import keyboard as kb
import time as t
import pyautogui as mouse
import threading

click = False

def clicker():
    while True:
        if click:
            mouse.click()
        t.sleep(0.01) #Time in seconds (0.01s = 10ms)
        
def toggle():
    global click
    click = not click
    if click:
        print("Clicker enabled")
    else:
        print("Clicker disabled")

def exit():
    global click
    click = False
    print("Exiting...")

    
click_thread = threading.Thread(target=clicker)
click_thread.daemon = True
click_thread.start()

kb.add_hotkey("left alt+`", toggle)
kb.add_hotkey("left ctrl+`", exit)

print("Press [left alt+`] to enable/disable clicker\n Press [left ctrl + ` ] to exit")
kb.wait()
