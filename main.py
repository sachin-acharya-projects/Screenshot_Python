import tkinter as tk
from tkinter import PhotoImage
from tkinter import filedialog
import datetime, time, os, pyautogui
logo_location = os.path.join(os.path.dirname(__file__), 'logo.png')

root = tk.Tk()
logo = PhotoImage(file = logo_location)
root.iconphoto(False, logo)
root.title('Screenshot')
canvas = tk.Canvas(root, width = 300, height = 300)
canvas.pack()

def take_screenshots():
    root.iconify()
    print('\a')
    print('\a')
    time.sleep(0.3)
    myScreenShots = pyautogui.screenshot()
    part_first = str(datetime.datetime.now()).replace(' ', '').replace(':', '').replace('-', '').split('.')[0]
    myScreenShots.save(part_first+'.png')
myButton = tk.Button(text='Take Screenshot', command=take_screenshots, font=10)
canvas.create_window(150, 150, window = myButton)
root.mainloop()
