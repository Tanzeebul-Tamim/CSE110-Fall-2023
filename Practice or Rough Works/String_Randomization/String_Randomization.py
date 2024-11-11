import string
import random
import time

letters = string.ascii_letters
result = ""
user_input = input("Please enter your name: ")
# user_input = "Code, Create, Conquer - 'Tanzeebul Tamim'"

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
    time.sleep(0.003)