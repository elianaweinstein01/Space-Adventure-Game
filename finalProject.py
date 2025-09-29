# "I hereby certify that this program is solely the result 
# of my own work and is in compliance with the Academic Integrity 
# policy of the course syllabus and the academic integrity policy 
# of the CS department.”

import random
import Draw

#canvas dimentions
STRIPWIDTH = 100000 #length of the whole game
WINDOWWIDTH = 700 #x of the screen
WINDOWHEIGHT = 500 #y of the screen

#amount of items
NUMSTARS = 40000 #amount of stars
NUMASTEROID = 740 #amount of asteroids
NUMGOLD = 15 #amount of gold
NUMSHEILD = 15 #amount of immunity shields
NUMMONSTER = 100 #amount of monsters in the game 

#ship coordinates 
SHIPX = 20 #ship x never changes

#sizes
SHIPSIZE = 100 #size of the ship
ASTEROIDSIZE = 50 #size of asteroids
LASERWIDTH = 300 #laser width
LASERHEIGHT = 10 #laser height

#initialize canvas
def createCanvas():
	Draw.setCanvasSize(WINDOWWIDTH, WINDOWHEIGHT)
	Draw.setBackground(Draw.BLACK) 

#creating 2D lists with items string, location on the strip and a Boolian value to determine if it got hit
def createThings():
	starList = [] #list of stars
	asteroidList = [] #list of asteroids
	goldList = [] #list of special gold
	shieldList = [] #list of shields
	monsterList = [] #list of monsters
	
	#starList[4] determines what size the star is. 
	for i in range (NUMSTARS):
		starList += [["star",random.randint(1, STRIPWIDTH), random.randint(0, WINDOWWIDTH), False, random.randint(2, 4)]]

	#random.choice because I only want them to appear in those specific columns 
	for i in range (NUMASTEROID):
		asteroidList += [["asteroid",random.randint(800, STRIPWIDTH), random.choice([25, 125, 225, 325, 425]), False]] 
	
	for i in range (NUMGOLD): 
		goldList += [["gold",random.randint(800, STRIPWIDTH), random.choice([20, 120, 220, 320, 420]), False]]
	
	for i in range (NUMSHEILD): 
		shieldList += [["shield",random.randint(800, STRIPWIDTH), random.choice([20, 120, 220, 320, 420]), False]]
	
	#monsterList[4] determines which monster it will be 
	for i in range (NUMMONSTER):
		monsterList += [["monster",random.randint(800, STRIPWIDTH), random.choice([20, 120, 220, 320, 420]), False, random.choice(["greenMonster.gif", "redMonster.gif"])]]	
	
	#returns all of the lists of things	
	return starList, asteroidList, goldList, shieldList, monsterList

#all of the hit functions are basically the same format. 
# if it hasent been hit before 
# and the items x - windowX is <= the other items x + its size 
# and the items x - windowx + its size is >= the other items x 
# and the items y + its size is >= the other items y
# and the items y is <= the other items size + its size
# it will return a string.

#if the ship and the asteroid overlap
#input: asteroid list, shipY, windowX and the boolean variable that determines if the shield is applied
def getHit(asteroids, shipY, windowX, applyShield):
	for asteroid in asteroids: 
		if (asteroid[3] == False 
		   and asteroid[1] - windowX <= SHIPX + SHIPSIZE 
		   and asteroid[1] - windowX + ASTEROIDSIZE >= SHIPX 
		   and asteroid[2] + ASTEROIDSIZE >= shipY 
		   and asteroid[2] <= shipY + 80 
		   and applyShield == False): 
			#the asteroid is now Hit and cant be hit again
			asteroid[3] = True 
			#returns the word asteroid which indicates that the ship has been hit by an asteorid
			return "asteroid" 
		
#if the ship and the gold overlap
#input: gold list, shipY and windowX
def getHitGold(gold, shipY, windowX):
	for g in gold: 
		if (g[3] == False 
		   and g[1] - windowX <= SHIPX + SHIPSIZE 
		   and g[1] - windowX + ASTEROIDSIZE >= SHIPX 
		   and g[2] + ASTEROIDSIZE >= shipY 
		   and g[2] <= shipY + SHIPSIZE): 
			#the gold is now hit and can't be hit again
			g[3] = True 
			#returns the word gold which indicates that a live has been collected
			return "gold" 

#if the ship and the shield overlap
#input: shield list, shipY, and windowX
def getHitShield(shields, shipY, windowX):
	for s in shields:
		if (s[3] == False 
		    and s[1] - windowX <= SHIPX + SHIPSIZE 
		    and s[1] - windowX + ASTEROIDSIZE >= SHIPX 
		    and s[2] + ASTEROIDSIZE >= shipY 
		    and s[2] <= shipY + SHIPSIZE): 
			#the shield is now Hit and cant be hit again
			s[3] = True 
			#returns the word shield which indicates that a shield has been collected
			return "shield" 

#if the ship and the monster overlap
#input: monster list, shipY, and windowX, and if the shield is applied		
def getHitMonster(monsters, shipY, windowX, applyShield):
	for m in monsters: 
		if (m[3] == False 
		    and m[1] - windowX <= SHIPX + SHIPSIZE 
		    and m[1] - windowX + ASTEROIDSIZE >= SHIPX 
		    and m[2] + ASTEROIDSIZE >= shipY 
		    and m[2] <= shipY + SHIPSIZE
		    and applyShield == False): 
			m[3] = True 
			#returns the word monster which indicates that a monster has been hit
			return "monster" 

#if the laser hits the monster
#input: monster list, windowX, the lasers X coordinate, the ships Y coordinate, if laser is activated			
def getHitLaser(monsters, windowX, laserX, shipY, shoot):
	for m in monsters:
		#if the laser is activated and the mosnter hasent been hit yet
		if (m[3] == False and shoot == True 
		    and m[1] - windowX <= laserX + LASERWIDTH 
		    and m[1] - windowX + SHIPSIZE >= laserX 
		    and m[2] + SHIPSIZE >= shipY + 50 
		    and m[2] <= shipY + 50 + LASERHEIGHT): 
			m[3] = True 
			#returns the word laser which indicates that a monster has been hit
			return "laser"

#start screen with stars in the back and start button		
def pressStartScreen(stars):
	# x and y coordinate of the mouse
	newKey = 0 
	starWindowX = 0
	
	while True:
		#draws the stars moving on the screen
		Draw.clear() 
		starWindowX += 3
		for star in stars: 
			#if the star is within the screen
			if star[1] >= starWindowX - star[4] and star[1] <= starWindowX + WINDOWWIDTH:
				Draw.setColor(Draw.YELLOW)
				Draw.filledRect(star[1] - starWindowX, star[2], star[4], star[4])
		#draws the start button
		Draw.picture("pressStart.gif", 110, 220) 
		Draw.show()
		
		#press the space bar or the return key to continue
		if Draw.hasNextKeyTyped():
			newKey = Draw.nextKeyTyped()
		if newKey == "Return" or newKey == "space":
			Draw.clear()
			#ends the loop, continues to choose your charecter 
			return	

#prompting user to choose their charecter 		
def pickAlienChar():
	#x and y coordinates of the mouse
	curX = 0 
	curY = 0
	tracker = 0
	
	while True:
		#fixes bug where it chooses an alien if you accidently clicked before
		tracker += 1
		#choose a charecter text
		Draw.picture("choose.gif", 55, 100)
		
		#displays all the aliens 
		Draw.picture("pinkAlien.gif", 75, 250) 
		Draw.picture("redAlien.gif", 225, 250)
		Draw.picture("purpleAlien.gif", 375, 250)
		Draw.picture("rickMorty.gif", 525, 250)
		
		#get mouse x and y coordinates and if the tracker is greater than 10
		if Draw.mousePressed() and tracker > 10:
			curX = Draw.mouseX()
			curY = Draw.mouseY()
		#first alien
		if curX >= 75 and curX <= 175 and curY >= 250 and curY <= 350:
			return "pinkAlien.gif"
		#second alien
		elif curX >= 225 and curX <= 325 and curY >= 250 and curY <= 350:
			return "redAlien.gif"
		#third alien
		elif curX >= 375 and curX <= 475 and curY >= 250 and curY <= 350:
			return "purpleAlien.gif"
		#fourth alien
		elif curX >= 525 and curX <= 625 and curY >= 250 and curY <= 350:
			return "rickMorty.gif"

#this will ask the user to enter their name if they achieved the high score
#input is the users score and the dictionary of highscores 
def highScore(score, stats):
	#if this isn't the first game, if the score is < one of the scores in the dict
	if len(stats) > 0:
		for i in stats:
			if int(score) <= i:
				#they didn't get a highscore, cut to scoreboard
				return	
			
	#if they made it this far, they got a highscore
	#turn the score into an int
	newScore = int(score)
	#add the score to the dictionary
	stats[newScore] = ""	
	Draw.clear() 

	while True:
		#Draws the whole screen
		Draw.setColor(Draw.GREEN)
		Draw.setFontSize(50)				
		Draw.string("YOU GOT THE HIGHSCORE!", 10, 20)
		Draw.filledRect(0, 80, 700, 360)
		Draw.setFontSize(30)
		Draw.setColor(Draw.BLACK)
		Draw.string("What is your name? : " + str(stats[newScore]), 20, 220)
		Draw.setColor(Draw.GREEN)
		Draw.string('Press "ENTER" to continue', 190, 450)
		
		#user keyboard input.
		if Draw.hasNextKeyTyped():
			newKey = Draw.nextKeyTyped() 
			
			#if the new key is a valid number or letter
			if newKey in "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" and len(stats[newScore]) < 15:
				#add it to the dictionary 
				stats[newScore] += newKey
			#if the new key is the space bar
			if newKey == "space":
				#add a space
				stats[newScore] += " "
			#if the new key is the delete button
			if newKey == "BackSpace" and len(stats[newScore]) != 0:
				#slice the last key off the dictionary
				stats[newScore] = stats[newScore][:-1]
			#if they pressed enter and they wrote a name 
			if newKey == "Return" and len(stats[newScore]) > 1:
				#end the loop
				Draw.clear()
				return

#end screen that reveals all the users stats and the highscore
#input: starWindowX to make the stars move, list of stars, lives, 
#users score, amount of shields used, amount of lives lost in total, 
#windowX to determine if the user won or lost, the alien charecter, the amount of monsters killed, stats for highscore"
def endGame(starWindowX, stars, lifeHearts, 
            score, shieldsUsed, livesLost, 
            windowX, alien, monstersKilled, stats):
	
	#determines what the highscore is
	bestName = ""
	bestScore = -1
	for i in stats:
		if i > bestScore:
			bestScore = i
			bestName = stats[i]
	
	starWindowX = 0
	while True:
		#draws the stars moving as decor 
		starWindowX += 3
		Draw.clear()
		for star in stars: 
			if star[1] >= starWindowX - star[4] and star[1] <= starWindowX + WINDOWWIDTH:
				Draw.setColor(Draw.YELLOW)
				Draw.filledRect(star[1] - starWindowX, star[2], star[4], star[4])	
		#draws the whole screen
		Draw.setFontBold(True)
		Draw.setColor(Draw.GREEN)
		Draw.setFontSize(50)
		
		#determines whether you lost or just reached the end (won)
		if lifeHearts <= 0 and windowX < STRIPWIDTH: 
			#loser
			Draw.string("GAME OVER", 190, 70) 
		elif lifeHearts > 0: 
			#winner
			Draw.string("YOU WON!", 190, 70) 
			
		#draws all of the stats		
		Draw.setFontSize(20)
		Draw.setFontBold(False)
		Draw.string("Highscore : " + str(int(bestScore)) + " - " + str(bestName), 190, 140)
		
		#2d list of all the stats
		endStats = [["Score : ", str(int(score))],\
		           ["Shields used : ", str(shieldsUsed)],\
		           ["Lives lost : ", str(livesLost)],\
		           ["Monsters killed : ", str(monstersKilled)]]
		#displays the stats
		for i in range(len(endStats)):
			Draw.string(endStats[i][0] + endStats[i][1], 190, 170 + i*30)
		
		#play again button
		Draw.filledRect(190, 290, 300, 50)
		Draw.setFontBold(True)
		Draw.setColor(Draw.BLACK)
		Draw.setFontSize(30)
		Draw.string("PLAY AGAIN", 255, 300)
		
		#alien as decor
		Draw.picture(alien, 290, 350)
		
		Draw.show()
		
		# mouse x and y cooridnates
		curX = 0 
		curY = 0
		if Draw.mousePressed():
			curX = Draw.mouseX()
			curY = Draw.mouseY()
		
		# if the play again button has been pressed 
		if curX >= 250 and curX <= 250 + 180 and curY >= 290 and curY <= 290 + 40:
			#fall out of loop which will restart the game 
			return
				
def drawScreen(windowX, windowY, starWindowX, #input window x coordinates, stars window x coordinates. 
	       things, shipY, alien, #list of things, ships y coordinate, alien charecter chosen
	       lifeHearts, applyShield, immunity, #amount of lives, if the shield is applied, if the shield is applied
	       drawText, score, fire, #draws the text, score, fire when ship hits asteroid
               tracker, laserX, #tracker that tracks the frames of the game, lasers X coordinate
               shoot, monstersKilled): #if laser is activated boolien value, amount of monsters killed 
	
	Draw.clear()
	
	#Draws all the things on the strip 
	for thing in things: 
		#stars
		if thing[0] == "star": 	
		#if the star is within the star's windows X - the items size so it smoothly dissapears
			if thing[1] >= starWindowX - thing[4] and thing[1] <= starWindowX + windowY: 
				#if the shield is activated 
				if applyShield == True:
					#the stars are a different color 
					Draw.setColor(Draw.VIOLET) 
				else:
					#otherwise, the stars will be yellow
					Draw.setColor(Draw.YELLOW)
				
				#draws a rectangle with the stars x and y coordinate and its specific size
				Draw.filledRect(thing[1] - starWindowX, thing[2], thing[4], thing[4]) 
				
		#if the items x is within the window X - the items size so it smoothly dissapears and it was never hit before	
		if (thing[1] >= windowX - ASTEROIDSIZE 
		    and thing[1] <= windowX + windowY 
		    and thing[3] == False):
			
			#if the item is an asteroid
			if thing[0] == "asteroid": 
				#if the shield is activated
				if applyShield == True:
					#the asteroid will turn pink and drawn on its x and y coordinate 
					Draw.picture("asteroidPink.gif", thing[1] - windowX, thing[2]) 
				else:
					#otherwise, the asteroid will remain blue and drawn on its x and y coordinate 
					Draw.picture("asteroidBlue.gif", thing[1] - windowX, thing[2]) 
					
			#if the item is a gold		
			if thing[0] == "gold": 
				#5 lives is the limit, it wont draw if you already have 5
				if lifeHearts < 5: 
					#draws the heart in the right x and y coordinates 
					Draw.picture("heart2.gif", thing[1] - windowX, thing[2])
			#if the item is a shield 
			if thing[0] == "shield": 
				#3 shields is the limit
				if immunity < 3: 
					#it will draw a shield 
					Draw.picture("shield2.gif", thing[1] - windowX, thing[2])
			#if its a monster
			if thing[0] == "monster":
				#draws the monster image 
				Draw.picture(thing[4], thing[1] - windowX, thing[2])
				
	#if the shield has been activated 				
	if shoot == True:
		#draws the laser, according to the ships x and y 
		Draw.setColor(Draw.RED)
		#laserX = SHIPX + 50
		Draw.filledOval(laserX, shipY + 50, LASERWIDTH, LASERHEIGHT)		
		Draw.setColor(Draw.WHITE)
		#draws it slightly smaller for glow effect
		Draw.filledOval(laserX + 2, shipY + 53, LASERWIDTH-6, LASERHEIGHT-6)	
	
	#if the shield has been activated				
	if applyShield == True: 
		#draw the bubble with the same x and y coordinates as the ship
		Draw.picture("bubble.gif", SHIPX-11, shipY-8) 
		#if this draw text value is true
		if drawText == True: 
			#write string "shield activated"
			Draw.setColor(Draw.GREEN)
			Draw.setFontSize(50)
			Draw.string("SHIELD ACTIVATED", 130, 220)
			
	#if the ship hit an asteroid, fire becomes True, if fire is True...
	if fire == True: 
		#draw the fire image on top of the ship
		Draw.picture("fire.gif", SHIPX+4, shipY - 23) 
	
	#draws instructions only in the beggining 	
	if tracker < 60 * 5:
		Draw.setColor(Draw.GREEN)
		Draw.setFontBold(True)
		Draw.setFontSize(15)
		Draw.string('Press the "up" and "down" keys to move the spaceship and avoid the asteroids', 10, 55)
		Draw.string('Collect the hearts to receive an extra life', 10, 80)
		Draw.string('Collect the shields to receive an immunity shield', 10, 105)
		Draw.string('Press the "space bar" to activate your shield', 10, 130)
		Draw.setColor(Draw.RED)
		Draw.string('MONSTERS TAKE 2 HEARTS', 10, 155)
		Draw.string('Press the "right" key to employ your laser and kill them', 10, 180)
	
	#draw ship according to the variable of which ship was chosen, ships x and y 
	Draw.picture(alien, SHIPX, shipY) 
	
	#loops the amount of times the amount of shields you have
	for i in range(immunity): 
		#draws the shield icons	
		Draw.picture("shield.gif", 650-i*50, 445)
	
	#loops the amount of times the amount of lives you have
	for i in range(lifeHearts):
		#draws the life icons
		Draw.picture("heart.gif", 640-i*55, 5) 
	
	#draws the score
	Draw.setColor(Draw.GREEN)
	Draw.setFontSize(40)
	#convert score to int and then string 
	Draw.string(str(int(score)), 10, 450) 
	
	Draw.setFontSize(20)
	#displays the amount of monsters killed
	Draw.string("Monsters:" + str(monstersKilled), 5, 5)
	
	Draw.show()

#main function that runs the game
#input all of the lists of things, alien chosen, the stats dictionary
def playRound(stars, asteroids, gold, shields, monsters, alien, stats):
	
	# combines all the lists together 
	things = stars + asteroids + gold + shields + monsters 
	
	# x and y coordinates of the mouse 
	curX = 0 
	curY = 0
	
	shipY = 200 #starting point of ship Y
	tracker = 0 #tracks the frames of the game
	score = 0 #the score of the game 	
	
	#shield variables 
	immunity = 1 #amount of shields
	applyShield = False #if the shield is being applied 
	shieldTracker = 0 #tracks the frames of the game once the shield is activated
	shieldsUsed = 0 #tracks the total amount of shields used
	drawText = False #if the text "shield activavted" should appear
	
	#ship gets hit variables
	fire = False #if the ship will be on fire
	lifeHearts = 3 #amlount of lives 
	hitTracker = 0 #tracks the time after being hit 
	livesLost = 0 #tracks the total amount of lives lost
	
	#speed of game variables
	speed = 0 #speed of the game
	windowX = 0 #starting point of window x
	starWindowX = 0 #seperate window for stars so they move slower - creates depth
	
	#laser variables
	shoot = False #if the laser is activated
	laserX = SHIPX + (SHIPSIZE / 2) # the x of the laser will always be in the center of the x of the ship
	laserTracker = 0 #tracks the amount of time once the laser is activated
	monstersKilled = 0 #tracks the amount of monsters killed
	
	#if you havent reached the end of the strip or you didnt lose all your lives		
	while windowX < STRIPWIDTH and lifeHearts > 0:
		#helpful tracker
		tracker += 1
		
		#increases the score
		score += .9 
		
		#as the game goes on, the speed gradually increases. 
		starWindowX += (1.5 + speed) 
		windowX += (3 + speed) 
		speed += .001 
		
		#user input		
		if Draw.hasNextKeyTyped():
			newKey = Draw.nextKeyTyped() 
			#if the newKey is "up", and the ship isnt on the top
			if newKey == "Up" and shipY != 0: 
				shipY -= 100 
			 #if the newKey is "Down" and the ship isnt at the bottom
			if newKey == "Down" and shipY != 400:
				shipY += 100 
			#if "space" is pressed and you have more than 0 shields and tracker fixes bug of shield being activated accidently 	
			if newKey == "space" and immunity > 0 and tracker > 30: 
				#increase the shieled tracker 
				shieldsUsed += 1 
				#one shield is used 
				immunity -= 1 
				#draw text "Shield Activated"
				drawText = True
				#shield is now applied 
				applyShield = True 
			#is the right key is typed and it shoot isnt already activated
			if newKey == "Right" and shoot == False:
				#laser is activated
				shoot = True			
		
		#if the shield is applied		
		if applyShield == True: 
			#begin the shield tracker
			shieldTracker += 1 
			#score will increase much faster
			score += 10 
			#after two seconds
			if shieldTracker > 60 * 2: 
				#the "shield activated" text will dissapear
				drawText = False 
			#after 5 seconds
			if shieldTracker > 60 * 5: 
				#the shield will dissapear
				applyShield = False 
				#reset shield tracker back to 0
				shieldTracker = 0
		#if the laser is activated		
		if shoot == True:
			#start the laser tracker
			laserTracker += 1
			#it only lasts for 15 frames 
			if laserTracker > 15:
				laserTracker = 0
				shoot = False
				
		#if fire is being applied		
		if fire == True: 
			#start hit tracker
			hitTracker += 1 
			#after one second 
			if hitTracker > 60 * 1:
				#fire dissapears
				fire = False 
				#reset the hit tracker to 0
				hitTracker = 0 	
				
		#if the ship touches a "gold" and you dont already have 5
		if getHitGold(gold, shipY, windowX) == "gold" and lifeHearts < 5:
			#gain a life
			lifeHearts += 1 
			
		#if the ship touches an "asteroid" 	
		if getHit(asteroids, shipY, windowX, applyShield) == "asteroid":
			#lose a life 
			lifeHearts -= 1 
			#ship will catch on fire
			fire = True
			#if the score is less than 1000
			if score < 1000: 
				#reset score to 0
				score = 0 
			else:
				#subtract 1000 from the score 
				score -= 1000 
			#increase the lives lost tracker 
			livesLost += 1
			
		#if the ship hits a shield and you dont already have three
		if getHitShield(shields, shipY, windowX) == "shield" and immunity < 3:
			#increase the amount of shields by 1
			immunity += 1 
		#if ship hits monster	
		if getHitMonster(monsters, shipY, windowX, applyShield) == "monster":
			#lose 2 instead of 1 lives
			livesLost += 2
			lifeHearts -= 2
		#if lser hits monster	
		if getHitLaser(monsters, windowX, laserX, shipY, shoot) == "laser":
			#score increases by 500
			score += 500
			#increase tracker
			monstersKilled += 1
			
		#Draws everything
		drawScreen(windowX, WINDOWWIDTH, starWindowX, 
			   things, shipY, alien, 
			   lifeHearts, applyShield, immunity, 
			   drawText, score, fire, tracker, laserX, shoot, monstersKilled)
	
	#only displays if user gets highscore	
	highScore(score, stats)
	
	#displays stats and replay button
	endGame(starWindowX, stars, lifeHearts, score, shieldsUsed, livesLost, windowX, alien, monstersKilled, stats)
				
	
def main():
	starList, asteroidList, goldList, shieldList, monsterList = createThings() 
	createCanvas()
	pressStartScreen(starList)
	alien = pickAlienChar()
	stats = {}
	while True:		
		starList, asteroidList, goldList, shieldList, monsterList = createThings() 
		playRound(starList, asteroidList, goldList, shieldList, monsterList, alien, stats)
		
main()