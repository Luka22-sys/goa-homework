age = int(input("რამდენი წლის ხარ? "))

if age < 18:
    status = "გახდი ბავშვი"
elif 18 <= age < 60:
    status = "გახდი ზრდასრული"
else:
    status = "გახდი ასაკოვანი"
print("თქვენი სტატუსი არის:", status)