numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(numbers)-1, -1, -1):  
    if numbers[i] % 2 != 0:  
        delete = numbers.pop(i)  

print(numbers)
