#Author: DuZii56
#This simple program will add up the total amount of entries a user inputs for their trips and gives a budget to spend on gas.
#https://github.com/DuZii56/GasCalculator.git

from os import system, name

#This will only work for a Linux machine.  Find proper code to run on a Windows machine.
def clear():
    _ = system('clear')
clear()

Allowence = []

def main():
    entries = 0
    quit = False
    
    answer = input('Press <enter> to continue')
   
    clear()
    while (not quit):
        print ('Number of entries: ', (entries))
        #Find a better way to clean this up.
        MD = float(input('\nEnter miles driven: '))
        MPG = float(input('Enter MPG: '))
        PoG = float(input('Enter the current price of gas: '))          

        budget = round(((MD / MPG) * PoG), 2)
        Allowence.append (budget)
        
        entries = entries + 1
        answer = input('\nContinue? Y/n ')
        if answer == 'n':
            Total = sum(Allowence)
            print ('\nTotal entires: ', (entries))
            print ('Your total is: $', (Total))
            quit = True
    
main()
input('\nPress <enter> to exit')
