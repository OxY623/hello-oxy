from random import *
import string
#Шифр Цезаря
alf_lower_eng='abcdefghijklmnopqrstuvwxyz'
alf_upper_eng='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alf_upper_ru = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alf_lower_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
def shifr(text,menu,key):
    #text = text.lower()
    print('Вот и ваш результат:')
    shifrovka=''


    for letter in text:
        if letter in alf_lower_ru:
            i = alf_lower_ru.find(letter)
            if menu == 'Ш':
                key_new = (i+key) % len(alf_lower_ru)
            elif menu == 'Р':
                key_new = (i - key) % len(alf_lower_ru)
            shifrovka += alf_lower_ru[key_new]
        elif letter in alf_upper_ru:
            i = alf_upper_ru.find(letter)
            if menu == 'Ш':
                key_new = (i + key) % len(alf_upper_ru)
            elif menu == 'Р':
                key_new = (i - key) % len(alf_upper_ru)
            shifrovka += alf_upper_ru[key_new]
        elif letter in alf_upper_eng:
            i = alf_upper_eng.find(letter)
            if menu == 'Ш':
                key_new = (i + key) % len(alf_upper_eng)
            elif menu == 'Р':
                key_new = (i - key) % len(alf_upper_eng)
            shifrovka += alf_upper_eng[key_new]
        elif letter in alf_lower_eng:
            i = alf_lower_eng.find(letter)
            if menu == 'Ш':
                key_new = (i + key) % len(alf_lower_eng)
            elif menu == 'Р':
                key_new = (i - key) % len(alf_lower_eng)
            shifrovka += alf_lower_eng[key_new]
        else:
            shifrovka += letter
    print(shifrovka)
#Запускаем цикл по буквам, прибавляем ключб выводим на экран.
#Поддерживает два языка



    #text=input()
    #key=int(input())
a = input('''Сообщение, которое нужно переделать: > ''')
work = input('Зашифровать введите "Ш", расшифровать введите "Р": > ')
n = int(input('''Сдвиг шифрования: > '''))
#a='Hawnj pk swhg xabkna ukq nqj.'
#work='Р'

#x=1

#while x!=26:
    #shifr(a, work, n)
    #x +=1