"""
Find PI to the Nth Digit - Enter a number and have the program generate PI up to that many decimal places. 
Keep a limit to how far the program will go.
"""

from decimal import Decimal, getcontext
num_digits = int(input("Enter the number of digits of PI that you would like to generate: "))
getcontext().prec = num_digits

# Formula for PI using the BBP Formula
print (sum(1/Decimal(16)**k * (
		Decimal(4)/(8*k+1) - 
		Decimal(2)/(8*k+4) - 
		Decimal(1)/(8*k+5) - 
		Decimal(1)/(8*k+6)) for k in range(num_digits)))
		
input("Press enter to exit")