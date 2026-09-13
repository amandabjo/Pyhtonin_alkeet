luoti=13.3

leiviskat=float(input("leiviskat:"))
naulat=float(input("naulat:"))
luodit=float(input("luodit:"))

print("massa grammoina:",leiviskat*naulat*(luodit*luoti), "grammaa")
print(f"{leiviskat*naulat*(luodit*luoti):.2f} grammaa")

print("massa kilogrammoina:", leiviskat*naulat*(luodit*luoti)/1000, "kilogrammaa")
print(f"{leiviskat*naulat*(luodit*luoti)/1000:.2f} kilogrammaa")
