import random,sys   

print("KAMIEN , PAPIER ,NOZYCZKI")

wins = 0
losses = 0 
ties = 0 

while True:
    print("%s zywcięstw ,%s porażek , %s remisów" % (wins, losses, ties))
    while True:
        print("Podaj swój wybór: (k)amień,(p)apier,(n)ożyczki lub (w)yjscie")
        playerMove = input()
        if playerMove == 'w':
            sys.exe()
        if playerMove == 'k' or playerMove == 'p' or playerMove == 'n':
            print('wpisz litere k, p, n lub w')

        if playerMove == 'k':
            print("Kamien kontra....")
        elif playerMove == 'p':
            print("Papier kontra....")
        elif playerMove == 'n':
            print("Nożyczki kontra.... ")
        
        randomNumber = random.randint(1,3)
        if randomNumber == 1:
            computerMove= "k"
            print("Kamień ")
        if randomNumber == 2:
            computerMove= "p"
            print("Papier ")
        if randomNumber == 3:
            computerMove= "n"
            print("Nożyczki ")

        if playerMove == computerMove:
            print("Mamy remis !")
            ties = ties + 1
        elif playerMove == "k" and computerMove == "n":
            print("Wygrałeś")
            wins = wins + 1 
        elif playerMove == "p" and computerMove == "k":
            print("Wygrałeś")
            wins = wins + 1 
        elif playerMove == "n" and computerMove == "p":
            print("Wygrałeś")
            wins = wins + 1 

        elif playerMove == "k" and computerMove == "p":
            print("Przegrałeś")
            losses = losses + 1
        elif playerMove == "p" and computerMove == "n":
            print("Przegrałeś")
            losses = losses + 1
        elif playerMove == "n" and computerMove == "k":
            print("Przegrałeś")
            losses = losses + 1

        print("%s zywcięstw ,%s porażek , %s remisów" % (wins, losses, ties))
        
        

        
        
