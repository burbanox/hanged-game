import os
from random import randint


def playerExist(fileLines,playerName) :
    print("we are in playerexist")
    for i in fileLines :
        if i.split(":")[0] ==playerName:
            return True
    return False 


def getPoints(fileLines,playerName) :
    print(f"fileline : {fileLines}")
    for i in fileLines :
        if i.split(":")[0]==playerName :
            return int(i.split(":")[1])
    return -1

def writePoints(playerName,points) :

    content = []
    with open("./txt-files/players.txt","r") as file :
        content = list(filter(lambda x : x!="\n" , file.readlines()))
        print(f"este es el contenido : {content}")
        file.close()

    with open("./txt-files/players.txt","w+") as file :

        boolean = False #This is for verify if the player points are larger than in the file
        userExist = playerExist(content,playerName) 
        print(userExist)
        if userExist :
            filePoints = getPoints(content,playerName)
            print("filePoints = " + str(filePoints))
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
                print(arr)
            
            if flag==1 :
                arr.append(f"{playerName}:{points}")
            print(arr)
            for i in arr :
                file.write(f"{i}\n")

        else :
            print(content)
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

    playerName = input("Write your nickname : ")
    lives = 1
    points = 0
    word = getWord()
    wordArray = list(map(lambda x: "_",word[0]))

    while(lives!=0) :

        imprimirPantalla(playerName,points,lives,wordArray,word[1])
        leter = input("Escribe una palabra : ")

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
        
        os.system("clear")


    if(lives==0) :
        print(f"You lose :( the word guess was : {word[0]}")

    writePoints(playerName,points)


if __name__ == "__main__" :
    main()