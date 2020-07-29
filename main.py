#jvadair's hangman program v0.238 ßeta
#Based on code found in "Invent Your Own Computer Games with Python"
#Citation given voluntarily
#Code completely retyped and redone, no copy and paste other than the HANGMAN_PICS variable.
#Find me on reddit! u/jvadair
#This is a private version given to friends and family, and is freely redistributable if credit is given.
#Yes I actually took the time to learn whate the code means
#Yes I REALLY DID REWRITE MOST OF IT, AND I ADDED LOTS OF UNIQUE CODE
#Most variable names are my own.
#Styled uniquely to my liking
#Wow you're still reading this?
#Oh and also all the comments are mine
#In case you couldn't tell
import random
import time
import os
from jvalib_asciidb import *
#first we have the first-run detection and setup
createfile = open("config.hgm", "a")
createfile.close
if open("config.hgm", "r").read() == '':
    fst = open("config.hgm", "w")
    fst.write('0\n')
    fst.write('banana apple peach coconut blackberry pineapple rasberry tomato lettuce pickle cucumber spinach kitten puppy kale apricot finch quake establish preliminary creation corruption perfection polymer versatile extravagant cancer texas california ohio michigan oregon kansas idaho iowa kentucky washington vigrinia vermont apprehensive insightful turkey bonanza scribble tactful vase infectious jeopardy lampshade hunter leather cruise piano aquamarine fungus toenail blimp bookshelf sunset sunrise railroad train automobile lavender woodwork brass symbiotic fern reunk lavish hammer thumbnail curtain compact candle blanket watermelon snail covenant haircut annoying obnoxious pest vile partition')
    fst.close()
#below is the pictures of 'hangman' that the player will see
HANGMAN_PICS = callascii('HANGMAN_PICS', 'NA')
print("Loading 7%")
#these are all the words that the program can generate
wordlist = open('config.hgm', 'r').readlines()[1].split(' ')
#begin functions, these will be called up later
#the function below picks the random word
def getrandom(wlist):
    pick = random.randint(0, len(wlist) -1)
    return wlist[pick]
secret = getrandom(wordlist)
print("Loading 12%")
#the function below creates the "UI"
def display(m, c, s):
    clear()
#below pulls up the hangman picture
    print(HANGMAN_PICS[len(m)])
    print()
#below we spell out the missed letters, adding a space in between
    print('Missed letters:', end=' ')
    for letter in m:
        print(letter, end=' ')
    print()
    print("_________________________")
    print()
#then we set the variable to a number of underscores the same length as the secret word 
    blanks = '_' * len(s)
#after that the code below replaces underscores with any letters that have been guessed correctly, similar to Vannah White
    for i in range(len(s)):
        if s[i] in c:
            blanks = blanks[:i] + s[i] + blanks[i+1:]
#then this bit down here just puts a space in between the mystery letters
    for letter in blanks:
        print(letter, end=" ")
    print()
    print("_________________________")
    print()
#now we move down to this function, which basically the user inputs exactly one letter - no special characters, numbers, or anything longer than 1 character.
print("Loading 45%")
def inputguess(alrg):
    while True:
        guess = input('Pick a letter >>> ').lower()
        if len(guess) != 1:
            print('You can only type a single letter, try again:')
        elif guess in alrg:
            print('That letter has already been guessed, try again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter only a letter, no numbers/special characters.')
        else:
            return guess
#this is pretty simple, it just asks if you want to play again or not, and then returns true if yes, false if otherwise. UPDATE: Also lumped custom word functionallity into here as well.
print("Loading 51%")
def askContinue():
    while True:
        print()
        y = input('Do you want to play again? You can also type \'c\' to add custom words. >>> ').lower()
        x = y.startswith('y')
        if x is True:
            return True
        elif x is False:
            if y.startswith('n'):
                return False
            elif y.startswith('c'):
                cval()
            else:
                print("Please enter a value that starts with 'y', 'n' or 'c'")

def cval():
    while True:
        clear()
        if customword(input('Which word would you ike to add? >>> ')):
            while True:
                aa = input('Word added successfully. Would you like to add another? >>> ')
                bb = aa.startswith('y')
                if bb is True:
                    break
                elif bb is False and aa.startswith('n'):
                    return
                else:
                    print("Please enter a value that starts with 'y' or 'n'")
        else:
            if cause == 'lenshort':
                print('Custom words must be at least 3 letters in length.')
            else:
                print('Please only use letters.')
            time.sleep(1)
#this will let the user add custom words to the list
def customword(x):
    x = list(map(str, x))
    if len(x) < 3:
        global cause
        cause = 'lenshort'
        return False
    for i in range(0, len(x)):
        if x[i] not in 'abcdefghijklmnopqrstuvwxyz':
            return False
    x = backtostring(x)
    file = open('config.hgm', 'r')
    file = file.readlines()
    wfile = open('config.hgm', 'w')
    wfile.write(file[0])
    wfile.write(file[1] + ' ' + x)
    wfile.close()
    return True
def backtostring(x):
    out = ''
    x = str(x)
    x = x[1:len(x) - 1]
    for i in range(0, (len(x) + 2) // 5):
        x = x[1:]
        out = out + x[0]
        if len(x) > 2:
            x = x[4:]
        else:
            x = x[:1]
            return out
def checktotalplays():
    file = open('config.hgm', 'r')
    return str(int(file.readlines()[0]))
#Thanks StackExchange \/ \/
print("Loading 53%")
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
print("Loading 62%")
time.sleep(0.3)
#Wwhat players see when they boot up the game (or restart):
def openingSequence():
    clear()
    global missed
    global correct
    global secret
    global gamedone
    missed = ''
    correct = ''
    secret = getrandom(wordlist)
    gamedone = False
    print(callascii('logotext', 'NA'))
    time.sleep(1)
    print("Presents...")
    time.sleep(3)
    print(callascii('hangmantext', 'v1.01 ℝelease'))
    time.sleep(2)
    clear()
#what players see when they win
print("Loading 69%")
def victorySequence(m, t):
    clear()
    for h in range(0, 3):
        print(callascii('youwintext', 'NA'))
        time.sleep(0.5)
        clear()
        time.sleep(0.5)
    print()
    time.sleep(0.2)
    print("You beat the game with " + str(m) + " false guesses, and " + str(t) + " total guesses!")
    print(checktotalplays() + ' total plays!')
print("Loading 74%")
#the game over screen
def gameOver(m, c, s):
   print(callascii('deadface', 'NA'))
   print()
   print()
   print(callascii('gameovertext', 'NA'))
   print()
   print()
   print("You lose. You made " + str(len(m)) + " false guesses, and " + str(len(c)) + " correct guesses. The secret word was " + s + ".")
   print(checktotalplays() + ' total plays!')
print("Loading 100%")
openingSequence()
#and now we begin the main game loop
while True:
    display(missed, correct, secret)
    guess = inputguess(missed + correct)
#below checks if the guess is in the secret word, then it sees if the player has guessed all of the letters in the secret word.
    if guess in secret:
        correct = correct + guess
        foundAll = True
        for i in range(len(secret)):
            if secret[i] not in correct:
                foundAll = False
                break
        if foundAll:
            display(missed, correct, secret)
            time.sleep(2)
            victorySequence(len(missed), len(missed + correct))
            gamedone = True
#if the letter wasn't in the secret word, the code notes it and then checks to see if the player has run out of guesses.
    else:
        missed = missed + guess
    if len(missed) == len(HANGMAN_PICS) - 1:
        display(missed, correct, secret)
        time.sleep(1)
        clear()
        time.sleep(.5)
        display(missed, correct, secret)
        time.sleep(.5)
        clear()
        time.sleep(1)
        gameOver(missed, correct, secret)
        gamedone = True
    if gamedone:
#Increases the number of played times by 1
        ipt = open('config.hgm', 'r')
        ipt = ipt.readlines()
        wrt = open('config.hgm', 'w')
        wrt.write(str(int(ipt[0]) + 1) + '\n')
        wrt.write(ipt[1])
        wrt.close()
#Breaks the loop if the player doesn't want to play again. If the player does want to continue, it plays the opening sequence and then goes back to the start of the loop.
        if askContinue():
            openingSequence()
        else:
            break
#The kill command
exit()
