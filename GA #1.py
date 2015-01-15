#Kris Kenney
#kenneyk@onid.orst.edu
#CS325
#Assignment #1

import random
import time

#Enumeration
def alg1(arr):
    sum1 = arr[0]
    count = 0

    for j in range (0,len(arr)):
        for i in range(0,len(arr)):
            #print(j,i)
            sum2 = 0
            for k in range(i,j+1):
                sum2 = sum2 + arr[k]
                count = count + 1
                if sum2 > sum1:
                    sum1 = sum2

    #print(sum1,count)

#Better Enumeration
def alg2(arr):
    sum1 = arr[0]
    count = 0

    for j in range (0,len(arr)):
        sum2 = 0
        for i in range (j,len(arr)):
            #print(j,i)
            sum2 = sum2+ arr[i]
            count = count + 1
            if sum2 > sum1:
                sum1 = sum2

    print(sum1,count)

#Dynamic Programming
def alg3(arr):
    max1 = max2 = arr[0]
    count = 0
    
    for x in range(1,len(arr)):
        max1 = max(arr[x], max1 + arr[x])
        max2 = max(max2, max1)
        count = count + 1
        
    print(max2, count)

#main function
def main():
    #a = [random.randint(-100,100) for _ in range (100)]
    #alg1(a)
    #alg2(a)
    #alg3(a)

    spare = [0,0,0,0,0,0,0,0,0,0]

    for j in range(1,9):
        for i in range(0,10):
            a = [random.randint(-100,100) for _ in range (j*100)]
            spare[i] = time.time()
            alg1(a)
            spare[i] = time.time() - spare[i]
        print(j*100,sum(spare)/10)

#program
main()

