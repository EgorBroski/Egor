from random import*
var=0
#Выбор
while(var==0):
    igrok=int(input("Что ты выбираешь: 1-камень, 2-ножницы или 3-бумагу"))
    if (igrok==1 or igrok==2 or igrok==3):
        ver=1
#Действие игры
if igrok==1:
    print("КАМЕНЬ!!!")
if igrok==2:
    print("НОЖНИЦЫ!!!")
if igrok==3:
    print("БУМАГА!!!")
komputer = random.randint(1, 3)
if komputer==1:
        print("Компьютер бьёт КАМНЕМ!")
if komputer==2:
    print("Компьютер бьёт НОЖНИЦАМИ!")
if komputer==3:
    print("Компьютер бьёт БУМАГОЙ!")
#Определяем кто выиграл
if igrok==komputer:
        pobeda=0
if igrok==1 and komputer==2:
        pobeda=1 
if igrok==1 and komputer==3:
        pobeda=2 
if igrok==2 and komputer==1:
        pobeda=2  
if igrok==2 and komputer==3:
        pobeda=1 
if igrok==3 and komputer==1:
        pobeda=1
if igrok==3 and komputer==2:
        pobeda=2
if pobeda==0:
        print("Ужас ничья!")
if pobeda==1:
        print("Победил ИГРОК!")
if pobeda==2:
        print("Победил компьютер...")
