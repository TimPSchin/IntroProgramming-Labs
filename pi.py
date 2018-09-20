#CMPT 120L 113
#Pi Program
#Author: Timothy Schindler
#Created: 9/20/18
import math
n = int(input("How many terms to sum do you want?: "))
den = 1
pi = 0

for x in range(0,n):
    if x == 0:
        pi += (4/den)
    elif (x % 2) != 0:
        pi -= (4/den)
    else:
        pi += (4/den)

    den += 2

dif = math.pi - pi
print("The answer is " + str(pi) + ".")
print("The defernce between the asnwer and pi is " + str(dif) + ".")


