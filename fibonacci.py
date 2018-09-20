#CMPT 120L 113
#Fibonacci Program
#Author: Timothy Schindler
#Created: 9/20/18

n = int(input("Which Fibonacci number do you want to see?: "))
fNum = 0
sNum = 1
hNum = 0

def fibonacci():
    global fNum, sNum, hNum
    for x in range(0,n):
        print(str(sNum) + ", ")
        hNum = sNum
        sNum = sNum + fNum
        fNum = hNum
    
fibonacci()
