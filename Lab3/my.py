temp = float(input("Введите свою температуру: "))
if(temp < 35.6):
    print("Вы труп?")
elif (temp > 35.6 and temp < 37):
    print("Вы здоровый человек!")
else:
    print("Вам нужно лечиться!")