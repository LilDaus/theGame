
#Her der indalder vi de midler der skal bruge for at få vores pygame, os og pygame menu til at virke
import pygame
import os
import pygame_menu


pygame.init()
surface = pygame.display.set_mode((600, 400))

pygame.mixer.init(frequency=44100, size=-16, channels=6, buffer=2048)
font = pygame.font.Font('freesansbold.ttf', 32)
#Her der kommer den musik ind som er i spillet. Den bliver impoteret via. en mp3 fil. Men virker også med andre former for filer
musicPath = os.path.normpath(os.path.join('assets', 'music','MusikQuang.mp3'))
pygame.mixer.music.load(musicPath)
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

#Her er størrelsen på spillet. Vi har gået efter Benjamins computers skærm
gameWindowHeight=768
gameWindowWidth=1366
#Her der impotere vi de forskellige klasser ind i vores main kode. Det gør det meget overskueligt
from Player import PlayerClass
from Enemy import EnemyClass
#from Shot import ShotClass
from Terrain import TerrainClass
from random import randint as rando
from Alger import AlgerClass

background_image = pygame.transform.scale(pygame.image.load('background3.png').convert_alpha(),(gameWindowWidth, gameWindowHeight))

terrain=[]
enemies=[]
shots=[]
algers=[]


screen = pygame.display.set_mode((gameWindowWidth, gameWindowHeight))



def collisionChecker(firstGameObject, secondGameObject):
        if firstGameObject.x + firstGameObject.width > secondGameObject.x and firstGameObject.x < secondGameObject.x + secondGameObject.width and firstGameObject.y + firstGameObject.height > secondGameObject.y and firstGameObject.y < secondGameObject.y + secondGameObject.height:
            return True
#Her kommer fjenderne i spillet til stede. Her koder vi deres y og x postion. Vi har også hastiheden på fjenden her
def spawnEnemy():
    enemies.append(EnemyClass(screen,spawnPosX=rando(0,gameWindowWidth),spawnPosY=rando(0,gameWindowHeight),speedX=rando(-7,2),speedY=rando(-4,2)))

for i in range(10):
        spawnEnemy()

#Her der kommer vores vand/alger ind i spillet.
def createAlger():
    algers.append(AlgerClass(screen, _x= rando(-10,gameWindowWidth+100), _y=rando(-100,gameWindowHeight+100),_width=rando(25,25) ,_height=rando(25,25)))


#Her er terrænget. Det er alle de murer der er placeret på vores bane. De tal der står er kordinaterne for dem
def createTerrain():
    terrain.append(TerrainClass(screen, 585, 130, 200, 10))  # 1
    terrain.append(TerrainClass(screen, 680, 130, 10, 70))  # 2
    terrain.append(TerrainClass(screen, 440, 0, 10, 220))  # 3
    terrain.append(TerrainClass(screen, 910, 0, 10, 220))  # 4
    terrain.append(TerrainClass(screen, 585, 600, 200, 10))  # 5
    terrain.append(TerrainClass(screen, 680, 600, 10, 70))  # 6
    terrain.append(TerrainClass(screen, 560, 500, 250, 10))  # 7
    terrain.append(TerrainClass(screen, 560, 320, 10, 190))  # 8
    terrain.append(TerrainClass(screen, 810, 320, 10, 190))  # 9
    terrain.append(TerrainClass(screen, 570, 320, 70, 10))  # 10
    terrain.append(TerrainClass(screen, 740, 320, 70, 10))  # 11
    terrain.append(TerrainClass(screen, 450, 210, 70, 10))  # 12
    terrain.append(TerrainClass(screen, 840, 210, 70, 10))  # 13
    terrain.append(TerrainClass(screen, 560, 698, 10, 70))  # 14
    terrain.append(TerrainClass(screen, 810, 698, 10, 70))  # 15
    terrain.append(TerrainClass(screen, 420, 500, 10, 220))  # 16
    terrain.append(TerrainClass(screen, 930, 500, 10, 220))  # 17
    terrain.append(TerrainClass(screen, 430, 600, 60, 10))  # 18
    terrain.append(TerrainClass(screen, 870, 600, 60, 10))  # 19
    terrain.append(TerrainClass(screen, 0, 384, 70, 10))  # 20
    terrain.append(TerrainClass(screen, 1296, 384, 70, 10))  # 21
    #terrain.append(TerrainClass(screen, 420, 360, 40, 40))  # 22
    #terrain.append(TerrainClass(screen, 910, 360, 40, 40))  # 23
    terrain.append(TerrainClass(screen, 150, 0, 60, 100))  # 24
    terrain.append(TerrainClass(screen, 150, 160, 60, 448))  # 25
    terrain.append(TerrainClass(screen, 150, 668, 60, 100))  # 26
    terrain.append(TerrainClass(screen, 1156, 0, 60, 100))  # 27
    terrain.append(TerrainClass(screen, 1156, 160, 60, 448))  # 28
    terrain.append(TerrainClass(screen, 1156, 668, 60, 100))  # 29
#Her får vi vores menu til at kunne trykke på knappen start. Under det kan man se highscoren
def start_the_game():
    highScore = 0

    try:
        with open('highScoreFile') as file:
            data = file.read()
            highScore = int(data.strip())
            print("Loaded highscore:", highScore)
    except:
        print("highScoreFile not found, resetting to 0.")

    for i in range(30):
        createAlger()


    createTerrain()


    playerObject = PlayerClass(screen,xpos=680, ypos=384,terrainCollection=terrain)


    done = False
    while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    done = True

                #-------PLAYER CONTROLS---------

                #KEY PRESSES:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        playerObject.ySpeed -= playerObject.maxSpeed
                    if event.key == pygame.K_DOWN:
                        playerObject.ySpeed += playerObject.maxSpeed
                    if event.key == pygame.K_LEFT:
                        playerObject.xSpeed -= playerObject.maxSpeed
                    if event.key == pygame.K_RIGHT:
                        playerObject.xSpeed += playerObject.maxSpeed
                        #Skud:                          .. Men kun når spilleren bevæger sig:

                    #if event.key == pygame.K_SPACE:  # and (playerObject.xSpeed !=0 or playerObject.ySpeed !=0):
                       # shots.append(ShotClass(screen, spawnPosX=playerObject.x + playerObject.width / 2,spawnPosY=playerObject.y + playerObject.height / 2,playerSpeedX=playerObject.xSpeed, playerSpeedY=playerObject.ySpeed))
                #KEY RELEASES:
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        playerObject.ySpeed += playerObject.maxSpeed
                    if event.key == pygame.K_DOWN:
                        playerObject.ySpeed -= playerObject.maxSpeed
                    if event.key == pygame.K_LEFT:
                        playerObject.xSpeed += playerObject.maxSpeed
                    if event.key == pygame.K_RIGHT:
                        playerObject.xSpeed -= playerObject.maxSpeed
            #debug: print out unused pygame events
            #else:
            #        print(event)

            #UPDATE GAME OBJECTS:

            playerObject.update()

            for shot in shots:
                shot.update()

            for enemy in enemies:
                enemyIsDead = False
                enemy.update()

                if enemy.x>gameWindowWidth or enemy.y>gameWindowHeight or enemy.x<0 or enemy.y<0:
                    enemyIsDead=True

                for shot in shots:
                    if collisionChecker(shot,enemy):
                        enemyIsDead=True
                        shots.remove(shot)
                        playerObject.points +=1
                        enemy.playSound()
                        #print('Points:',playerObject.points)
                        if playerObject.points > highScore:
                            highScore = playerObject.points
                if collisionChecker(enemy,playerObject):
                    playerObject.collisionSFX.play()
                    print("Quan mistede vand")

                    playerObject.points=0

                if enemyIsDead:
                    enemies.remove(enemy)
                    spawnEnemy()

            for alger in algers:
                if collisionChecker(alger, playerObject):
                    algers.remove(alger)
                    playerObject.collisionSFX.play()
                    playerObject.points += 1
                    createAlger()


            #DRAW GAME OBJECTS:
            screen.fill((0, 0, 0)) #blank screen. (or maybe draw a background)
            screen.blit(background_image,[0,0])
            playerObject.draw()



            #Score:                                                 antialias?, color
            text = font.render('Vand opsamlet: ' + str(playerObject.points), True,(0, 255, 0))
            screen.blit(text,(0,0))

            text = font.render('HIGHSCORE: ' + str(highScore), True, (255, 0, 0))
            screen.blit(text, (300,0))

            for shot in shots:
                shot.draw()

            for enemy in enemies:
                enemy.draw()

            for tile in terrain:
                tile.draw()

            for alger in algers:
                alger.draw()
            playerObject.draw()

            pygame.display.flip()
            clock.tick(60)


    #When done is false the while loop above exits, and this code is run:
    with open('highScoreFile', 'w') as file:
        print("Saving highscore to file:", highScore)
        file.write(str(highScore))


menu = pygame_menu.Menu(height=300,width=400,theme=pygame_menu.themes.THEME_ORANGE,title='Hent vand til Quan')

menu.add_text_input('Quan'
                    '')
menu.add_button('Start', start_the_game)
menu.add_button('Quit', pygame_menu.events.EXIT)

if __name__ == '__main__':
    menu.mainloop(surface)
