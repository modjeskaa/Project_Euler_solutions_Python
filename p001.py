numbers = []

for i in range(1,1000):
    if i % 3 ==0 or i % 5 ==0:
        numbers.append(i)

suma = sum(numbers)
print(numbers)
print(suma)

#Answer: 233168
