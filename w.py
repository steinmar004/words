import random
print("\t\tWitaj w grze'Wymieszane litery'")
print()
#dost = input("Wartość zmiennej indeks to:")
print("\tUporządkuj litery aby odtworzyć nowe słowo.\nZgadnij jakie to słowo: wyświetlę 10_krotnie wylosowane litery z oznaczonymi pozycjami:")
dost = "ksero"
low = - len(dost)
high = len(dost)
for p in range(10):
    position = random.randrange(low,high)
    print("")

kom = input("Wprowadź komunikat")
w = ""
VOV = "aąeęioóuy" 

for l in kom:
    if l.lower() not in VOV:
        w += l
        print(f"Został utworzony nowy łańcuch:{w}")
print(f"Twoj komunikat bez samogłosek to:{w}")
