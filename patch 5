#Graph of connected edges
map = {1:[[2,3,4],'T'],
       2:[[1,3,5,6],0],
       3:[[1,2,4,6],0],
       4:[[1,3,6,7],0],
       5:[[2,6,8],0],
       6:[[2,3,4,5,7,8,9,10],0],
       7:[[4,6,10],0],
       8:[[5,6,9],'A'],
       9:[[8,10,6],'B'],
       10:[[7,6,9],'C'],
       "turn": "P"}
rlocation = 1
police = ['A','B','C']


#find location of police/robber
def corresponding_key(val, dictionary):
    for k, v in dictionary.items():
        if val in v:
            return k
#find empty coord
def findemptycoord(curloc):
     connectedcoord = map[curloc][0].copy()
     emptycoord=connectedcoord.copy()
     for i in range(len(connectedcoord)):
        if map[connectedcoord[i]][1]!= 0:
            X=connectedcoord[i]
            for j in range(len(emptycoord)):
                if emptycoord[j]==X:
                    emptycoord.pop(j)
                    break
     return emptycoord
#conditions
win = False
lose = False
#map printing
def printmap():
    print("Current Map:")
    print("     "+str(map[1][1])+"     ")
    print("   / | \    ")
    print("  "+str(map[2][1])+"--"+str(map[3][1])+"--"+str(map[4][1]))
    print("  | \|/ |")
    print("  "+str(map[5][1])+"--"+str(map[6][1])+"--"+str(map[7][1]))
    print("  | /|\ |")
    print("  "+str(map[8][1])+"--"+str(map[9][1])+"--"+str(map[10][1]))
    print()
#coord printing
def printmapcond():
    print("Coordinates of the points:")
    print("     "+str(1)+"     ")
    print("   / | \    ")
    print("  "+str(2)+"--"+str(3)+"--"+str(4))
    print("  | \|/ |")
    print("  "+str(5)+"--"+str(6)+"--"+str(7))
    print("  | /|\ |")
    print("  "+str(8)+"--"+str(9)+"--"+str(10))
    print()
def losecond():
    if len(findemptycoord(rlocation)) == 0:
        print("The Robber is trapped! The Police Win!")
        return True
    else:
        return False
        
def wincond():
    if rlocation == 8 or rlocation == 9 or rlocation == 10:
        print("The Robber Escaped! The Robber Wins!")
        return True
    else:
        return False
        
#Starting Condition + Map Gen
print("Introduction:\n The thief has broken into a house and three police are ready to enter the house to catch him.\n""The map of the house is shown below, one player act as the thief and the other as the police. \n""The thief should try to escape, while the police should try to block him from running.\n "'Police are A B C. The thief is T. \n'"\nGame Rules\n""1. For each round, the police move first, and the thief moves next.\n""2. Only one of the police can move in each round.\n""3. Each move should follow the existing road to a connected neighbor node.\n""4. The police must take the move in every round.\n""5. The police cannot move onto an occupied node (no matter who is on this node).\n""6. If the thief cannot take any move, the police win.\n""7. If the thief reaches the exit, the police lose.\n")
#start or load
while True:
    choice = input("Please enter \"start\" or \"load\" ")
    if choice == "load":
        try:
            savef = open("save.txt","r")
            map = eval(savef.read())
            savef.close()
            break
        except:
            print("You do not have any save")
    elif choice == "start":
        break
    else:
        print("Invaild input")
#Gameplay
while lose is False and win is False:
    printmap()
    printmapcond()
    #Police Turn
    if map["turn"] == "P":
        print("Its the Police's Turn!")
        polinput = str(input("Please select a policeman(A,B,C) or enter \"save\" to save the current file ")) #select a police
        if polinput == "save":
            savef=open("save.txt","w")
            savef.write(f"{map}")
            print("File saved")
            savef.close()
            polinput = str(input("Please select a policeman(A,B,C) "))
        while polinput not in police: #select error
            if polinput not in police:
                polinput = str(input('Invalid policeman! Please select policeman A, B, or C '))
        plocation = int(corresponding_key(polinput,map)) #find police location
        print(polinput, ' is in the coordinate', plocation) #Print police location
        freecoord = (findemptycoord(plocation)).copy() #print a list that contain empty location
        print("You can only go to coordinates", freecoord)
        coordinput=0
        while coordinput not in freecoord:
            try:
                coordinput = int(input("Please select a coordinate to go to ")) #selected police go to that coordinate    
                if coordinput not in freecoord: #prevent move to exist location
                    print("Invalid coordinate! You can only go to coordinates ", freecoord)     
            except ValueError:
                print("Invalid coordinate! You can only go to coordinates ", freecoord)     
        map[plocation][1]= 0 #update map: original location to empty
        map[coordinput][1] = polinput #update map : new location to police
        lose=losecond()
        if lose==True: #check if the Thief lose
            break
    #Robber Turn
    map["turn"]="T"
    printmap()
    printmapcond()
    print("Its the Robber's Turn!")
    rlocation = int(corresponding_key("T",map))
    print('The robber is in the coordinate', rlocation)
    freecoord = (findemptycoord(rlocation)).copy()
    print("You can only go to coordinates", freecoord)
    coordinput=0
    while coordinput not in freecoord:
        try:
            coordinput = input("Please select a coordinate to go to or enter \"save\" to save the file ")
            if coordinput == "save":
                savef = open("save.txt","w")
                savef.write(f"{map}")
                print("File saved") 
                savef.close()
            else: 
                coordinput = int(coordinput)
        except ValueError:
            print("Invalid coordinate! You can only go to coordinates ", freecoord)
    map["turn"] = "P"     

    map[rlocation][1]= 0
    map[coordinput][1] = 'T'
    rlocation = coordinput
    win=wincond()
