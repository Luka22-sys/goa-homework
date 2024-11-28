num_words = int(input("რამდენი სიტყვა გინდა შეიყვანო? "))

words = []

for i in range(num_words):
    word = input(f"მიუთითე {i+1}-ე სიტყვა: ")
    words.append(word)

joined_words = " ".join(words)

print("შეყრილი სიტყვები:", joined_words)