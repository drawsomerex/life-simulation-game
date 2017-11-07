import os,random
f = open('game_output.txt', 'w')
playerYear = 0
bankAccount = random.randint(1,500)
stockMarketIndex = True
stockMarketAccount = random.randint(1,500)
playerDeathIndex = playerYear
playerSavings = .5
playerStock = .1
playerLiving = True
wifeLiving = True
playerMorgage = 0
bankruptcyCount = 0
gameOngoing = True
homeowner = False
salary = 30326
costOfLiving = 24749
homePrice = 365300
timeMarried = 0
morgageRate = 4.176
morgageTermMonths = 30
welfareStatus = False
homePaidFor = False
wifeCount = 0
yearsOnWelfare = 0
welfareTotal = 0
playerWidower = False
marriedState = False
playerName = "James" #input("Input your name:")
f.write("Hello " + playerName + ". You were born in Oregon to loving parents who put $" + str(bankAccount) + " in a bank account for you and invested " + str(stockMarketAccount) + " in the stock market for you.")
def deathCheck (check): #figure this junk out!
        if check < 50:
                playerDead = random.randint(1,1000) #1% chance of dying each year
        elif 50 <= check <= 78:
                playerDead = random.randint(1,50) #2% chance of dying each year after 50
        elif 78 <= check <= 100:
                playerDead = random.randint(1,10) #10% chance of dying each year after 78
        elif 100 <= check <= 120:
                playerDead = random.randint(1,2) #50% chance of dying each year after 78
        elif check >= 120:
                playerDead = 1        
        if playerDead == 1:
                return False
        else:
                return True 
def marriage():
        global wifeAge, playerYear, marriedState, wifeCount, costOfLiving
        chance = random.randint(1,5)
        if chance == 3:
                marriedState = True
                costOfLiving *= 1.25
                wifeCount += 1
                ageDiff = random.randint(1,10)
                upDown = random.choice([True,False])
                if upDown == True:
                        if playerYear <= 28:
                                 wifeAge = 18
                        elif playerYear >  28:
                                wifeAge = playerYear - ageDiff
                elif upDown == False:
                        wifeAge = playerYear + ageDiff
                timeMarried = 0
                print("You married wife #" + str(wifeCount) + ", who is a beautiful " + str(wifeAge) + " year old woman. You are quite pleased.")                                              
def jobMarket():
        global salary
        jobChoice = random.randint(1,3)
        if jobChoice == 1:
                salary *= .90
                print("You have gotten a bad job")
        if jobChoice == 2:
                salary *= 1
                print("You have gotten an average job")
        if jobChoice == 3:
                salary *= 1.25
                print("You have gotten a good job")
def playerStats():
        global salary
        playerIntelligence = random.randint(1,3)
        if playerIntelligence == 1:
                salary *= .90
                print("You are dumb.")
        if playerIntelligence == 2:
                salary *= 1
                print("You are normal intelligence.")
        if playerIntelligence == 3:
                salary *= 1.25
                print("You are smart. Congratulations, things are easier for you.")        
def randomActsOfProvidence():
        global bankAccount
        count = random.randint(1,100)
        if 1 <= count <= 10:
                disaster = random.randint(50,1000)
                bankAccount -= disaster
                print("You have suffered a setback of $" + str(disaster))
        if 11 <= count <= 20:
                disaster = random.randint(50,1000)
                bankAccount += disaster
                print("You have an unexpected windfall of $" + str(disaster))
        if count == 99:
                disaster = random.randint(1000,10000)
                bankAccount -= disaster
                print("You have suffered a major disaster and lost $" + str(disaster))
        if count == 100:
                disaster = random.randint(1000,10000)
                bankAccount += disaster
                print("You have struck the jackpot and got a windfall of $" + str(disaster))                                           
def StockMarket():
        global stockMarketIndex, stockMarketAccount
        stockMarketIndex = random.choice([True, False])  # stock market either goes up or down
        if stockMarketIndex == True:
                stockMarketAccount *= 1.25
        else:
                stockMarketAccount *= .75
def SharePriceSimulator(check): # not yet implimented
                upDown = random.randrange(-75,75,1)
                upDown = (upDown/100) + 1
                check *= upDown
                return check
def homeOwnership():
        global homeowner, homePaidFor, playerMorgage, bankAccount, stockMarketAccount, costOfLiving, morgagePayment, moragePaidAge
        if homeowner == True:
                if homePaidFor == False:
                        if playerMorgage > 0:
                                if bankAccount > morgagePayment:
                                        bankAccount -= morgagePayment
                                        playerMorgage -= morgagePayment
                                        print("You have paid your morgage.")
                                elif stockMarketAccount > morgagePayment:
                                        stockMarketAccount -= morgagePayment
                                        playerMorgage -= morgagePayment
                                else:
                                        print("You cannot afford to keep your house.")
                                        homeowner = False
                        elif playerMorgage <= 0:
                                print("You have paid off your morgage!")
                                homePaidFor = True
                                moragePaidAge = playerYear
        if bankAccount >= (homePrice/10): #if you have as much as downpayment of homePrice
                if homeowner == False:
                        print ("You put $" + str((homePrice/10)) + " down on a house. You are now a homeowner!")
                        homeowner = True
                        bankAccount -= (homePrice/10)
                        playerMorgage = (homePrice - (homePrice/10))
                        monthly_rate = morgageRate / 100 / 12
                        morgagePayment = (monthly_rate / (1 - (1 + monthly_rate) ** (-morgageTermMonths))) * homePrice
                        costOfLiving -= morgagePayment                
def banking():
        global stockMarketAccount, bankAccount, bankruptcyCount, costOfLiving, welfareStatus
        if stockMarketAccount >= 500: #if you have more than $500 invested save some
                transferFunds = stockMarketAccount * playerSavings
                stockMarketAccount -= transferFunds
                bankAccount += transferFunds
                print ("You saved:$" + str('${:,.2f}'.format(transferFunds)))
        elif bankAccount >= 500: #if you have more than $500 in savings, invest some
                transferFunds = bankAccount * playerStock
                bankAccount -= transferFunds
                stockMarketAccount += transferFunds
                print ("You invested:$" + str('${:,.2f}'.format(transferFunds)))
        elif bankAccount <= 0:
                print("You have gone bankrupt. You are now living on welfare")
                bankAccount = 0
                welfareStatus = True
                yearsOnWelfare = 0
                stockMarketAccount = 0
                bankruptcyCount += 1
def welfareSystem():
        global costOfLiving, welfareStatus, bankAccount, yearsOnWelfare, welfareTotal
        if welfareStatus == True:
                if bankAccount > costOfLiving:
                        welfareStatus = False
                        print("You are financially stable for now and have gone off welfare")
                bankAccount += (costOfLiving * .3)
                yearsOnWelfare += 1
                welfareTotal += (costOfLiving * .3)
                print("You received $" + str(int(costOfLiving * .2)) + " in welfare.")
def stats():
        global totalFunds, stockMarketAccount, bankAccount, deadWifeAge, wifeCount
        totalFunds = stockMarketAccount + bankAccount
        print("Your name is " + playerName)
        print("You are aged " + str(playerYear))
        print("Your bank account:" + str('${:,.2f}'.format(bankAccount)))
        print("Your stock market account:" + str('${:,.2f}'.format(stockMarketAccount)))
        if bankruptcyCount >= 1:
                print("You have gone bankrupt " + str(bankruptcyCount) + " times.")
                print("You were on welfare for " + str(yearsOnWelfare) + " years and received a total of $" + str(int(welfareTotal)) + ".")
        if homeowner == True:
                if homePaidFor == False:
                        print("You are a homeowner!")
                elif homePaidFor == True:
                        print("You paid off your morgage at age:" + str(moragePaidAge))
        elif homeowner == False:
                print("Unfortunately, you are a renter.")
        if marriedState == True:
                if playerWidower == True:
                        print("Your beloved wife #" + str(wifeCount) + " died at the age of " + str(deadWifeAge) + "You were married for " + str(timeMarried))
                elif playerWidower == False:
                        print("Your beloved wife #"+ str(wifeCount) + " is " + str(wifeAge) + " years old and looks to have lots of life still ahead of her. You were married for " + str(timeMarried) + " years.")        
def ageAYear():
        global playerWidoer, timeMarried, moragePaidAge, deadWifeAge, marriedState, wifeLiving, wifeAge, salary, playerYear, bankAccount, stockMarketIndex, stockMarketAccount, homeowner, playerMorgage, morgagePayment, costOfLiving, homePaidFor
        playerLiving = deathCheck(playerYear)
        if marriedState == True:
                wifeLiving = deathCheck(wifeAge)
                wifeAge += 1
                timeMarried += 1
        if playerLiving == False:
                gameEnd()
        if wifeLiving == False:
                if marriedState == True:
                        print("Unfortunately, beloved wife #" + str(wifeCount) + " died at the age of " + str(wifeAge) + ". You were married for " + str(timeMarried) + " wonderful years.")
                        costOfLiving *= .75
                        deadWifeAge = wifeAge
                        timeMarried = 0
                marriedState = False
                playerWidower = True
        playerYear += 1
        if playerYear >= 18:
                if playerYear == 18:
                        jobMarket()
                        playerStats() 
                bankAccount += salary
                bankAccount -= costOfLiving
                randomActsOfProvidence()
                if marriedState == False:
                        marriage()
        bankAccount *= 1.0125
        StockMarket()
        welfareSystem()
        homeOwnership()
        banking()
        print("You are aged " + str(playerYear) + " years.")
        #stats() # for debuging
def finances():
        global playerSavings, playerStock
        menuChoice = input("1. Conservative 2. Risky")
        if menuChoice == "1":
                playerSavings = .2
                playerStock = .2
        if menuChoice == "2":
                playerSavings = .1
                playerStock = .5
def menu():
        menuChoice = input("1. View Stats 2. Advance a Year")
        if menuChoice == "1":
                stats()
        elif menuChoice == "2":
                ageAYear()
        else:
                print("Sorry, that isn't an option.")
                menu()
def gameEnd():
        global gameOngoing
        print("You have died.")
        gameOngoing = False
        stats()
while gameOngoing:
        ageAYear() #menu() #For the same of simulation
