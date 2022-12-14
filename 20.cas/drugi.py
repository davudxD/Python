# Set (skup) je kolekcija koja je neuredjena (unordered) i neindeksirana (unindexed).
# Setovi se zapisuju u viticastim zagradama.

# Elementi seta su neuredjeni, nepromenljivi i ne dozvoljavaju duplikate.
myset = {"srpski jezik", "matematika", "engleski jezik", "programiranje"}
print(myset)

myset = {"srpski jezik", "matematika", "engleski jezik", "programiranje", "matematika"}
print(myset)

duzina = len(myset)
print(duzina)

tip = type(myset)
print(tip)

# Set moze sadrzati razlicite tipove podataka.
myset2 = {"Vahid", 17, False}
print(myset2)

# for petlja je dozvoljena takodje.
for i in myset2:
    if type(i) == int:
        print(i)

# Dodavanje elemenata setu:
myset = {"srpski jezik", "matematika", "engleski jezik", "programiranje"}

myset.add("biologija")
print(myset)

# Sto se tice dodavanja seta drugom setu to se vrsi pomocu mentode update()
myset = {"srpski jezik", "matematika", "engleski jezik", "programiranje"}
myset2 = {"programiranje", "biologija", "fiziko", "hemija"}
myset.update(myset2)
print(myset)

# Za brisanje elemenata se koristi remove() metoda ili discard().
# Postoji jedna razlika izmedju ove dve metode:
# to je da ako pokusamo da izbrisemo nepostojeci element nekog seta preko remove metode dobicemo
# dok preko discard necemo dobiti error.

myset = {"srpski jezik", "matematika", "engleski jezik"}
myset.remove("srpski jezik")
print(myset)

myset.discard("programiranje")
print(myset)

# clear() metoda ce isprazniti ceo set:
myset.clear()
print(myset)

# preko del mozemo izbrisati ceo set:
# del myset
# print(myset)

# Alternativa za update moze biti union() metoda

myset = {"srpski jezik", "matematika", "engleski jezik", "programiranje"}
myset2 = {"programiranje", "biologija", "fiziko", "hemija"}

myset3 = myset.union(myset2)
print(myset3)

myset = {"srpski jezik", "matematika", "engleski jezik", "programiranje"}
myset2 = {"programiranje", "biologija", "fiziko", "hemija"}
#  metoda intersection_update ce nam ostaviti samo one elemente koji su sadrzani u oba seta.
myset.intersection_update(myset2)
print(myset)









