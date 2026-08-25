from array import array
färger = ["Blå", "Röd", "Lila"]
print(färger)
lägga_till = input("Vilken färg vill du lägga till i listan: ")
färger.append(lägga_till)
print(färger)

ny_färg = input("Välj en annan färg: ")
plats = int(input("Var vill du sätta in färgen? ange plats nummer: "))
färger.insert(plats, ny_färg)
print(färger)

bort = input("Från denna listan, vilken färg vill du ta bort? : ")

for i in färger:
    if bort == i:
        färger.remove(bort)

print(färger)

position_bort = int(input("Ge plats nummer till färg som du vill ta bort: "))
färger.pop(position_bort)
print(färger)
