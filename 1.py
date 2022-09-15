import random

sang_kaghaz_ghichi=[1,2,3]
count=0
player1=0
player2=0
while True:
    
    a=int(input('select:1. tak nafare  2. do nafare? '))
    b=int(input('bazi chand dor bashad? 1 3 5?'))
    if a==1:
        for i in range(b):
            
            player=input('select:1. sang  2.kaghaz  3.ghichi')
            camputer=random.choice(sang_kaghaz_ghichi)
            count+=1
            print("camputer:",camputer)
        if player==camputer:
            count-=1
            continue
        elif (player==1 and camputer==3) or(player==3 and camputer==2) or(player==2 and camputer==1):
            player1+=1
            break
        elif (player==1 and camputer==2) or(player==2 and camputer==3) or (player==3 and camputer==1):
            player2+=1
            break
        print(player1,player2)
        print(count)
        if player1>player2:
            print('you win')
        elif player1 <player2:
            print('i win :)') #in bakhsh javab nmide.

    elif a==2 :
        for i in range(b):
            player=input('player1 :1. sang  2.kaghaz  3.ghichi') 
            player_2=input('player2 :1. sang  2.kaghaz  3.ghichi')
            count+=1
        if player==player_2:
            count-=1
            continue
        elif (player==1 and player_2==3) or(player==3 and player_2==2) or(player==2 and player_2==1):
            player1+=1
            break
        elif (player==1 and player_2==2) or(player==2 and player_2==3) or (player==3 and player_2==1):
            player2+=1
            break
