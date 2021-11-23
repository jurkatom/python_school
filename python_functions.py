#1) 2 cviceni na zaklady funkci (8)
print("1) 2 cviceni na zaklady funkci (8)\n")

def divide_two_nums(n1, n2):
    x=n1/n2
    if n1%n2==0:
        return int(x)
    return x

def sum_of_nums(num_list):
    total_sum=0
    for num in num_list:
        total_sum=total_sum+num
    return total_sum

num_list_example=[5, 4, 1, 13, 42]

print("10 divided by 2 is " + str(divide_two_nums(10,2)))
print("Total sum of a made up list is " + str(sum_of_nums(num_list_example))+"\n")

#2) Lambda funkce (12)
print("2) Lambda funkce (12)\n")

list_size = (
    lambda random_list: print("big list\n") if len(random_list) > 5 else
    print("small list\n"))

big_apple_list=["apple", "second apple", "more apples", "too much apples", "who eats this much apples?", "windows"]

list_size(big_apple_list)
    
#3) Funkce s jednim parametrem (21)
print("3) Funkce s jednim parametrem (21)\n")

s="Peter Piper picked a peck of pickled peppers. A peck of pickled peppers Peter Piper picked.If Peter Piper picked a peck of pickled peppers, where’s the peck of pickled peppers Peter Piper picked?"

def string_upper_lower(string):
    uppercase=0
    lowercase=0
    for x in string:
        if x.isupper():
            uppercase+=1
        elif x.islower():
            lowercase+=1
    print("Uppercase letters: "+str(uppercase)+"\nLowercase letters: "+str(lowercase)+"\n")
    
string_upper_lower(s)

#4) Funkce s dvema parametry (22)
print("4) Funkce s dvema parametry (22)\n")

def meal_vouchers(price, voucher_value):
    voucher_num=int(price/voucher_value)
    cash=price%(voucher_value*voucher_num)
    print("Lunch cost: "+str(price)+" CZK\nPay in cash: "+str(cash)+" CZK\nPay in meal vouchers: "+str(voucher_num)+" pcs, "+str(voucher_value)+" CZK each\n")
    
meal_vouchers(500, 74)

#5) Rekurzivni funkce (24)
print("5) Rekurzivni funkce (24)\n")

def factorial_function(num, fact=1):
    if num==1:
        print(fact)
    else:
        fact=fact*num
        factorial_function(num-1, fact)
    
factorial_function(1)
factorial_function(3)