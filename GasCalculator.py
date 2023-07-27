#Author: DuZii56
#This simple program will give the user a budget to spend on gas with the information given by the user.
#https://github.com/DuZii56/GasCalculator.git

def main():   
    miles_driven = float(input('\nEnter miles driven: '))
    miles_per_gallon = float(input('Enter MPG: '))
    price_of_gas = float(input('Enter the current price of gas: '))          
    print(f'Your total is: ${round(((miles_driven / miles_per_gallon) * price_of_gas), 2)}')

main()
