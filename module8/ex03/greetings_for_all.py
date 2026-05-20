#!/usr/bin/env python3

def greetings(text = "noble stranger") :
    if (isinstance(text, str) == False) :
        print("Error! It was not a name.")
    else :
        print(f"Hello, {text}")


greetings("Rashin")
greetings("Alex")
greetings()
greetings(42)