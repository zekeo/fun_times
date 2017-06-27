import random
import time

guess = (random.randint(0, 100))

print("I bet I can read your mind. Pick a number up to 100!")
time.sleep(1)
print("I need a little help though: please respond with higher, lower, or correct (or h, l, or c).")
time.sleep(1)
print("do you have your number?")
time.sleep(2)
print(guess)

h = "higher"
l = "lower"
c = "correct"

response = ()
maxguess = int(100)
minguess = int(0)


while response != "correct":
    response = (input("higher, lower or correct?"))
    guess = int(guess)

    if response == "higher":
        if guess > minguess:
            minguess = guess
        guess = int(round(((maxguess-guess)/2)+guess))
        print("I bet your number is %s" % guess)

    elif response == "lower":
        if guess < maxguess:
            maxguess = guess
        guess = int(round(((guess-minguess) / 2)+minguess))
        print("I bet your number is %d" % guess)

    else:
        print("I don't understand, h, l, or c!?!?")

print("I knew I could read your mind!")