vowels = ['ა', 'ე', 'ი', 'ო', 'უ', 'ჲ', 'ა' , 'ე']

text = "გამარჯობა, როგორ ხარ?"

vowel_count = 0

for letter in text:
    if letter in vowels:
        vowel_count += 1

print(f"ხმოვნების რაოდენობა: {vowel_count}")