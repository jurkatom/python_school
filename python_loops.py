#1) Seznamy (12)
print("1) Seznamy (12)")

names_list = ['Jiri', 'Jan', 'Marie', 'Petr', 'Jana', 'Josef',
'Pavel', 'Martin', 'Jaroslav', 'Tomas', 'Eva', 'Miroslav',
'Hana', 'Anna', 'Zdenek', 'Frantisek', 'Vaclav', 'Michal',
'Lenka', 'Katerina']
name=input("Tell me your name without diacritical marks, please. Or you will be eradicated.\n")
name=str.upper(name[0:1])+name[1:]

if name in names_list:
    print("Your name is in the top 20 czech names.")
else:
    print("Your name is NOT in the top 20 czech names.")

#2) Smyčky (20)
print("\n2) Smyčky (20)")

d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta',
'e':'echo', 'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india',
'j':'juliett', 'k':'kilo', 'l':'lima', 'm':'mike',
'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec',
'r':'romeo', 's':'sierra', 't':'tango', 'u':'uniform',
'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee',
'z':'zulu'}
name=str.lower(input("Tell me your name without diacritical marks again, please.\n"))

for letter in name:
    print(d[letter])

#3) Trasnponovaná matice (21)
print("\n3) Trasnponovaná matice (21)")

a = [[1,2,3],
 [4,5,6],
 [7,8,9]]
b = a

x=0
y=0
while x<3:
    while y<3:
        if x!=y:
            placeholder=a[y][x]
            b[y][x]=a[x][y] 
            b[x][y]=placeholder
        y=y+1
    x=x+1
    y=0+x
    
for z in b:       
    print(z)

#4) Nákupní seznam (25)
print("\n4) Nákupní seznam (25)")

shopping_list = ["milk", "eggs", "beer", "butter", "dark matter", "portal gun", "sorcerer's stone", "lightsaber"]
for item in shopping_list:
    addition=input("Add an item to your shopping list.\n")
    if addition in shopping_list:
        print(str.upper(addition[0:1]) + addition[1:] + " is already in the shopping list.")
        break
    else:
        shopping_list.append(addition)
        print(str.upper(addition[0:1]) + addition[1:] + " was added to your shopping list.")
        
        #V zadani bylo vyresit ulohu pomoci "for", nebylo by kazdopadne lepsi resit pres "while true:"?

#5) List comprehension (28)
print("\n5) List comprehension (28)")

num_list = list(range(1,6))
sqr_num_list = [x*x for x in num_list]
fav_num_list = [str(x) + " is my favorite number!" for x in num_list]

print(sqr_num_list, fav_num_list, sep="\n")

#6) GATTACA (29)
print("\n6) GATTACA (29)")

seq=str.upper(input("Give me some random letters including \"A\"s, please. No spaces!\n"))
a_list=[]
#solution 1
for num, value in enumerate(seq):
    if value=="A":
        a_list.append(num)

print(a_list)

#solution 2
x=0
b_list=[]
for letter in seq:
    if letter=="A":
        b_list.append(x)
    x=x+1
    
print(b_list)

#7) Slovníky (31)
print("\n7) Slovníky (31)")

scores = {'John' : 10, 'Emily' : 35, 'Matthew' : 50}
new_scores = {f:scores[f]*3 for f in scores}
print(new_scores)