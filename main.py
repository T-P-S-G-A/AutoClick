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
        
def start():
    global click
    click = True
    print("Clicker enabled")


def exit():
    global click
    click = False
    print("Stopping...")

    
click_thread = threading.Thread(target=clicker)
click_thread.daemon = True
click_thread.start()

# Keybinds
kb.add_hotkey("alt+`", start) #Start Clicker
kb.add_hotkey("ctrl+`", exit) #Exit Clicker

print("Press [alt + `] to enable clicker\n Press [ctrl + ` ] to exit")
kb.wait()
