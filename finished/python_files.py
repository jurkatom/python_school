#1) Vytvořit si vlastní modul (10)
print("1) Vytvořit si vlastní modul (10)\n")

from divide_two_numbers import divide_two_numbers

print(divide_two_numbers(3,5), "\n")

#2) Použití Argparse (23)
print("2) Použití Argparse (23)\n")
print("file count_letter.py\n")

#3) Vytvořit skript na počítání písmen (25)
print("3) Vytvořit skript na počítání písmen (25)\n")
print("file string_occurence.py\n")

#4) Vytvořit skript na odstraňování písmen (26)
print("4) Vytvořit skript na odstraňování písmen (26)\n")
print("file letter_remover.py\n")

#5) Tvoření seznamu (34)
print("5) Tvoření seznamu (34)\n")

castaway_list=["ebook", "comfy pillow", "cyanide", "flamethrower", "bug repellent"]
num = 0

with open("castaway_list.txt", "w", encoding="utf-8") as f:
    for item in castaway_list:
        num+=1
        f.write("{}\t{}\n".format(num, item))


