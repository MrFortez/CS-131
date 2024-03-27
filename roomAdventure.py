import random


class Room:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.exits = []
        self.grabbables = []
        self.exitNames = []
        self.itemDescriptions = []
        self.isLocked = False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value
    
    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    @property
    def exitNames(self):
        return self._exitNames

    @exitNames.setter
    def exitNames(self, value):
        self._exitNames = value

    @property
    def itemDescriptions(self):
        return self._itemDescriptions 

    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value

    @property
    def isLocked(self):
        return self._isLocked

    @isLocked.setter
    def isLocked(self, value):
        self._isLocked = value

    def addExit(self, exitName, destinationRoom):
        self.exitNames.append(exitName)
        self.exits.append(destinationRoom)

    def addItem(self, itemName, itemDescription):
        self.items.append(itemName)
        self.itemDescriptions.append(itemDescription)

    def addGrabbable(self, grabbable, location):
        self.grabbables.append([grabbable, location])

    def delGrabbable(self, item):
        self._grabbables.remove(item)

    def __str__(self):
        s = ''

        #let's concatenate the room name
        s+="You are in "+self.name+"\n\n"

        #then let's add the items
        s+="You see:\n"
        for item in self.items:
            s+=item+"\n"

        s+="\n"
        
        #and now the exits
        s+="Exits to the:\n"
        for exitName in self.exitNames:
            s+=exitName+"\n"

        return s

def createRooms():
    #add the rooms
    r1 = Room("Room 1")
    r2 = Room("Room 2")
    r3 = Room("Room 3")
    r4 = Room("Room 4")
    r5 = Room("Room 5")
    r6 = Room("Room 6")
    r7 = Room("Room 7")
    r8 = Room("Room 8")
    r9 = Room("Room 9")

    #this room is for the end sequence and will be attached to a random viable room
    r0 = Room("Escape")

    #array of rooms
    roomLayout = [[r1, r2, r3], [r4, r5, r6], [r7, r8, r9]]

    #randomize the safe's code
    global safeCode 
    safeCode = [random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)]
    # print(safeCode)

    #randomize the vault's code
    global vaultCode
    vaultCode = [random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)]
    # print(vaultCode)

    #determine the color order for the vault code
    global vaultCodeOrder
    vaultCodeOrder = ["red", "yellow", "green", "blue", "purple"]
    random.shuffle(vaultCodeOrder)
    # print(vaultCodeOrder)
    
    #add the exits
    for i in range(0,3):
        for j in range(0, 3):
            if i > 0:
                roomLayout[i][j].addExit("north", roomLayout[i - 1][j])
          
            if j < 2:
                roomLayout[i][j].addExit("east", roomLayout[i][j + 1])
 
            if i < 2:
                roomLayout[i][j].addExit("south", roomLayout[i + 1][j])

            if j > 0:
                roomLayout[i][j].addExit("west", roomLayout[i][j - 1])

    #the exit room will be attached to any room in the top row, always as a north exit
    exitLocation = random.randint(0, 2)
    roomLayout[0][exitLocation].addItem("door", f"a door in the north of this room. that seems to lead out of the mansion. It is barricaded, you'd need some kind of tool to break through")
    roomLayout[0][exitLocation].addExit("north", r0)


    #ADD THE ITEMS (randomized :D)
    #Vault will always be in one of the bottom 3 rooms
    vaultLocation = random.randint(0, 2)
    roomLayout[2][vaultLocation].addItem("vault", "a large metal vault, there seems to be a 5 digit lock on it (use the verb unlock to try and solve it)")

    #Table and key will always spawn in one of the top three rooms, which will never be locked
    keyLocation = random.randint(0, 2)
    roomLayout[0][keyLocation].addItem("table","A woooden table.")

    #Kitchen will always spawn in one of the middle three rooms
    kitchenLocation = random.randint(0, 2)
    roomLayout[1][kitchenLocation].addItem("stove","A cooking stove.")
    roomLayout[1][kitchenLocation].addItem("refrigerator", "A black refrigerator.")

    #Game room can spawn in any of the middle or bottom rooms that dont have the kitchen or vault
    while (True):
        gameLocation = [random.randint(1, 2), random.randint(0, 2)]
        if (not (gameLocation[0] == 1 and gameLocation[1] == kitchenLocation)):
            if (not (gameLocation[0] == 2 and gameLocation[1] == vaultLocation)):
                break

    roomLayout[gameLocation[0]][gameLocation[1]].addItem("pooltable", "An old pool table.")
    roomLayout[gameLocation[0]][gameLocation[1]].addItem("dartboard", f"A dart board. There are darts on {safeCode[0]}, {safeCode[1]}, and {safeCode[2]}")

    #Bedroom can spawn in any of the top or middle rooms that isnt the kitchen
    while (True):
        bedLocation = [random.randint(0, 1), random.randint(0, 2)]
        if (not (bedLocation[0] == 1 and bedLocation[1] == kitchenLocation)):
            break

    roomLayout[bedLocation[0]][bedLocation[1]].addItem("bed", f"A queen-sized bed, it's quite comfortable. You look under the sheets and find a yellow slip of paper with the number {vaultCode[vaultCodeOrder.index('yellow')]} on it!")
    roomLayout[bedLocation[0]][bedLocation[1]].addItem("bedstand", "A small table next to the bed.")

    #Living room can appear in any of the top or bottom rooms, as long as it isnt the vault or bedroom
    while (True):
        livingLocation = [random.randint(0, 2), random.randint(0, 2)]
        if (not livingLocation[0] == 1):
            if (not (livingLocation[0] == 0 and livingLocation[1] == bedLocation)):
                if (not (livingLocation[0] == 2 and livingLocation[1] == vaultLocation)):
                    break


    roomLayout[livingLocation[0]][livingLocation[1]].addItem("rug","A bearskin rug")
    roomLayout[livingLocation[0]][livingLocation[1]].addItem("mantle", "A brick mantle with a fireplace")
    roomLayout[livingLocation[0]][livingLocation[1]].addItem("plant", "A large potted plant in the corner. It has shriveled due to a lack of light")

    #Safe can be found anywhere other than the vault
    while (True):
        safeLocation = [random.randint(0, 2), random.randint(0, 2)]
        if (not (safeLocation[0] == 2 and safeLocation[1] == vaultLocation)):
            break
        
    roomLayout[safeLocation[0]][safeLocation[1]].addItem("safe", "A metal safe with a 3 digit lock (use the verb unlock to try and solve it)")

    #miscellaneous items which can be found in any room
    toolBoxLocation = [random.randint(0, 2), random.randint(0, 2)]
    roomLayout[toolBoxLocation[0]][toolBoxLocation[1]].addItem("toolbox", "a toolbox with an assortment of tools. ")

    clockLocation = [random.randint(0, 2), random.randint(0, 2)]
    roomLayout[clockLocation[0]][clockLocation[1]].addItem("clock", "an old grandfather clock. Looks like it has a few loose screws. There may be a way to get inside")

    cageLocation = [random.randint(0, 2), random.randint(0, 2)]
    roomLayout[cageLocation[0]][cageLocation[1]].addItem("cage", "a small bird cage. Theres a lock with a black spherical hole in it")



    #add the grabbbables
    roomLayout[0][keyLocation].addGrabbable("key", "table")
    roomLayout[1][kitchenLocation].addGrabbable("apple", "refrigerator")
    roomLayout[gameLocation[0]][gameLocation[1]].addGrabbable("8ball", "pooltable")
    roomLayout[toolBoxLocation[0]][toolBoxLocation[1]].addGrabbable("crowbar", "toolbox")
    roomLayout[toolBoxLocation[0]][toolBoxLocation[1]].addGrabbable("screwdriver", "toolbox")
    roomLayout[bedLocation[0]][bedLocation[1]].addGrabbable("flashlight", "bedstand")

    #set Locks
    roomLayout[random.randint(1, 2)][random.randint(0, 2)].isLocked = True

    currentRoom = r1

    return currentRoom

def death(deathMessage):
    print(deathMessage)

def removeItemFromInventory(noun):
    for i in range(0, len(inventory)):
        if (inventory[i][0] == noun):
            inventory.pop(i)
            break


def go(noun):
    global currentRoom
    global successfulAction
    response = "Given exit is invalid."
    for i in range(len(currentRoom.exitNames)):
        if (noun == currentRoom.exitNames[i]):
            if (not currentRoom.exits[i].isLocked):
                if (not (currentRoom.items.count("door") > 0 and noun == "north" and (not isExitOpen))):
                    currentRoom = currentRoom.exits[i]
                    try:
                        response = f"You have moved to {currentRoom.name}"
                    except:
                        response = ""
                    successfulAction = True
                    break
                else:
                    response = "The exit is still barricaded!"
            else:
                response = "The room is locked!"
    print(response)


def look(noun):
    global currentRoom
    global successfulAction
    response = "Given item is invalid."
    for i in range(len(currentRoom.items)):
        if (noun == currentRoom.items[i]):
            response = currentRoom.itemDescriptions[i]
            successfulAction = True
            for grabbable in currentRoom.grabbables:
                if (grabbable[1] == noun):
                    response +=  " There is a " + grabbable[0] + " in it. "
            break
    print(response)

            
def take(noun):
    global currentRoom
    global successfulAction
    response = "I don't see that item."
    for grabbable in currentRoom.grabbables:
        if (noun == grabbable[0]):
            inventory.append(grabbable)
            currentRoom.delGrabbable(grabbable)
            response = f"{noun} grabbed."
            successfulAction = True
            break
    print(response)

# Use an item in your inventory
def use(noun):
    global currentRoom
    global successfulAction
    response = "That item is not in your inventory"
    if (noun == "key"):
        response = "There are no locked doors in this rooom"
        for i in range(len(currentRoom.exitNames)):
            if (currentRoom.exits[i].isLocked):
                currentRoom.exits[i].isLocked = False
                removeItemFromInventory(noun)
                response = f"You unlocked the doors to {currentRoom.exits[i].name}"
                successfulAction = True
                break
    
    if (noun == "apple"):
        response = f"You took a bite out of the apple. You found a slip of blue paper with the number {vaultCode[vaultCodeOrder.index('blue')]} on it inside!"
        successfulAction = True

    if (noun == "screwdriver"):
        response = "Theres nothing to use a screwdriver on here"
        if (currentRoom.items.count("clock") > 0):
            response = f"You used the screwdriver to unscrew the loose screws, inside you found a green slip of paper with the number {vaultCode[vaultCodeOrder.index('green')]} on it inside! \nYou screw everything back into place so theres no trace left"
            successfulAction = True

    if (noun == "8ball"):
        response = "The 8 ball doesnt seem to have any use in this room"
        if (currentRoom.items.count("cage") > 0):
            response = f"You placed the 8 ball into the lock's sphereical hole, causing the cage door to swing open. In the cage you found a red slip of paper with the number {vaultCode[vaultCodeOrder.index('red')]} on it! \n Afterwards you close the cage"
            successfulAction = True

    if (noun == "flashlight"):
        response = "You turned on the flashlight and aimed it all around the room. Nothing happened"
        if (currentRoom.items.count("plant") > 0):
            response = f"You turned on the flashlight and aimed it all around the room. When you aimed it at the plant its leaves suddenly unfurrled and revealed a purple slip of paper with the number {vaultCode[vaultCodeOrder.index('purple')]} on it inside! \n The plant then shrivels back to its sad state"
            successfulAction = True

    if (noun == "crowbar"):
        response = "theres nothing important to break in this room"
        if (currentRoom.items.count("door") > 0):
            response = "You smashed the barricades on the door, the exit is now open!"
            global isExitOpen
            isExitOpen = True
            successfulAction = True

    print(response)
    

# attempt to unlock an item such as the safe
def unlock(noun):
    global currentRoom
    global successfulAction
    response = "That item has nothing to unlock"
    if (noun == "safe"):
        while (True):
            successfulAction = True
            inputCode = input("input a 3 digit code: ")
            if (len(inputCode) == 3):
                if (inputCode[0] == str(safeCode[0]) and inputCode[1] == str(safeCode[1]) and inputCode[2] == str(safeCode[2])):
                    response = "Correct Code! The safe unlocked, revealing a white slip of paper with five squares:  \n"
                    for color in vaultCodeOrder:
                        response += "a " + color + " square. " 
                else:
                    response = "Incorrect Code"
                break
            else:
                print("Invalid Code. Use the format [12345], with no spaces between the numbers")

    if (noun == "vault"):
        while (True):
            successfulAction = True
            inputCode = input("input a 5 digit code: ")
            if (len(inputCode) == 5):
                if (inputCode[0] == str(vaultCode[0]) and inputCode[1] == str(vaultCode[1]) and inputCode[2] == str(vaultCode[2]) and inputCode[3] == str(vaultCode[3]) and inputCode[4] == str(vaultCode[4])):
                    response = 'Correct Code! The vault unlocked! Inside you found a giant diamond!:  \nSoon afterwards, an incredibly loud alarm began to play \n "UNAUTHORIZED PERSON HAS OPENED VAULT, SELF DESTRUCTING IN 5 MINUTES" \nLooks like its time to find a way out!'
                    global hasDiamond
                    hasDiamond = True

                else:
                    response = "Incorrect Code"
                break
            else:
                print("Invalid Code. Use the format [12345], with no spaces between the numbers")

    
    print(response)




# ****************
#    MAIN CODE
# ****************
    
safeCode = []
vaultCode = []
vaultCodeOrder = []
currentRoom = createRooms()
inventory = []
successfulAction = True
numOfActions = 0
numOfActionsInEscape = 0
isExitOpen = False
hasDiamond = False


#core game loop
#go back and forth between
#printing the current room
#and receiving and executing input

while (True):
    numOfActions += 1
    if (successfulAction):
        print(currentRoom)
        inventoryDisplay = ""
        for grabbable in inventory:
            inventoryDisplay += grabbable[0] + ", "
        print("You are carrying: \n" + inventoryDisplay)
        successfulAction = False

    action = input("What would you like to do: ")
    action = action.lower()
    words = action.split(" ")
    if (len(words) == 2):
        verb = words[0]
        noun = words[1]
        if (verb == "go"):
            go(noun)
            
        elif (verb == "look"):
            look(noun)
        
        elif (verb == "take"):
            take(noun)
            
        elif (verb == "use"):
            use(noun)

        elif (verb == "unlock"):
            unlock(noun)

        else:
            print("That is not a valid verb. Valid verbs are go, look, take, use, and unlock")
        
    else:
        print("I don't understand. Try the format: [verb noun]. Valid verbs are go, look, take, use, and unlock")


    if (currentRoom == None):
        death("you fell out of a window and died :(")
        break



    if (currentRoom.name == "Escape"):
        if (hasDiamond):
            print("You Luckily managed to escape, and with the Giant Diamond in tow! You're gonna be rich!")
            break
        else:
            print("You managed to escape, but you didnt manage to find any treasure...")
            break

    if (hasDiamond):
        numOfActionsInEscape += 1
        print(f"You have {6 - numOfActionsInEscape} actions left to escape")

    elif (numOfActionsInEscape >= 6):
        death("You didnt make it in time. The building began to combust around you, and in an instant you were gone... \n    GAME OVER   ")
        break