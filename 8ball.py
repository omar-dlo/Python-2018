print("Hello, user! Welcome to Magic 8-ball.")

import time

import random

time.sleep(1)
name=input("What is your name?")
play=input("Would you like to play?(Type 1 for yes, 2 for no.)")
answers = ["This is true,", "I can't answer this,", "You thought the answer was yes? Wrong again,", "Obviously not,","That's not a very smart question. But yes,","Your mom. Just kidding! The answer would be no," , "Yeah... umm.. no," ]
name = name.title()
name = name.strip()
play = play.strip()

if play == "1":
        while True:
                question = input("Please ask a question.")
                time.sleep(2)
                print("The magic 8-ball is shaking...")
                time.sleep(2)
                new_answer = random.choice(answers)
                print("%s" %new_answer, name)
                play2=input("Would you like to continue,%s?(Yes or No)" %name)
                play2 = play2.title()
                play2 = play2.strip()
                if play2 == "Yes":
                        continue
                else:
                        print("Goodbye!")
                        time.sleep(2)
                        break

elif play == "2":
        print("Goodbye!")
        time.sleep(2)



    
