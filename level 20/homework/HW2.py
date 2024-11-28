numbers = [5, 3]

for i in range(1, 101):
    if i % 5 == 0 or i % 3 == 0:
        numbers.append(i)

print("5-ის და 3-ის ჯერადები:", numbers)