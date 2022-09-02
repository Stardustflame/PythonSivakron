N = int(input('Enter Your Loop : '))
Total = []
print("Enter Your Data : ")
for i in range(N):
    data = int(input(' '))
    Total += [data]
print(Total,end=' ')
N.sort()
print(" ---> ",end=' ')
print(Total)
print("Min -> ",Total[0])
print("Max -> ",Total[-1])