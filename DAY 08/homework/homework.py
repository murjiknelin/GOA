# Python:

# Easy:
# 1. დაპრინტეთ 12 მაგალითი შედარების ოპერატორებზე (<, >, <=, >=, == , !=)
# 2. შეინახე ინტეჯერი ცვლადში, შემდეგ დაპრინტე მისი ტიპი.
# 3. შეინახე სტრინგი ცვლადში, შემდეგ დაპრინტე მისი ტიპი.
# 4. შეინახე ფლოატი ცვლადში, შემდეგ დაპრინტე მისი ტიპი.
# 5. შექმენი ცვლადი, სადაც შეინახავ "42"-ს, შემდეგ ეს ცვლადი გადააქციე ინეტეჯერად და დაპრინტე.
# 6. შექმენი ცვლადი, სადაც შეინახავ "3.14"-ს, შემდეგ ეს ცვლადი გადააქციე ფლოატად და დაპრინტე.

# Medium:
# 7. ცვლადში მომხმარებელს ინფუთით შემოატანინე სტრინგი, და დაპრინტე მისი ტიპი.
# 8. ცვლადში მომხმარებელს ინფუთით შემოატანინე ინტეჯერი, და დაპრინტე მისი ტიპი.
# 9. ცვლადში მომხმარებელს ინფუთით შემოატანინე ფლოათი, და დაპრინტე მისი ტიპი.

# Hard:
# 10. ცვლადში მომხარებელს ინფუთით შემოატანინე მისი ასაკი, და დაუპრინტე თუ რომელი წელი იყო მისი დაბადების დროს.
# 11. ცვლადში მომხმარებელს ინფუთით შემოატანინე მისი ასაკი, მეორე ცვლადში კი მამამისის ასაკი, საბოლოოდ დაუპრინტე, თუ რამდენჯერ დიდი იქნება მამამისი მასზე 15 წლის შემდეგ.


#1
print(54 < 100)
print(34 < 45)
print(130 > 55)
print(78 > 23)
print(287 <= 287)
print(245 <= 356)
print(564 >= 564)
print(743 >= 45)
print(339 == 339)
print(45 == 45)
print(845 != 774)
print(678 != 56)

#2

age = 14
print(type(age))

#3

name = "achi"
print(type(name))

#4

hight = 1,7
print(type(hight))

#5

money = "42"
print(int(money))

#6

wallet = "3.14"
print(float(wallet))

#7

woll = input()
print(type(woll))

#8

rooom = int(input())
print(type(rooom))

#9

roof = float(input())
print(type(roof))  

#10

age =  int(input(" enter your age" ))
print(2024 - age)

#11

my = int(input("enter your age here"))
dad = int(input("enter your dads age here"))
my1 = my + 15
dad1 = dad + 15
print(my1 / dad1)


