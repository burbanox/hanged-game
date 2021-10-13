import os
from random import randint


def playerExist(fileLines,playerName) :
    for i in fileLines :
        if i.split(":")[0] ==playerName:
            return True
    return False 


def getPoints(fileLines,playerName) :
    for i in fileLines :
        if i.split(":")[0]==playerName :
            return int(i.split(":")[1])
    return -1

def writePoints(playerName,points) :

    content = []
    with open("./txt-files/players.txt","r") as file :
        content = list(filter(lambda x : x!="\n" , file.readlines()))
        file.close()

    with open("./txt-files/players.txt","w+") as file :

        boolean = False #This is for verify if the player points are larger than in the file
        userExist = playerExist(content,playerName) 
        if userExist :
            filePoints = getPoints(content,playerName)
            if filePoints < points :
                boolean = True
                content.pop(content.index(f"{playerName}:{filePoints}\n"))
        
        if(not userExist) or boolean :
            arr = []
            flag = 1

            for i in content :
                if (int(i.split(":")[1]) < points) and flag != 0 :
                    arr.append(f"{playerName}:{points}\n")
                    arr.append(i)
                    flag = 0
                else :
                    arr.append(i)
            
            if flag==1 :
                arr.append(f"{playerName}:{points}")
            for i in arr :
                file.write(f"{i}\n")

        else :
            for i in content :
                file.write(f"{i}\n")

        file.close()

def getWord() :
    word = []
    with open("./txt-files/words.txt","r") as file :
        content = file.readlines()
        word = content[randint(0,len(content)-1)].split(":")
    return word

def remplazarLetra(array,a) :
    arr = []
    
    for i in array :
        if a==i :
            arr.append(a)
        else :
            arr.append("_")

    return arr


def imprimirPantalla(playerName,points,lives,wordArray,definition) :

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
    print(f"\tDefinition : {definition}\n\n")

    for i in range(len(wordArray)) :
        if i== 0 :
            print(f"\t{wordArray[i]}",end=" ")
        else :
            print(f"{wordArray[i]}",end=" ")
    
    print("\n\n")

def main():
    nameExist = False
    errorMessage = ""
    while(not nameExist) :
        try :
            playerName = input(f"Write your nickname {errorMessage} : ")
            if playerName == "" :
                os.system("clear")
                raise ValueError("You must write Something")
            nameExist = True
            errorMessage = ""
        except ValueError as error:
            errorMessage = f"({error})"

    lives = 1
    points = 0
    word = getWord()
    wordArray = list(map(lambda x: "_",word[0]))

    while(lives!=0) :

        try :
            imprimirPantalla(playerName,points,lives,wordArray,word[1])
            print("write exit to exit")
            leter = input(f"Escribe una palabra {errorMessage} : ")

            if leter=="exit" :
                os.system("clear")
                break
            elif len(leter) > 1 :
                raise ValueError("You must only write one charecter")
            errorMessage = ""

            if leter in word[0] :
                arr = []
                for i in range(len(word[0])) :
                    if leter == word[0][i] :
                        arr.append(leter)
                    else :
                        arr.append(wordArray[i])
                wordArray = arr
                points +=1
            else :
                lives -=1
        
            if "_" not in wordArray :
                word = getWord()
                wordArray = list(map(lambda x: "_",word[0]))

        except ValueError as error :
            errorMessage = f"({error})"
        
        os.system("clear")


    if(lives==0) :
        print(f"You lose :( the word guess was : {word[0]}")

    writePoints(playerName,points)
    print(f"Your points were : {points}")


if __name__ == "__main__" :
    main()