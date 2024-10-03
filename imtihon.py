# 1. Foydalanuvchi ismi va yoshini kiritsin. Siz f stringni ishlatib foydalanuvchi haqidagi ma’lumotni
# ekranga chiqaring.
# name = input("Ismingizni kiriting: ")
# surname = input("Familiyangizni kiriting: ")
# print(f"Salom {name.capitalize()} {surname.capitalize()}, guruhga xush kelibsiz")
from itertools import count

# 2. Foydalanuvchi input orqali kiritgan sonning kvadratini hisoblab ekranga chiqaradigan dastur tuzing.
# number = int(input("Son kiriting: "))
# print(f"{number} ning kvadrati: {number ** 2}")


# 3. Tuple ochib 4 ta son kiriting. For loopdan foydalanib tupledagi 3 ga qoldiqsiz bo’linadigan sonlarni
# ekranga chiqaring.
# numbers = (12,15,20,18)
# for number in numbers:
#     if number % 3 == 0:
#         print(number, end="  ")


# 4. 23 ni 5 ga bo’lgandagi qoldiqni chiqarib beruvchi dastur tuzing.
# qoldiq = 23 % 5
# print(f"23 ni 5 ga bo'lganda qoldiq: {qoldiq} chiqadi")


# 5. Foydalanuvchi tug’ilgan yilini kiritsin. Siz foydalanuvchining yoshini hisoblab ekranga chiqaring.
# age = int(input("Tug'ilgan yilingizni kriting: "))
# print(f"Salom Shukrullo. Sizning yoshingiz {2024 - age} da")


# 6. Funksiyaga argument sifatida bir son bering. Funksiyangiz sonning toq yoki juftligini aniqlasin.
# number = int(input("Son kiriting: "))
# def main(son):
#     if son % 2 == 0:
#         print("Juft son")
#     else:
#         print("Toq son")
# main(number)


# 7. a va b o’zgaruvchilar berilgan. a ning qiymatini b ga, b ning qiymatini a ga o’zgartirib ekranga
# chiqaring.
# a = input("a sonni kiriting: ")
# b = input("b sonni kiriting: ")
# print(f"a soni {b} ga teng")
# print(f"b soni {a} ga teng")


# 8. 1 dan 100 gacha bo’lgan sonlarni ekranga chiqaring. 5 ga bo’linadigan sonlar tashlab ketilsin.
# for i in range(1,101):
#     if i % 5 == 0:
#         continue
#     else:
#         print(i)


# 9. Quyidagi kod ekranga qanday natija chiqarishini yozing. (Kompyuter yoki telefonda yozib tekshirish
# mumkin emas, qo’lga tushsangiz balingiz olib tashlanadi!
# natija:
# 1
# 1
# 1
# 1
# 1


# 10. random orqali 1 dan 50 gacha bo’lgan sonlar orasidan bir tasodifiy son chiqaring va u sonning toq
# yoki juftligini aniqlaydigan dastur tuzing.
# import random
# random_number = random.randint(1, 50)
# if random_number % 2 == 0:
#     print(f"Bu {random_number} juft son")
# else:
#     print(f"Bu {random_number} toq son")


# 11. Tuple ochib ichiga 4 ta element yozing. for loop dan foydalanib elementlarni teskarisiga
# chiqaradigan dastur tuzing.
# sonlar = (5,8,7,15)
# for son in reversed(sonlar):
#     print(son)


# 12. Foydalanuvchi a va n sonlarini kiritsin. a dan n gacha bo’lgan sonlar yig’indisini hisoblab, yig’indini
# ekranga chiqaruvchi dastur tuzing.
# Yig’indi deb hamma sonlar qo’shib chiqilgandagi natija nazarda tutilyapti.
# son = 0
# for i in range(1,11):
#     son += i
# print(son)


# 13. Foydalanuvchi vergul bilan ismlar kiritsin( split() orqali ularni listga olish kerak ). Kiritilgan ismlarni
# teskari tartibda chiqarib beradigan dastur tuzing.
# ismlar = input("Ismingizni kiriting: ").split(",")
# for ism in reversed(ismlar):
#     print(ism, end=" ")


# 14. Bir dictionary oching va ichiga 3 ta element yozing. Uchchala elementning ham valuelari integer
# sonlar bo’lsin. Tuzilgan dictionaryning valuelarini sort qilib ekranga chiqaring.
# element = {"Abor":22,
#            "Temur": 18,
#            "Shukrullo":23
#            }
# elem = list(element.values())
# elem.sort()
# for i in elem:
#     print(i, end="  ")


# 15. Quyidagi kodning natijasini yozing.
# Kompyuter yoki telefonda yozib tekshirish mumkin emas, qo’lga tushsangiz balingiz olib
# tashlanadi.
# sonlar = [4,36,61,72]


# 16. 2 ta set oching va ikkalasiga ham mevalarni yozing. Ikkalasi uchun umumiy bo’lgan( ham a setda,
# ham b setda bor bo’lgan ) elementlarni ekranga chiqaring.
# mevalar1 = {"olma", "nok", "anor","uzum"}
# mevalar2 = {"olma", "behi", "uzum", "shaftoli"}
# orasidagi_farq = mevalar1.intersection(mevalar2)
# print(orasidagi_farq)


# 17. 3 ta integer son berilgan. Ularning nechtasi musbat ( 0 dan katta ), nechtasi manfiy( 0 dan kichik )
# ligini aniqlab ekranga chiqaradigan dastur tuzing.
# a,b,c = 2,5,-6
#
# positive_count = 0
# negative_count = 0
# for num in [a,b,c]:
#     if num > 0:
#         positive_count += 1
#     elif num < 0:
#         negative_count += 1
#
# print(f"Musbat sonlar: {positive_count}")
# print(f"Manfit sonlar: {negative_count}")



# 18. Foydalanuvchi bitta ikki xonali son kiritsin. Uning raqamlari o’rnini almashtirishdan hosil bo’ladigan
# sonni ekranga chiqaring.
# user_input = 57
# onlik = user_input // 10
# birlik = user_input % 10
# reversed_number = birlik * 10 + onlik
# print(reversed_number)


# 19. Faqat ismlardan iborat bo’lgan list oching. Foydalanuvchidan ism so’rang, kiritilgan ism listda bor
# bo’lsa, “Siz ro’yxatda borsiz ” degan yozuv chiqarsin. Aks holda ismni listga qo’shsin va ism listga
# qo’shilgani haqida ekranga xabar chiqarsin.
# Faqat ismlardan iborat list
# names_list = ["Ali", "Bobur", "Laylo", "Otabek"]
# user_input = "Zuhra"
# if user_input in names_list:
#     print("Siz ro'yxatda borsiz")
# else:
#     names_list.append(user_input)
#     print(f"{user_input} ism ro'yxatga qo'shildi")
# print(names_list)



# 20. Foydalanuvchidan input orqali ism, familiyasini qabul qiling. Ikkalasini ham 1-harfini katta harfga
# o’zgartirib ekranga chiqaring.
# ism_kirit = input("Ismingizni kiriting: ")
# fam_kirit = input("Familiyangizni kiriting: ")
# natija = f"Salom {ism_kirit.capitalize()} {fam_kirit.capitalize()}"
# print(natija)


# 21. Sonlardan iborat list oching. O’zingiz istagan usulda list boshiga toq sonlarni, undan keyin juft
# sonlarni joylang.
sonlar = [2,5,8,6,4,7]


# 22. Bitta listni argument qilib oluvchi funksiya yozing. Funksiyangiz list ichidagi hamma toq sonlarni juft
# songa aylantirib chiqsin, juft sonlar esa o’zgarishsiz qolsin.
# number = [2,5,7,8,6,3,5]
# def reverse_son(son):
#     for i in son:
#         if i % 2 == 1:
#             print(i + 1)
#         else:
#             print(i)
# reverse_son(number)
