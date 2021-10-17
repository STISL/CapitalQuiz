#AUTHOR: F. RUSTIQUE, JR. FOR STISL 
#This version uses a dictionary containing
#key:value pairs of states and their capitals
#Date: 06Sep2021

#import choice method from random module to randomly pick questions:
from random import choice
#import os to use clearConsole method:
import os

#clearConsole clears screen output
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

#create dictionary of states with capitals:
dic_stateCap = {'Alabama':'Montgomery','Alaska':'Juneau','Arizona':'Phoenix',
'Arkansas':'Little Rock','California':'Sacramento','Colorado':'Denver',
'Connecticut':'Hartford','Deleware':'Dover','Florida':'Tallahassee',
'Georgia':'Atlanta','Hawaii':'Honolulu','Idaho':'Boise','Illinois':'Springfield',
'Indiana':'Indianapolis','Iowa':'Des Moines','Kansas':'Topeka','Kentucky':'Frankfort',
'Louisiana':'Baton Rouge','Maine':'Augusta','Maryland':'Annapolis','Massachusetts':'Boston',
'Michigan':'Lansing','Minnesota':'Saint Paul','Mississippi':'Jackson','Missouri':'Jefferson City',
'Montana':'Helena','Nebraska':'Lincoln','Nevada':'Carson City','New Hampshire':'Concord',
'New Jersey':'Trenton','New Mexico':'Santa Fe','New York':'Albany','North Carolina':'Raleigh',
'North Dakota':'Bismarck','Ohio':'Columbus','Oklahoma':'Oklahoma City','Oregon':'Salem',
'Pennsylvania':'Harrisburg','Rhode Island':'Providence','South Carolina':'Columbia',
'South Dakota':'Pierre','Tennessee':'Nashville','Texas':'Austin','Utah':'Salt Lake City',
'Vermont':'Montpelier','Virginia':'Richmond','Washington':'Olympia','West Virginia':'Charleston',
'Wisconsin':'Madison','Wyoming':'Cheyenne'}

#create empty dictionary that populates from missed state capitals:
dic_missedStateCap = {}

#define review function for missed capitals:
def review(numberRight):
    clearConsole()
    #review the missed state capitals 15 times using a while loop and counter:
    counter = 15
    while counter > 0:
        stateKey = choice(list(dic_missedStateCap))
        correctAnswer = dic_missedStateCap[stateKey]
        #capitalQuestion = print(f"\nWhat is the capital of {stateKey}? ")
        userAnswer = str(input(f"\nWhat is the capital of {stateKey}? "))
        clearConsole()
        if (userAnswer.lower() == correctAnswer.lower()):
            print("""Correct! :)""")
            counter -= 1
            continue
        else:
            print(f"\nThat is incorrect. The capital of {stateKey} is {correctAnswer}.")
            counter -= 1
            continue
    else:
        print(f"\nYou have reviewed the last 3 capitals you missed 15 times altogether.")
        print("You will now continue on with the other capitals.")
        dic_missedStateCap.clear()
        askCapitalQuestion(numberRight)

#if user names all 50 capitals:
def congratulate():
    clearConsole()
    print(f"Congratulations! You just named all 50 capitals!\n")
    print("Do you want to go again?")
    response = str(input("Enter 'y' for yes, or 'q' to quit: ").lower())
    try:
        if (response == 'y'):
            numberRight = 0
            askCapitalQuestion(numberRight)
        elif (response == 'q'):
            print(f"\nOkay. Good-bye.\n")
            quit()
    except Exception as e:
        print(e)

#define askCapitalQuestion function:
def askCapitalQuestion(numberRight):
    #randomly select and assign to stateKey variable an item from dic_stateCap
    #that has to convert into a list first:
    stateKey = choice(list(dic_stateCap))
    correctAnswer = dic_stateCap[stateKey]
    print(f"\nWhat is the capital of {stateKey}?")
    userAnswer = str(input())
    if (userAnswer.lower() == correctAnswer.lower()):
        numberRight += 1
        if (numberRight == 50):
            congratulate()
        else:
            clearConsole()
            print("""Correct! :)""")
            print(f"You've named {numberRight} state capitals correctly!")
            #Remove correctly answered key from dict_StateCap so state isn't asked again while user is not messing up:
            dic_stateCap.pop(stateKey)
            askCapitalQuestion(numberRight)
    else:
        #numberWrong += 1
        #add the missed state & capital to the "missed" dictionary:
        dic_missedStateCap[stateKey] = correctAnswer
        #display correct answer:
        clearConsole()
        print(f"\nThat is incorrect. The capital of {stateKey} is {correctAnswer}.")
        #give user option to review last 3 missed capitals when "missed" dictionary has 3 key value pairs:
        #if (numberWrong == 3):
        if (len(dic_missedStateCap) == 3):
            print(f"\nYou've missed 3 different capitals.")
            while True:
                try:
                    ask2review = str(input(f"\nDo you want to go over the 3 you've most recently missed?\nEnter 'y' for yes or 'n' for no to keep going.\nOr, if your brain's had enough, enter 'q' to quit: "))
                    if(ask2review == 'y'):
                        clearConsole()
                        review(numberRight)
                    elif(ask2review == 'n'):
                        dic_missedStateCap.clear()
                        clearConsole()
                        askCapitalQuestion(numberRight)
                    elif(ask2review == 'q'):
                        clearConsole()
                        print(f"\nLooks like you don't want to think. Bye.\n")
                        quit()
                    clearConsole()
                    print(f"\nInvalid entry. Try again.")
                except Exception as e:
                    print(e)
        askCapitalQuestion(numberRight)

#define begin function:
def begin(numberRight):
    clearConsole()
    print(f"\nThis is a challenge.\nCan you name the 50 capitals of every U.S. state?\n*Cities must be spelled out with correct capitalization.\n")
    while True:
        try:
            startGame = str(input(f"Enter 'y' to try or 'q' to quit: ")).lower()
            if(startGame == 'q'):
                print(f"\nOkay. Good-bye.\n")
                quit()
            elif(startGame == 'y'):
                clearConsole()     
                #pass numberRight and run askCapitalQuestion:
                askCapitalQuestion(numberRight)
            print(f"\nInvalid entry. Try again.")
        except Exception as e:
            print(e)

#begin function starts program.
#numberRight parameter begins with argument value of 0 to begin game:
begin(numberRight=0)