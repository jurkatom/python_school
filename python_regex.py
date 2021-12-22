#1) Nahrazení v textu (13)
print("1) Nahrazení v textu (13)\n")
# (\w)(\w+)\s+(\w+)
# \1\. \3

#2) Zen of Python (18)
print("2) Zen of Python (18)\n")
import re
text = "The Zen of Python, by Tim Peters\n\nBeautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated.\nFlat is better than nested.\nSparse is better than dense.\nReadability counts.\nSpecial cases aren't special enough to break the rules.\nAlthough practicality beats purity.\nErrors should never pass silently.\nUnless explicitly silenced.\nIn the face of ambiguity, refuse the temptation to guess.\nThere should be one-- and preferably only one --obvious way to do it.\nAlthough that way may not be obvious at first unless you're Dutch.\nNow is better than never.\nAlthough never is often better than *right* now.\nIf the implementation is hard to explain, it's a bad idea.\nIf the implementation is easy to explain, it may be a good idea.\nNamespaces are one honking great idea -- let's do more of those!"
print(len(re.findall(r"[ao]\.", text)))
print(len(re.findall(r"[^\W_]", text)))
print(len(re.findall("[Tt][Tt]", text)))
print(len(re.findall("[Tt][Tt]?", text)), "\n")

#3) Name function (26)
print("3) Name function (26)\n")

while True:
    user_name = input("Give me your name, please:")
    match = re.search("[A-Z][a-z]*", user_name)
    if match == None or match.group() != user_name:
        print("Your name is not correct, try again!\n")
    elif match.group() == user_name:
        break

#4) Ponechání pouze čísel (29)
print("\n4) Ponechání pouze čísel (29)\n")

def only_digits(string):
    number = re.sub(r"\D", "", string)
    return number

numbers = only_digits('2004-959-559 # This is Phone Number')
print(numbers)
numbers = only_digits("I don't have any numbers.")
print(len(numbers), "\n")
