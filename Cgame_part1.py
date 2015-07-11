import mlcd,pygame

PLAYER_CHAR=">"

screenbuff=[[" "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "]]

player={"position":0,"line":0,"score":000}
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


done=False
#initialize mlcd as 16x2 character lcd
mlcd.init(16,2)
while not done:

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
pygame.quit()
    
    
