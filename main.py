from win10toast_click import ToastNotifier
from pyscreeze import PyScreezeException
import datetime, time, os, pyautogui
from tkinter import PhotoImage
import tkinter as tk

logo_location = os.path.join(os.path.dirname(__file__), 'logo.png')
logo_location_ico = os.path.join(os.path.dirname(__file__), 'logo.ico')
toaster = ToastNotifier()

root = tk.Tk()
logo = PhotoImage(file = logo_location)
root.iconphoto(False, logo)
root.title('Screenshot')
canvas = tk.Canvas(root, width = 300, height = 300)
canvas.pack()

def displayImage(imagePth):
    os.startfile(imagePth)

def take_screenshots():
    root.iconify()
    # print('\a')
    # print('\a')
    time.sleep(0.3)
    myScreenShots = pyautogui.screenshot()
    part_first = str(datetime.datetime.now()).replace(' ', '').replace(':', '').replace('-', '').split('.')[0]
    if not os.path.exists("Screenshots"):
        os.mkdir("Screenshots")
    filePth = os.path.join("Screenshots", part_first+'.png')
    try:
        myScreenShots.save(filePth)
    except PyScreezeException:
        os.system("pip install --upgrade pip&&pip install --upgrade Pillow")
        toaster.show_toast(
            title="Error Occured",
            msg="Sorry, Some requirements were not satisfied\nNow Packages has been installed successfully\nPlease RESTART the application",
            icon_path=logo_location_ico,
        )
        exit(1)
    toaster.show_toast(
        title="Screenshot",
        msg="Screenshot has been saved\n\n{}".format(filePth),
        icon_path=logo_location_ico,
        callback_on_click=lambda: displayImage(filePth)
        )
myButton = tk.Button(text='Take Screenshot', command=take_screenshots, font=10)
canvas.create_window(150, 150, window = myButton)
root.mainloop()