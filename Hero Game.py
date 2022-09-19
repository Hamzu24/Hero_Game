import random as r
import time

inventory = ["the will to live", "e demonic crossbow", "e demonic sword", "l mythical body cloak"]
brawlStats = ['N/A', [15, 17, "small dwarf", 1], [25, 30, "menacing dwarf", 5], [53, 40, "troll", 20], [100, 54, "demonic ogre", 100], [250, 60, "Satanic Abaddon", 1000]]
weaponStats = {"the will to live" : [0, "sword"], "none" : [0, "sword"], "c basic sword" : [2, "sword"], "u double edged sword" : [4, "sword"], "r excalibur" : [8, "sword"], "e demonic sword" : [14, "sword"], "l mythical sword" : [25, "sword"], "c basic shield" : [15, "protection"], "u round shield" : [25, "protection"], "r full body shield" : [38, "protection"], "e impenetrable body armour" : [57, "protection"], "l mythical body cloak" : [80, "protection"], "c rock" : [1, "ranged"], "u crossbow" : [5, "ranged"], "r flaming crossbow" : [10, "ranged"], "e demonic crossbow" : [20, "ranged"], "l mythical crossbow" : [30, "ranged"], "c bandages" : [10, "health"], "u mini shield potions" : [25, "health"], "r slurp juice" : [40, "health"], "e chugg jugg" : [75, "health"], "l infinity heal" : [100, "health"], "c rat poison" : [0, "poison"], "u basic poison" : [-20, "poison"], "r horse poison" : [-75, "poison"], "e demonic poison" : [-100, "poison"], "l dimensoinal droplet" : [0, "poison"]}
equippedWeapons = {"sword" : "none", "ranged" : "none", "protection" : "none"}
rewardLevels = [1, 3, 6, 10, 16, 29, 42, 68, 91, 160, 311, 500, 676, 825, 1698, 2301, 3801, 6001, 7501, 10001]
rarities = ["c", "u", "r", "e", "l"]
name = ""
title = ""
rewardsClaimed = 0
chestItems = 4
traderItems = 5
reputation = 0
defencePoints = 0
attackPoints = 0
health = 100
chestChances = [40, 27.5, 22.5, 7.5, 2.5]
items = [["c basic sword", "c basic shield", "c bandages", "c rat poison", "c rock"], ["u double edged sword", "u round shield", "u mini shield potions", "u basic poison", "u crossbow"], ["r excalibur", "r full body shield", "r slurp juice", "r horse poison", "r flaming crossbow"], ["e demonic sword", "e impenetrable body armour", "e chugg jugg", "e demonic poison", "e demonic crossbow"], ["l mythical sword", "l mythical body cloak", "l infinity heal", "l dimensional droplet", "l mythical crossbow"]]
def start():
    global name, title
    name = input("What's your name?")
    time.sleep(1)
    print("The story of the hero "+name+" started here...")
    title = name+" the irrelevant"
    time.sleep(1)
    menu()

def menu():
    global rewardLevels, rewardsClaimed, reputation
    usrAnswer = ""
    time.sleep(1)
    print("What do you want to do now "+title+"? You can...")
    time.sleep(1)
    print("\nOpen a chest (chest)\nTrade with a local merchant (trade)\nBrawl (brawl)\nManage your inventory (inventory)\nPlay the tutorial (tutorial)")
    if rewardsClaimed != 20:
        usrAnswer = input("(next reputation reward unlocked at "+str(rewardLevels[rewardsClaimed])+" reputation, and you currently have"+str(reputation)+")")
    else:
        usrAnswer = input("All rewards claimed. You have "+str(reputation)+" reputation")
    if usrAnswer == "chest":
        openChest()
    elif usrAnswer == "trade":
        trade()
    elif usrAnswer == "tutorial":
        tutorial()
    elif usrAnswer == "brawl":
        usrAnswer = int(input("What level of brawl do you want to fight? (1 to 5)"))
        brawl(usrAnswer)
    elif usrAnswer == "inventory":
        print("You have these items in your inventory: ")
        printInventory(inventory)
        print("Do you want to...")
        time.sleep(1)
        usrAnswer = input("\nManage (manage) your inventory\nSee all the possible items (items)\nUse an item- healing or poison(use)\nEquip an item- armour/shield or weapons (equip)")
        if usrAnswer == "manage":
            manageInventory()
        elif usrAnswer == "items":
            listItems()
        elif usrAnswer == "use":
            useItem()
        else:
            equip()
def listItems():
    global items
    print("The letter before an item says its rarity (c : common, u : uncommon, r : rare, e : epic, l : legendary).\nThese are all the possible items in the game: \n")
    for i in range(0, 5):
        for x in range(0, 5):
            if x == 4:
                print(items[i][x]+"\n")
            else:
                print(items[i][x]+", ")
    time.sleep(1)
    menu()

def useItem():
    global inventory, weaponStats, health
    usrAnswer = ""
    selectedItem = ""
    usrAnswer = input("what is the name of the item you want to use from your inventory?\n(Maximum health is 100)")
    possessionOfItem = False
    for i in inventory:
        if i == chance:
            possessionOfItem = True
    if possessionOfItem == True:
        print("you don't possess that item...")
    else:
        selectedItem = weaponStats.get(usrAnswer)
        if selectedItem[1] == "health" or selectedItem[1] == "poison":
            if chance == "c rat poison":
                print("You get a slight stomach ache and feel stupid...")
            elif chance == "l dimensional droplet":
                print("You ascend to a higher dimension, and forget all of your earthly troubles...")
                exit()
            else:
                health = health + selectedItem[0]
                print("You now have "+str(health)+" health...")
            deathCheck()
            health = healthCheck(health)
            inventory.remove(chance)
        else:
            print("That item cannot be used in this way")
    menu()

def manageInventory():
    global inventory
    deleting = False
    usrAnswer = ""
    selectedItem = ""
    print("Do you want to...")
    time.sleep(1)
    usrAnswer = input("\nRemove (r) an item\nOr delete all of one rarity of item in your inventory (rr)")
    if usrAnswer == "r":
        deleting = True
        while deleting == True:
            usrAnswer = input("What is the name of the item you want to delete (say the EXACT name of the item)?")
            if usrAnswer == "the will to live":
                exit()
            inventory.remove(usrAnswer)
            time.sleep(1)
            print("Your new inventory looks like this: ")
            printInventory(inventory)
            time.sleep(1)
            deleting = input("Do you want to remove more items? (y or n)")
            if deleting == "y":
                deleting = True
            else:
                deleting = False
        menu()
    else:
        print("What rarity of item do you want to delete? Say the first letter (eg. c, u, r, etc.)")
        usrAnswer = input("However be warned, once you do this, there is no going back...\nto cancel just type cancel")
        time.sleep(1)
        if usrAnswer == "cancel":
            menu()
        else:
            itemsToBeDeleted = []
            for i in range(0, len(inventory)):
                selectedItem = inventory[i]
                if selectedItem[0:1] == usrAnswer:
                    itemsToBeDeleted.append(selectedItem)
            for i in itemsToBeDeleted:
                inventory.remove(i)
            time.sleep(1)
            print("Your new inventory looks like this: ")
            printInventory(inventory)
            time.sleep(1)
            menu()

def equip():
    global equippedWeapons, health, weaponStats, attackPoints, defencePoints
    print("At the moment, these are your stats: ")
    time.sleep(1)
    print("Attack: "+str(attackPoints)+", equipped "+equippedWeapons.get("sword")+" as sword and "+equippedWeapons.get("ranged")+" as ranged")
    print("Defence: "+str(defencePoints)+", equipped "+equippedWeapons.get("protection"))
    print("Health: "+str(health))
    equipping = True
    usrAnswer = ""
    selectedItem = ""
    time.sleep(1)
    while equipping == True:
        usrAnswer = input("Which aspect of your loadout do you want to edit (sword, ranged or protection)? (type s, r or p)")
        if usrAnswer == "s":
            usrAnswer = input("What item in your inventory do you want to replace it with? (say the EXACT name)")
            selectedItem = equippedWeapons.get("sword")
            if weaponStats.get(usrAnswer)[1] == "sword":
                attackPoints = attackPoints - weaponStats.get(selectedItem)[0]
                equippedWeapons["sword"] = usrAnswer
                attackPoints = attackPoints + weaponStats.get(usrAnswer)[0]
                time.sleep(1)
                print("You now have "+str(attackPoints)+" attack points...")
            else:
                print("This item cannot be used in this way...")
        elif usrAnswer == "r":
            usrAnswer = input("What item in your inventory do you want to replace it with? (say the EXACT name)")
            selectedItem = equippedWeapons.get("ranged")
            if weaponStats.get(usrAnswer)[1] == "ranged":
                attackPoints = attackPoints - weaponStats.get(selectedItem)[0]
                equippedWeapons["ranged"] = usrAnswer
                attackPoints = attackPoints + weaponStats.get(usrAnswer)[0]
                time.sleep(1)
                print("You now have "+str(attackPoints)+" attack points...")
            else:
                print("This item cannot be used in this way...")
        else:
            usrAnswer = input("What item in your inventory do you want to replace it with? (say the EXACT name)")
            selectedItem = equippedWeapons.get("protection")
            if weaponStats.get(usrAnswer)[1] == "protection":
                defencePoints = defencePoints - weaponStats.get(selectedItem)[0]
                equippedWeapons["protection"] = usrAnswer
                defencePoints = defencePoints + weaponStats.get(usrAnswer)[0]
                time.sleep(1)
                print("You now have "+str(defencePoints)+" defence points...")
            else:
                print("This item cannot be used in this way...")
        time.sleep(1)
        equipping = input("Do you want to continue equipping? (y or n)")
        if equipping == "y":
            equipping = True
        else:
            equipping = False
    menu()

def healthCheck(health):
    if health > 100:
        health = 100
    return health

def deathCheck():
    global health
    if health <= 0:
        print("You died!")
        exit()

def reputationCheck():
    global rewardsClaimed, name, title, reputation, defencePoints, attackPoints, chestItems, traderItems
    time.sleep(1)
    if reputation > 0 and rewardsClaimed == 0:
        print("You have earned a reputation reward!")
        time.sleep(1)
        print("You title is now: \n"+name+" the weak")
        title = name+" the weak"
        rewardsClaimed = rewardsClaimed + 1
    if reputation > 2 and rewardsClaimed == 1:
        print("You have earned a reputation reward!")
        time.sleep(1)
        print("You have earned the perk hardened skin\nYour defence points have been permanently increased by 2")
        defencePoints = defencePoints + 2
        rewardsClaimed = rewardsClaimed + 1
    if reputation > 5 and rewardsClaimed == 2:
        print("You have earned a reputation reward!")
        time.sleep(1)
        print("Your title is now:\n"+name+" the energetic")
        title = name+" the energetic"
        rewardsClaimed = rewardsClaimed + 1
    if reputation > 9 and rewardsClaimed == 3:
        print("You have earned a reputation reward!")
        time.sleep(1)
        print("Chests now provide four items instead of just three!")
        chestItems = 4
        rewardsClaimed = rewardsClaimed + 1
    if reputation > 15 and rewardsClaimed == 4:
        print("You have earned a reputation reward!")
        time.sleep(1)
        print("You have earned the perk permanently angry\nYour attack points have been permanently increased by 3")
        attackPoints = attackPoints + 3
        rewardsClaimed = rewardsClaimed + 1
    if reputation > 28 and rewardsClaimed == 5:
        print("You have earned a reputation reward!")
        time.sleep(1)
        print("Your title is now:\n"+name+" the muscular")
        title = name+" the muscular"
        rewardsClaimed = rewardsClaimed + 1
    if reputation > 41 and rewardsClaimed == 6:
        print("You have earned a reputation reward!")
        time.sleep(1)
        print("Traders now provide five items instead of just four!")
        traderItems = 6
        rewardsClaimed = rewardsClaimed + 1
    if reputation > 67 and rewardsClaimed == 7:
        print("You have earned a reputation reward!")
        time.sleep(1)
        print("You have earned the perk big boned\nYour defence points have been permanently increased by 5")
        defencePoints = defencePoints + 5
        rewardsClaimed = rewardsClaimed + 1
    if reputation > 90 and rewardsClaimed == 8:
        print("You have earned a reputation reward!")
        time.sleep(1)
        print("Your title is now:\n"+name+" the relentless")
        title = name+" the relentless"
        rewardsClaimed = rewardsClaimed + 1
    if reputation > 159 and rewardsClaimed == 9:
        print("You have earned a reputation reward!")
        time.sleep(1)
        print("You have earned the perk crazily confident\nYour attack points have been permanently increased by 6")
        attackPoints = attackPoints + 6
        rewardsClaimed = rewardsClaimed + 1
    if reputation > 310 and rewardsClaimed == 10:
        print("You have earned a reputation reward!")
        time.sleep(1)
        print("Chests now provide five items instead of just four!")
        chestItems = 5
        rewardsClaimed = rewardsClaimed + 1
    if reputation > 499 and rewardsClaimed == 11:
        print("You have earned a reputation reward!")
        time.sleep(1)
        print("Your title is now "+name+" the feared")
        title = name+" the feared"
        rewardsClaimed = rewardsClaimed + 1
    if reputation > 675 and rewardsClaimed == 12:
        print("You have earned a reputation reward!")
        time.sleep(1)
        print("Traders now provide six items instead of just five!")
        traderItems = 7
        rewardsClaimed = rewardsClaimed + 1
    if reputation > 824 and rewardsClaimed == 13:
        print("You have earned a reputation reward!")
        time.sleep(1)
        print("You have earned the perk kung fu training\nYour attack points have been permanently increased by 4")
        attackPoints = attackPoints + 4
        rewardsClaimed = rewardsClaimed + 1
    if reputation > 1697 and rewardsClaimed == 14:
        print("You have earned a reputation reward!")
        time.sleep(1)
        print("Your title is now "+name+" the omnipotent")
        title = name+" the omnipotent"
        rewardsClaimed = rewardsClaimed + 1
    if reputation > 2300 and rewardsClaimed == 15:
        print("You have earned a reputation reward!")
        time.sleep(1)
        print("Chests now provide seven items instead of just five!")
        chestItems = 7
        rewardsClaimed = rewardsClaimed + 1
    if reputation > 3800 and rewardsClaimed == 16:
        print("You have earned a reputation reward!")
        time.sleep(1)
        print("Traders now provide eight items instead of just six!")
        traderItems = 9
        rewardsClaimed = rewardsClaimed + 1
    if reputation > 6000 and rewardsClaimed == 17:
        print("You have earned a reputation reward!")
        time.sleep(1)
        print("You have earned the perk insanely muscular\nYour attack points have been permanently increased by 25")
        attackPoints = attackPoints + 25
        rewardsClaimed = rewardsClaimed + 1
    if reputation > 7500 and rewardsClaimed == 18:
        print("You have earned a reputation reward!")
        time.sleep(1)
        print("You have earned the perk godly reflexes\nYour defence points have been permanently increased by 6")
        defencePoints = defencePoints + 6
        rewardsClaimed = rewardsClaimed + 1
    if reputation > 10000 and rewardsClaimed == 19:
        print("You have earned the final reputation reward...")
        time.sleep(2)
        print("Your title is now\n"+name+" the sweat")
        title = name+" the sweat"
        rewardsClaimed = rewardsClaimed + 1
    time.sleep(1)

def openChest():
    global chestItems, rarities, inventory
    usrAnswer = ""
    selectedItem = ""
    rarityChance = 0
    usrAnswer = input("Do you want to accept all items, or only items above a certain rarity\n(eg. for only uncommon or better rarity items type u, for items of all rarities type c)")
    for i in range(1, chestItems):
        rarityChance = r.randint(0, 100)
        if rarityChance < 40:
            rarityChance = 0
        elif rarityChance < 67.5:
            rarityChance = 1
        elif rarityChance < 90:
            rarityChance = 2
        elif rarityChance < 97.5:
            rarityChance = 3
        else:
            rarityChance = 4
        if rarityChance >= rarities.index(usrAnswer):
            selectedItem = items[rarityChance][r.randint(0, 4)]
            print("You got...")
            time.sleep(1)
            print("A "+selectedItem+"!")
            inventory.append(selectedItem)
            time.sleep(1)
        else:
            print("Item discarded due to low rarity...")
            time.sleep(1)
    print("The chest has been emptied!")
    menu()
   
def trade():
    global traderItems, inventory, items
    traderInventory = []
    usrAnswer = ""
    selectedIndex = 0
    for i in range(1, traderItems):
        selectedItem = items[r.randint(0, 4)][r.randint(0, 4)]
        traderInventory.append(selectedItem)
    time.sleep(1)
    print("The AI has these items in his inventory: ")
    printInventory(traderInventory)
    trading = True
    while trading == True:
        usrAnswer = input("Do you want to trade with this person more? (y or n)")
        if usrAnswer == "y":
            printInventory(inventory)
            usrAnswer = int(input("What item in your inventory do you want to lose? (say the index of the item) - You can only trade items of the same rarity... "))
            time.sleep(1)
            selectedIndex = int(input("What item do you want from the trader? (say the index)"))
            if inventory[usrAnswer][:1] == traderInventory[selectedIndex][:1]:
                inventory.pop(usrAnswer)
                inventory.insert(usrAnswer, traderInventory[selectedIndex])
                traderInventory.pop(selectedIndex)
            else:
                print("These items are not of the same rarity!")
            time.sleep(1)
            print("Your inventory looks like this: ")
            printInventory(inventory)
            time.sleep(1)
        else:
            trading = True
    time.sleep(1)
    print("The trader is never seen again...")
    menu()

def brawl(level):
    global equippedWeapons, health, inventory, attackPoints, defencePoints, brawlStats, reputation
    time.sleep(1)
    print("You enter the arena, and see a "+brawlStats[level][2]+" standing in the centre...")
    time.sleep(r.randint(1, 3))
    print("You finally build up your courage, and enter the arena...")
    AIhealth = brawlStats[level][0]
    time.sleep(0.5)
    print("Upon observation you can see that the enemy has:\n"+str(brawlStats[level][0])+" health\n"+str(brawlStats[level][1])+" defence points")
    time.sleep(1)
    while AIhealth > 0 and health > 0:
        chance = int(input("You can either go for an uppercut, jab or a block (1, 2 or 3)"))
        chance2 = r.randint(1, 3)
        if chance == 3 and chance2 == 2:
            print("You block his jab, and swiftly counterattack!")
            chance = 1
        elif chance == 2 and chance2 == 1:
            print("He swings for an uppercut, but you quickly jab him!")
            chance = 1
        elif chance == 1 and chance2 == 3:
            print("He tries to block, but you uppercut under his defences!")
            chance = 1
        elif chance == 2 and chance2 == 3:
            print("He blocks your jab, and manages to land a punch...")
            chance = 2
        elif chance == 1 and chance2 == 2:
            print("You swing for an uppercut, but he dazes you with a jab...")
            chance = 2
        elif chance == 3 and chance2 == 1:
            print("You try to block, but he uppercuts under your arms...")
            chance = 2
        else:
            chance == 3
        time.sleep(0.5)
        if chance == 1:
            chance = r.randint(1, 100)
            if chance >= brawlStats[level][1]:
                chance2 = r.randint(1, 7)
                if chance2 == 6:
                    damageTaken = (attackPoints*2)+r.randint(-3, 3)
                    AIhealth = AIhealth - selectedItem
                    print("An amazing blow topples him to the floor!\nHe takes "+str(damageTaken)+" points of damage, leaving his health at "+str(AIhealth))
                else:
                    selectedItem = attackPoints+r.randint(-3, 3)
                    AIhealth = AIhealth - selectedItem
                    print("The blow does "+str(selectedItem)+" points of damage leaving him with "+str(AIhealth)+" health")
            else:
                print("Your attack harmlessly bounces off of his defences...")
        elif chance == 2:
            chance = r.randint(1, 100)
            if chance >= defencePoints:
                selectedItem = (level*2)*r.randint(1, level)
                health = health - selectedItem
                print("His blow does "+str(selectedItem)+" points of damage, leaving your health at "+str(health))
            else:
                print("His attack bounces harmlessly off of your defences...")
        elif chance == 3:
            print("You both go for the same attack, confusing eachother and eventually backing off...")
        time.sleep(0.5)
    if health > 0:
        print("You won the brawl! He is sprawled across the floor, defeated.")
        itemWon = ""
        itemWon = items[level][r.randint(0, 4)]
        inventory.append(itemWon)
        time.sleep(1)
        print("You also won a "+itemWon+" from the brawl!")
        time.sleep(1)
        reputation = reputation + brawlStats[level][3]
        print("You also gained "+str(brawlStats[level][3])+" reputation, leaving you with "+str(reputation)+" reputation")
        time.sleep(1)
        reputationCheck()
        menu()
    else:
        print("You were defeated in a brawl...")
        exit()

def printInventory(array):
    global health, equippedWeapons, weaponStats
    print(str(health)+" health")
    trading = 0
    counter = 0
    listingInventory = [[], [], [], [], []]
    specifiedStats = []
    for i in range(0, len(array)):
        if array[i] != 'the will to live':
            specifiedStats = weaponStats.get(array[i])
            if specifiedStats[1] == "sword":
                listingInventory[0].append(array[i])
            elif specifiedStats[1] == "protection":
                listingInventory[1].append(array[i])
            elif specifiedStats[1] == "health":
                listingInventory[2].append(array[i])
            elif specifiedStats[1] == "poison":
                listingInventory[3].append(array[i])
            elif specifiedStats[1] == "ranged":
                listingInventory[4].append(array[i])
    for i in listingInventory:
        if counter == 0:
            print("\nSwords:")
        elif counter == 1:
            print("\nProtection:")
        elif counter == 2:
            print("\nHealth:")
        elif counter == 3:
            print("\nPoison:")
        elif counter == 4:
            print("\nRanged:")
        if i == []:
            print("None")
        for j in i:
            if j == equippedWeapons.get("sword") or j == equippedWeapons.get("protection") or j == equippedWeapons.get("ranged"):
                j = j+" EQUIPPED"
            print(j)
        counter = counter + 1
    print("\n")

def tutorial():
    time.sleep(1)
    input("In this hero game, the aim of the game is to get the best equipment, and beat the hardest brawls")
    input("From the main menu you can do lots of things, but to get your first weapons you have to open chests")
    input("You get three items from chests. Items can have different rarities, shown by a letter at the start of the item name:\nCommon (c)\nUncommon (u)\nRare (r)\nEpic (e)\nLegendary (l)")
    input("The rarer the item, the more it does for you")
    input("Along with this, there are five classes of items:\nSwords\nProtection (shields and armour)\nHealing items\nPoison\nRanged")
    input("Your hero has two main combat stats: combat points and defence points.")
    input("Your combat points determine the average amount of damage you will inflict on an opponent\nIt is the combination of your equipped ranged weapon damage and your equipped sword damage")
    input("Your defence points determine what percentage of chance you will have of defending your foe's attacks (eg. 35 = 35% chance of blocking an attack)")
    input("You can change the items you have equipped from the equip option in the inventory menu")
    input("Even if you delete an equipped item from your inventory, it will still be equipped\nHowever when you equip a different item it will be permanently lost")
    input("You can also manage your inventory from this menu\n(deleting an item, sorting your inventory and deleting all of one rarity of item in your inventory (eg. common, rare, etc.))")
    input("Finally, from the inventory menu you can use items. You can use both poisons and health items (although poisons damage your health)\nIt is advised that you heal after a brawl to regain your lost health")
    input("You can also trade. You can trade for any item from a trader as long as the items are both of the same rarity")
    input("The final thing that needs to be explianed is reputation")
    input("Reputation is earned from completing brawls. The harder the brawl, the more reputation earned")
    input("Brawls are fought like a game of rock, paper scisssors, however with jabs, uppercuts and blocks.\nThere is an element of luck")
    input("Once you enter a brawl, however, there is no backing down... ...and once your health reaches zero, all your progress is lost...")
    input("But gaining reputation unlocks a multitude of perks, such as better chests, better traders, titles and perks")
    input("Note: poisons exist solely to decrease the player's health, and serve no combat function")
    time.sleep(1)
    input("You have now completed the tutorial! Press enter to go to the main menu")
    menu()
    

start()
