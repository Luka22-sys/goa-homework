def custom_split(string):
    result = []  
    for char in string:
        result.append(char)  
    return result

text = "დავით"
split_text = custom_split(text)

print(split_text)