import pyperclip
from pynput.keyboard import Controller,Listener,Key
import time

def paste():
    time.sleep(0.2)
    #按下后间隔0.2s
    i=pyperclip.paste()
    keyboard = Controller()
    keyboard.type(i)
    print("粘贴成功"+"\n"+i+"\n")

def on_release(key):
    if key == Key.esc:
        # 停止监听
        return False
    if key == Key.f2:
        paste()
        # 这里是按f2调用粘贴函数

with Listener(
        on_release=on_release) as listener:
    listener.join()
