import pyperclip
import time
import pyautogui

# 读取txt文件
time.sleep(1)
with open('1.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    #print(text)

# 逐句复制粘贴
for line in text.split('\n'):
    pyperclip.copy(line.strip())

    # 粘贴内容
    pyautogui.hotkey('ctrl', 'v')
    #time.sleep(0.5)  
    pyautogui.press('enter')
    #time.sleep(0.5)  # 
