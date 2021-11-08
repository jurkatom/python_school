#1) Dědictví (11)
print("1) Dědictví (11)")

heritage = 1256983
children_num = 28
remaining = heritage % children_num
print("King will have " + str(remaining) + " coins remaining.");

#2) Ověření matematických výsledků (16)
print("\n2) Ověření matematických výsledků (16)")

if ((12**52%15)<8) or (3**5)>100:
    evaluation="true"
else:
    evaluation="false"
print("Statement that remainder after division of 12^52 by 15 is less than 8 or 3^5 is more than 100 is " + evaluation)

if (5*(3**3))!=(900/75):
    evaluation="true"
else:
    evaluation="false"
print("Statement that 5 times 3^3 is not equal to 900 divided by 75 is " + evaluation)

#3) Balení do závorek nebo množení písmen (21)
print("\n3) Balení do závorek nebo množení písmen (21)")

str1="[[]]"
str2="PYTHON"
merged_strs=str1[0:2] + str2 + str1[2:4]
print(merged_strs)

print("Python"[4:6]*4)
print("Perl"[2:3]*6)

#4) Hrátky s řetězci (24)
print("\n4) Hrátky s řetězci (24)")

word="python"
word_lenght=int(len(word))
half_of_word_lenght=int(word_lenght/2)
print(word[:half_of_word_lenght].upper() + word[half_of_word_lenght:].lower())

for x in range (0,2):
    print(word[0] * word_lenght)
    word="git"
    word_lenght=int(len(word))

#5) Vyřešení chyby (27)
print("\n5) Vyřešení chyby (27)")

print("Result of expression print(7+3*2) will be string of number 13, since both are integers.")
print("Result of expression print('7' + str(3*2)) will be string of number 7 and string of number 6 without space")
print("Result of expression print('7' + '3*2') will be string of number 7 and string of expression 3*2 without space")
print("Expression print('7' + 3*2) will result in error, since it's not possible to use additon with string and integer")

#6) Hobby proměnná (31)
print("\n6) Hobby proměnná (31)")

hobby="being a couch potato"
print("My hobby is {0}.".format(hobby))
date="2018-11-01"
print("{0}/{1}".format(date[8:10], date[5:7]))

#7) Práce se seznamy (37)
print("\n7) Práce se seznamy (37)")

list=["being a couch-potato"]
list.append("eating")
list.append("sleeping")
list.append("reading")
print("I like " + list[0] + " the most.")
print("I like " + list[-1] + " the least.")
del list

#8) Řazení měst (38)
print("\n8) Řazení měst (38)")

cities=["Prague", "Brno", "Ostrava", "Plzen", "Liberec", "Olomouc", "Usti nad Labem", "Hradec Kralove", "Ceske Budejovice", "Pardubice"]
cities.sort()
print(cities)
print("*".join(cities))

#9) Zen of Python (49)
print("\n9) Zen of Python (49)")

alphabet=set("abcdefghijklmnopqrstuvwxyz")
text=set("""Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
""")
print("Unused letters were " + (str(alphabet.difference(text)))[1:-1] + ".")

#10) Odstranění ze slovníku (50)
print("\n10) Odstranění ze slovníku (50)")

d = {'payton':'An interpreted, object-oriented programming language'}
d["python"] = d["payton"]
del d["payton"]
print(d)

phonebook = {('John','Doe'):'123456789'}
print(phonebook)

#11) Práce se slovníkem (51)
print("\n11) Práce se slovníkem (51)")

info = {('Name', 'Surname'):('John', 'Doe')}
name_sur = str(list(info.values()))
print(name_sur[3:7] + "_" + name_sur[11:14])