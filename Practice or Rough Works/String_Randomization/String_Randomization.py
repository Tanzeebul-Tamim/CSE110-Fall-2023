import string
import random
import time

letters = string.ascii_letters
result = ""

file = open('./text.txt', 'r', encoding='utf-8')
# user_input = input("Enter your name: ")
user_input = file.read()

for letter in user_input:
    while True:
        i = random.choice(letters)
        print(result + i)
        if letter == i:
            result += i
            break
        elif letter in (" ", "-", ",", "'"):
            result += letter
            break

        time.sleep(0.005)

for i in range (0 , 60):
    print(user_input)
    time.sleep(0.005)