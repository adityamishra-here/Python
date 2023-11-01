students = ["Aditya", "Anany", "Ansh", "Anant", "Anshul"]

for i in students:
print(i)

print("\n")

for i in students:
if i == "Ansh":
break
print(i)
print("\n")

for i in students:
if i == "Anant":
break
print(i)
print("\n")

for i in students:
if i == "Anant":
continue
print(i)


OUTPUT:
Aditya
Anany
Ansh
Anant
Anshul


Aditya
Anany


Aditya
Anany
Ansh


Aditya
Anany
Ansh
Anshul
