import random
import sys
gra = 0
go = 1
count = 0
def board():
    print (tabela[0:3])
    print (tabela[3:6])
    print (tabela[6:9])


tabela = [" "," "," "," "," "," "," "," "," "]

while go == 1:
    while gra != 1:

        ruch = int(input("Gdzie chcesz umieścić x?"))

        if tabela[ruch-1] == " ":
            tabela[ruch-1] = "x"
            gra = 1
            count = count +1

        else :
            print("To miejsce jest już zajete")

    print (tabela[0:3])
    print (tabela[3:6])
    print (tabela[6:9])
    gra = 0

    if count == 9 :
        print("Koniec gry")
        quit()
    #Komputer
    while gra !=1:
        move = random.randint(1,9)
        print ("Komputer wybrał pozycje :",move)
        print ()

        if tabela[move-1] == " ":
            tabela[move-1] = "o"
            gra = 1
            count = count +1

    if tabela[0] == "o" and tabela [1] == "o" and tabela [2]=="o":
        print ("O wygrało!")
        board()
        quit()

    if tabela[0] == "x" and tabela [1] == "x" and tabela [2]=="x":
        print ("X wygrało!")
        board()
        quit()
        
    if tabela[0] == "o" and tabela [3] == "o" and tabela [6]=="o":
        print ("O wygrało!")
        board()
        quit()
    if tabela[0] == "x" and tabela [3] == "x" and tabela [6]=="x":
        print ("X wygrało!")
        board()
        quit()
    if tabela[1] == "o" and tabela [4] == "o" and tabela [7]=="o":
        print("O wygrało")
        board()
        quit()
    if tabela[1] == "x" and tabela [5] == "x" and tabela [7]=="x":
        print ("X wygrało!")
        board()
        quit()
    if tabela[2] == "o" and tabela [5] == "o" and tabela [8]=="o":
        print ("O wygrało!")
        board()
        quit()
    if tabela[2] == "x" and tabela [5] == "x" and tabela [8]=="x":
        print ("X wygrało!")
        board()
        quit()
    if tabela[0] == "o" and tabela [4] == "o" and tabela [9]=="o":
        print ("O wygrało!")
        board()
        quit()
    if tabela[0] == "x" and tabela [4] == "x" and tabela [8]=="x":
        print ("X wygrało!")
        board()
        quit()
    if tabela[3] == "x" and tabela [4] == "x" and tabela [5]=="x":
        print ("X wygrało!")
        board()
        quit()
    if tabela[3] == "o" and tabela [4] == "o" and tabela [5]=="o":
        print ("O wygrało!")
        board()
        quit()
    if tabela[6] == "o" and tabela [7] == "o" and tabela [8]=="o":
        print ("O wygrało!")
        board()
        quit()
    if tabela[6] == "x" and tabela [7] == "x" and tabela [8]=="x":
        print ("X wygrało!")
        board()
        quit()
    
    print (tabela[0:3])
    print (tabela[3:6])
    print (tabela[6:9])

    
    gra=0
go = 0
        #Komputer 
