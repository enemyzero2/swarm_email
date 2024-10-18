import pyautogui
import keyboard
import os
import time
import uuid
from swarm import Agent

def get_picture():
    print("等待快捷键 'Ctrl + i + P' 来截屏...")
    while True:
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('i') and keyboard.is_pressed('p'):
            img_name = f"{uuid.uuid4().hex}.png"
            img_path = os.path.join("./output_picture",img_name)

            if not os.path.exists("./output_picture"):
                os.makedirs("./output_picture")

            screenshot = pyautogui.screenshot()
            print("截屏成功！")
            screenshot.save(img_path)

            return{
               "img_name": img_name,
            }
        time.sleep(0.1)
get_picture.__doc__ = "实时截屏函数，等待快捷键 'Ctrl + i + P' 来截屏，截屏后返回图片名"