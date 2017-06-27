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

response = ()
maxguess = (100)
minguess = (0)


while response not in ["correct", "c"]:
    response = (input("higher, lower or correct? \n:"))
    guess = int(guess)

    if ((guess == 100) or (guess == 0)):
        print("You're a dirty rotten liar")
        break

    else:
        if (maxguess-minguess) >= 2:
            if response in ["higher", "h"]:
                if guess > minguess:
                    minguess = guess
                guess = int(round(((maxguess-guess)/2)+guess))
                print("I bet your number is %s" % guess)

            elif response in ["lower", "l"]:
                if guess < maxguess:
                    maxguess = guess
                guess = int(round(((guess-minguess) / 2)+minguess))
                print("I bet your number is %d" % guess)

            else:
                print("I don't understand, h, l, or c!?!?")

        else:
            print("oh I see you don't like intergers. Fine.")
            time.sleep(1)
            print("no more than one decimal though ok?")
            time.sleep(1)

            while response not in ["correct", "c"]:
                response = (input("higher, lower or correct? \n:"))
                guess = int(guess)

                if minguess == maxguess:
                    maxguess = (maxguess + .5)

                if response in ["higher", "h"]:
                    if guess > minguess:
                        minguess = int(guess)
                        guess = int(guess)
                    guess = (round((((maxguess-guess)/2)+guess), 2))
                    print("I bet your number is %s" % guess)

                elif response in ["lower", "l"]:
                    if guess < maxguess:
                        maxguess = int(guess)
                    guess = (round((((guess-minguess) / 2)+minguess), 2))
                    print("I bet your number is %d" % guess)

                else:
                    print("I don't understand, h, l, or c!?!?")



print("I knew I could read your mind!")