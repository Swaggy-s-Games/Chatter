import keyboard as kb
import time
import json

print()
print()
print("Press 1-2-3-4 to type them!")

kw1 = open("Keywords\Keyword1.txt", "r")
k1 = kw1.readlines()

kw2 = open("Keywords\Keyword2.txt", "r")
k2 = kw2.readlines()

kw3 = open("Keywords\Keyword3.txt", "r")
k3 = kw3.readlines()

kw4 = open("Keywords\Keyword4.txt", "r")
k4 = kw4.readlines()

running = True
while running:
    
    if kb.read_key() == "1":
        kb.press_and_release("t")
        time.sleep(0.3)
        kb.write(k1)
        time.sleep(0.3)
        kb.press_and_release("Enter")
        time.sleep(1)
    
    if kb.read_key() == "2":
        kb.press_and_release("t")
        time.sleep(0.3)
        kb.write(k2)
        time.sleep(0.3)
        kb.press_and_release("Enter")
        time.sleep(1)
    
    if kb.read_key() == "3":
        kb.press_and_release("t")
        time.sleep(0.3)
        kb.write(k3)
        time.sleep(0.3)
        kb.press_and_release("Enter")
        time.sleep(1)
    
    if kb.read_key() == "4":
        kb.press_and_release("t")
        time.sleep(0.3)
        kb.write(k4)
        time.sleep(0.3)
        kb.press_and_release("Enter")
        time.sleep(1)
