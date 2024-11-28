def custom_join(list_of_strings, delimiter=""):
    result = "" 
    for string in list_of_strings:
        result += string 
    return result

list_of_strings = ['დ', 'ა', 'ვ', 'ი', 'თ']
joined_text = custom_join(list_of_strings)

print(joined_text)