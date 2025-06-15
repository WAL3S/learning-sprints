#sum of 1 to n

n = int(input('Enter a value for N: '))

total = 0

for i in range(1,n+1):
    total = i + total
    
print(total)