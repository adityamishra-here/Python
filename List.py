marks=[100,99,70]
print(marks)
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[-1])
print(marks[-2])
print(marks[-3])
print(marks[0:2])
print(marks[1:2])
print(marks[2:3])
print("Maths",marks[0])
print("Accounts",marks[1])
print("BST",marks[2])
print(marks)
#for loop in list
for score in marks:
print(score)
#Append: use to add element in b/w program
marks.append(100)
print(marks)
# Insert: use to add element in desired postion by mentioning the index no
marks.insert(0,200)
print(marks)
print(200 in marks)
print(50 in marks)
print(len(marks))

OUTPUT:
[100, 99, 70]
100
99
70
70
99
100
[100, 99]
[99]
[70]
Maths 100
Accounts 99
BST 70
[100, 99, 70]
100
99
70
[100, 99, 70, 100]
[200, 100, 99, 70, 100]
True
False
5
