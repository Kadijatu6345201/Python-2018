import random
import time

response = ["Surprisingly enough, I feel like The chances of this happening are a reasonable 90%", "The chances of this happening are lower then the chances of a single person counting to infinity","It's a fair bet,but like don't count on it.", "I don't Think so, but really you never know."]
name = input("Welcome to hell my loyal subject. State your name : ")

print ("Okay, " + name + ", here's what's gonna happen. your gonna ask me some questions, and I'm gonna give a reasonably vague response that only partially answers your question. Whenever you want to stop asking questions, simply type, 'I wish to go back to the mortal realm,' and I'll stop asking for your next question. Understood? good.")

user_question = input("What's your question: ")

if user_question == "I wish to go back to the mortal realm":
        break
    else:
        print (random.shuffle(response)) 
 
