new_arr = [1, 23, 3, 4, 5, 56, 6, 6, 6, 7, 7, 78, 2, 342, 3423, 4234212, 1, 312, 31, 341]

new_arr[0] = "დავითი"

for i in range(len(new_arr)):
    if isinstance(new_arr[i], int):  
        if new_arr[i] % 2 != 0:  
            new_arr[i] = "კენტი"

print('----------------------------------------------')
for item in new_arr:
    print(item)