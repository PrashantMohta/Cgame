import mlcd,pygame,time,random

PLAYER_CHAR=">"
OBSTACLE_CHAR="|"

STARTSCREEN_TEXT=[["Avoid Obstables","Space for more"],
                  ["Controls:space","for moving and"],
                  ["Esc for quitting","the game"],
                  ["To begin",">Press Space"],
                  ]

screenbuff=[[" "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "]]

player={"position":0,"line":0,"score":000}
game={"speed":4.05,"level":2.5,"obstacle":0} 
keys={"space":False,"quit":False,"next":False}

def keypress(): #get keypresses
    global keys
    keys["space"]=keys["quit"]=keys["next"]=False #reset all keys
    #check keys
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            keys["space"] = True
        elif event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            keys["quit"] = True

def startscreen():
    global player,game,keys,startstate
    done=False
    while not done:
        if(startstate<len(STARTSCREEN_TEXT)):
            mlcd.draw(STARTSCREEN_TEXT[startstate])
        else:
            done=True
        keypress()
        if keys["space"]:
            startstate+=1
        if keys["quit"]:
            startstate=len(STARTSCREEN_TEXT)+1
    
    
def endscreen():
    global player,game,keys
    done=False
    while not done:
        mlcd.draw(["score="+str(player["score"])+"spd="+str(game["speed"]),"  -PrashantMohta"])
        keypress()
        if keys["quit"]:
            done=True
    pygame.quit()
    exit()

    
done=False
#initialize mlcd as 16x2 character lcd
mlcd.init(16,2)
lasttime=time.time()
curtime=0.0
startstate=0
#show start screen
startscreen()

while not done:
    curtime=time.time()
    if (curtime-lasttime>1/game["speed"]):
        lasttime=curtime


        #increment score and count obstacle
        #up the level and increase the speed
        if screenbuff[0][player["position"]]==OBSTACLE_CHAR or screenbuff[1][player["position"]]==OBSTACLE_CHAR:
            player["score"]+=1
            game["obstacle"]-=1
            game["level"]+=0.5
            game["speed"]+=0.05
            #if((game["level"]+2)%game["posmovthres"]==0 and player["position"]<12 and screenbuff[player["line"]][player["position"]+1]!=OBSTACLE_CHAR and screenbuff[player["line"]][player["position"]+2]!=OBSTACLE_CHAR):
            #    player["position"]+=1

        #move everything one place to the left
        for lindex,lin in enumerate(screenbuff,start=0):
            for index,pos in enumerate(lin, start=0):
                if index>0:
                    screenbuff[lindex][index-1]=pos
       
        #add new chars at end of buff , obstacles if there is a gap
        screenbuff[0][-1]=" "
        screenbuff[1][-1]=" "
        if screenbuff[0][-2] != OBSTACLE_CHAR and screenbuff[1][-2]!=OBSTACLE_CHAR:
            if game["obstacle"]<int(game["level"]) and random.choice([0,1]):
                lin_temp=random.choice([0,1])
                screenbuff[lin_temp][-1]=OBSTACLE_CHAR
                game["obstacle"]+=1
        elif screenbuff[0][-2] != OBSTACLE_CHAR:
            if game["obstacle"]<int(game["level"]) and random.choice([0,1]):
                lin_temp=random.choice([0,1])
                if(lin_temp==1):
                    screenbuff[lin_temp][-1]=OBSTACLE_CHAR
                    game["obstacle"]+=1
        elif screenbuff[1][-2] != OBSTACLE_CHAR:
            if game["obstacle"]<int(game["level"]) and random.choice([0,1]):
                lin_temp=random.choice([0,1])
                if(lin_temp==0):
                    screenbuff[lin_temp][-1]=OBSTACLE_CHAR
                    game["obstacle"]+=1
            

    #check for collision
    if screenbuff[player["line"]][player["position"]]==OBSTACLE_CHAR:
        done=True #player lost
    #add player to the buffer
    screenbuff[player["line"]][player["position"]]=PLAYER_CHAR
    #ready the lines for drawing on lcd
    lines=[''.join(screenbuff[0]) + "|scr",
         ''.join(screenbuff[1]) + "|"+str(player["score"])]
    mlcd.draw(lines)
    
    #remove player from buffer
    screenbuff[player["line"]][player["position"]]=" "
    #get keypresses
    keypress()
    #modify player line (move the player) if space is pressed
    if keys["space"]:
        if player["line"]==0:
            player["line"]=1
        else:
            player["line"]=0
    #quit
    if keys["quit"]:
        print("game quit")
        done=True
endscreen()  
pygame.quit()
    
    
