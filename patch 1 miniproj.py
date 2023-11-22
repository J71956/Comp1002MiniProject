import pickle
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
       10:[[7,6,9],'C']}
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
     print(connectedcoord)
     for i in range(len(connectedcoord)-1):
        print(i)
        if map[connectedcoord[i-1]][1]!= 0:
            connectedcoord.pop(i-1)
     return connectedcoord
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
def losecond(freecoord):
    if len(freecoord) == 0:
        lose = True
        
def wincond(rlocation):
    
    if rlocation == 8 or rlocation == 9 or rlocation == 10:
        win = True
        
#Starting Condition + Map Gen
print("Introduction:\n The thief has broken into a house and three police are ready to enter the house to catch him.\n""The map of the house is shown below, one player act as the thief and the other as the police. \n""The thief should try to escape, while the police should try to block him from running.\n "'Police are A B C. The thief is T. \n'"\nGame Rules\n""1. For each round, the police move first, and the thief moves next.\n""2. Only one of the police can move in each round.\n""3. Each move should follow the existing road to a connected neighbor node.\n""4. The police must take the move in every round.\n""5. The police cannot move onto an occupied node (no matter who is on this node).\n""6. If the thief cannot take any move, the police win.\n""7. If the thief reaches the exit, the police lose.\n")
#Gameplay
while lose is False and win is False:
    printmap()
    printmapcond()
    #Police Turn
    print("Its the Police's Turn!")
    polinput = str(input('Please select a policeman ')).capitalize()
    while polinput not in police== True:
          polinput = str(input('Invalid policeman! Please select policeman A, B, or C'))
    plocation = int(corresponding_key(polinput,map))
    print(polinput, ' is in the coordinate', plocation)
    freecoord = findemptycoord(plocation)
    print("You can only go to coordinates", freecoord)
    coordinput = int(input("Please select a coordinate to go to"))
    while coordinput not in freecoord == True:
        print("Invalid coordinate! You can only go to coordinates ", freecoord)     
        coordinput = int(input("Please select a coordinate to go to"))
    map[plocation][1]= 0
    map[coordinput][1] = polinput
    losecond(findemptycoord(rlocation))
    #Robber Turn
    printmap()
    printmapcond()
    print("Its the Robber's Turn!")
    rlocation = int(corresponding_key("T",map))
    print('The robber is in the coordinate', rlocation)
    freecoord = findemptycoord(rlocation)

    print("You can only go to coordinates", freecoord)
    coordinput = int(input("Please select a coordinate to go to"))
    while coordinput not in freecoord == True:
        print("Invalid coordinate! You can only go to coordinates ", freecoord)     
        coordinput = int(input("Please select a coordinate to go to"))
    map[rlocation][1]= 0
    map[coordinput][1] = 'T'
    rlocation =coordinput
    wincond(rlocation)
if win == True:
    print("The Robber Escaped! The Robber Wins!")
elif lose == True:
    print("The Robber is trapped! The Police Win!")
