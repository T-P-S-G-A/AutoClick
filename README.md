# AutoClick


![Python](https://img.shields.io/badge/Python-3.x-blue)


This project implements a simple **auto-clicker** using Python. The auto-clicker can simulate mouse clicks at a specified interval, allowing users to automate repetitive clicking tasks efficiently. It uses the `pyautogui` library for mouse interactions and the `keyboard` library for handling keyboard shortcuts.

## Features
- **Toggle Clicking**: Start and stop the auto-clicking process using keyboard shortcuts.
- **Customizable Keybindings**: Easily change keybindings to suit your preferences.
- **Lightweight & Efficient**: Utilizes threading to minimize resource usage.

## Requirements

Before running this project, ensure you have the following installed:

- Python 3.x
- Required libraries: `pyautogui` and `keyboard`

You can install the required libraries using pip:
   ```bash
   pip install pyautogui keyboard
   ```


## How to use:
### After installing the Program and all necessary libraries:

- Press [Alt + `] to start the Auto Clicker
- Press [Ctrl + `] to Stop the Auto Clicker

### To change keybinds to Start/Stop
- Locate the Keybinds Heading in the code:
   ```
   # Keybinds
   kb.add_hotkey("alt+`", start) #Start Clicker
   kb.add_hotkey("ctrl+`", exit) #Exit Clicker
   
- Change the keybinds to your preferences
- <Optional> If you want a combination of keys, add '+' with each key like the original code mentioned here:
```
kb.add_hotkey("alt+`", start)
