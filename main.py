import os

def remplazarLetra(array,a) :
    arr = []
    
    for i in array :
        if a==i :
            arr.append(a)
        else :
            arr.append("_")

    return arr


def imprimirPantalla(playerName,points,lives,wordArray) :

    print(
    """
    *****************
    *               *    
    *  HANGED GAME  *
    *               *
    *****************

    """)
    print(f"\t{playerName} you have : {points} points\n\n")
    print(f"\tLives = {lives}\n\n")
    
    for i in range(len(wordArray)) :
        if i== 0 :
            print(f"\t{wordArray[i]}",end=" ")
        else :
            print(f"{wordArray[i]}",end=" ")
    
    print("\n\n")

def main():

    playerName = input("Write your nickname : ")
    lives = 1
    points = 0
    word = "harold"
    wordArray = list(map(lambda x: "_",word))

    while(lives) :

        imprimirPantalla(playerName,points,lives,wordArray)
        leter = input("Escribe una palabra : ")

        if leter in word :
            arr = []
            for i in range(len(word)) :
                if leter == word[i] :
                    arr.append(leter)
                else :
                    arr.append(wordArray[i])
            wordArray = arr
        else :
            lives -=1
        
        os.system("clear")

if __name__ == "__main__" :
    main()