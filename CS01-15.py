Num = int(input('Enter Your Loop : '))
NumTotal = []
for i in range(Num):
    data = int(input('Enter your data : '))
    NumTotal += [data]
    print(NumTotal)
    NumTotal.sort()
    print(NumTotal)