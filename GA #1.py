#Kris Kenney
#kenneyk@onid.orst.edu
#CS325
#Assignment #1

#Enumeration
def alg1(arr):
    sum1 = arr[0]
    count = 0

    for j in range (0,len(arr)):
        for i in range(0,len(arr)):
            #print(j,i)
            sum2 = 0
            for k in range(i,j):
                sum2 = sum2 + arr[k]
                count = count + 1
                if sum2 > sum1:
                    sum1 = sum2

    print(sum1,count)

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
        print (x)
        
    print(max2, count)

#main function
def main():
    a = [31,-41,59,26,-53,58,97,-93,-23,84]
    alg1(a)
    alg2(a)
    alg3(a)

#program
main()
