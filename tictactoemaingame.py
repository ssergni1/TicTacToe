##TiC TAC TOE BY TAREK EL-ETER 

#all the modules i needed to import
'''modules i used to import'''
import os 
import time
import random
import sys
import subprocess
import math


new = ['','','','','','','','','']
man = ''
player2 = ''
machine = ''
null = ''

 
def sign(man, machine, player2):
    '''this function asks wither they want to be x or o'''
    man = input("What team do you want to be? X or O ")
    while man not in ('x','X','o','O'):
        print ("Invalid Choice!")
        man = input("What team do you want to be? X or O ")
    if man == 'x' or man == 'X':
        print ("Ok, X is yours!")
        machine = 'o'
    else:
        print ("Ok, O is yours!")
        machine = 'x'
    return man.upper(), machine.upper(), player2.upper()
    
    

def decide_turn():
    '''decides the turn of who will play first'''
    turn = None
    while turn not in ('y','Y','n','N'):
        turn = input("Do you want to play first? ")
        if turn == 'yes' or turn == 'Y':
            return 1
        elif turn == 'no' or turn == 'N':
            return 0
        else:
            print ("thats an invalid choice.")

def draw(a):
    '''This function draws the board a given as input'''
    print ("\t|\t|\t")
    print ("   "+a[0]+"  \t|"+a[1]+"    \t|"+a[2]+"")
    print ("--------|-------|--------")
    print ("   "+a[3]+"  \t|"+a[4]+"    \t|"+a[5]+"")
    print ("--------|-------|--------")
    print ("   "+a[6]+"  \t|"+a[7]+"    \t|"+a[8]+"")
    print ("\t|\t|\t")
    

def congo_man():
    '''prints that the user has won'''
    print ("You have won!!")

def congo_machine():
    '''prints in a fun way that the ai has won'''
    print ("Lol, you lost to a computer!!!")

def man_first(man, machine, new):
    '''function if man is the first to play'''
    while winn(man, machine, new) is None:
        move = man_move(man, new)
        new[int(move)] = man
        draw(new)
        if winn(man, machine, new) != None:
            break
        else:
            pass
        print ("Ok i'll take..")
        p_move = machine_move(man, machine, new)
        new[int(p_move)] = machine
        draw(new)
    q = winn(man, machine, new)
    if q == 1:
        congo_man()
    elif q == 0:
        congo_machine()
    else:
        print ("Its a Tie...")

def machine_first(man, machine, new):
    '''the function for the machine to be first'''
    while not winn(man, machine, new):
        print ("i'll take...")
        p_move = machine_move(man, machine, new)
        new[p_move] = machine
        draw(new)
        if winn(man, machine, new) != None:
            break
        else:
            pass
        move = man_move(man, new)
        new[int(move)] = man
        draw(new)
    q = winn(man, machine, new)
    if q == 1:
        congo_man()
    elif q == 0:
        congo_machine()
    else:
        print ("Its a tie bro...")


def winn(man, machine, new):
    '''shows all possible ways for the user and the machine to win'''
    ways = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in ways:
        if new[i[0]] == new[i[1]] == new[i[2]] != null:
            winner = new[i[0]]
            if winner == man:
                return 1
            elif winner == machine:
                return 0
            if null not in new: 
                return 'TIE'
    if null not in new: 
        return 'TIE'    
    return None


def man_move(man, new):
    '''makes a prompt asking user where do they want to move'''
    a = input("where do you want to move? ")
    while True:
        if a not in ('0','1','2','3','4','5','6','7','8'):
            print ("Sorry, that's a invalid move")
            a = input("where do you want to move? ")
        elif new[int(a)] != null:
            print ("Sorry, that place is already taken")
            a = input("where do you want to move? ")
        else:
            return int(a)

   
def machine_move(man, machine, new):
    '''shows best moves for machine and also its range and how it moves'''
    best = [4, 0, 2, 6, 8]
    blank = []
    for i in range(0,9):
        if new[i] == null:
            blank.append(i)
    
    for i in blank:
        new[i] = machine
        if winn(man, machine, new) is 0:

            return i
        new[i] = null

    for i in blank:
        new[i] = man
        if winn(man, machine, new) is 1:

            return i
        new[i] = null

    return int(blank[random.randrange(len(blank))])


def display_instruction():
    '''loads the games nice background theme'''
    print(" Displays Game Instuructions. ")
    print("""
Welcome to my game...

████████╗██╗ ██████╗    ████████╗ █████╗  ██████╗    ████████╗ ██████╗ ███████╗
╚══██╔══╝██║██╔════╝    ╚══██╔══╝██╔══██╗██╔════╝    ╚══██╔══╝██╔═══██╗██╔════╝
   ██║   ██║██║            ██║   ███████║██║            ██║   ██║   ██║█████╗  
   ██║   ██║██║            ██║   ██╔══██║██║            ██║   ██║   ██║██╔══╝  
   ██║   ██║╚██████╗       ██║   ██║  ██║╚██████╗       ██║   ╚██████╔╝███████╗
   ╚═╝   ╚═╝ ╚═════╝       ╚═╝   ╚═╝  ╚═╝ ╚═════╝       ╚═╝    ╚═════╝ ╚══════╝
   
You will make your move by entering a number, 0 - 8.
These numbers are bound to the board position as illustrated:


0 | 1 | 2
----------
3 | 4 | 5            
----------
6 | 7 | 8

                          
Have Fun
      """)

  
def main(man, machine, new):
    '''displays instructions as well as decided whoose turn it will be after the user has been alrerady asked if he wwants to be first '''
    display_instruction()
    print ("so let the game begin...")
    a = sign(man, machine, player2)
    man = a[0]
    machine = a[1]
    b = decide_turn()
    if b == 1:
        print ("Ok, you are first!")
        print ("Lets get started, here's a new board!")
        draw(new)
        man_first(man, machine, new)
    elif b == 0:
        print ("Ok, I'll be the first to start!")
        print ("So, lets start the game")
        draw(new)
        machine_first(man, machine, new)
    else:
        pass

main(man, machine, new)
input("Press enter to exit")
