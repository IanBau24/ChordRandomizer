import random
import time

notes = ("C","C#","D","D#","E","F","F#","G","G#","A","A#","B")

# ask user which key to build
def getKeyStart():
    keyStart = input("Enter key (C,D,E,F,G,A,B): ")
    match keyStart.lower():
        case "c":
            return 0
        case "d":
            return 2
        case "e":
            return 4
        case "f":
            return 5
        case "g":
            return 7
        case "a":
            return 9
        case "b":
            return 11
        case _:
            return 1


# writing our own steps allows us to traverse the list at the intervals we want
steps = [2,2,1,2,2,2,1]

# creates a list and fills it with the notes corresponding to the key
key = []
i = getKeyStart() # our actual index starting at the key we chose
for step in steps: # traverse steps
    key.append(notes[i%12]) # using mod length allows us to loop around the list if needed
    i += step

# traverse list once again and append chord quality to each element
chordQuality = ["","m","m","","","m","dim"]
for i in range(len(key)):
    key[i] += chordQuality[i]


time.sleep(1)
print("Key is:", key)
time.sleep(1)
print("Randomizing chords...")
time.sleep(2.5)
print("Your random chords for today are:",random.sample(key, k = 4))



