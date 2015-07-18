[33mcommit e5096c533383637164680b1f2ff70ca9542bfcc7[m
Author: Dracon <mohtaprashantrocks@gmail.com>
Date:   Tue Jul 14 22:17:32 2015 +0530

    Obstacles added

[1mdiff --git a/Cgame_part2.py b/Cgame_part2.py[m
[1mindex 4049dad..ef4c1b2 100755[m
[1m--- a/Cgame_part2.py[m
[1m+++ b/Cgame_part2.py[m
[36m@@ -59,18 +59,18 @@[m [mwhile not done:[m
                 lin_temp=random.choice([0,1])[m
                 screenbuff[lin_temp][-1]=OBSTACLE_CHAR[m
                 game["obstacle"]+=1[m
[31m-##        elif screenbuff[0][-2] != OBSTACLE_CHAR:[m
[31m-##            if game["obstacle"]<int(game["level"]) and random.choice([0,1]):[m
[31m-##                lin_temp=random.choice([0,1])[m
[31m-##                if(lin_temp==1):[m
[31m-##                    screenbuff[lin_temp][-1]=OBSTACLE_CHAR[m
[31m-##                    game["obstacle"]+=1[m
[31m-##        elif screenbuff[1][-2] != OBSTACLE_CHAR:[m
[31m-##            if game["obstacle"]<int(game["level"]) and random.choice([0,1]):[m
[31m-##                lin_temp=random.choice([0,1])[m
[31m-##                if(lin_temp==0):[m
[31m-##                    screenbuff[lin_temp][-1]=OBSTACLE_CHAR[m
[31m-##                    game["obstacle"]+=1[m
[32m+[m[32m        elif screenbuff[0][-2] != OBSTACLE_CHAR:[m
[32m+[m[32m            if game["obstacle"]<int(game["level"]) and random.choice([0,1]):[m
[32m+[m[32m                lin_temp=random.choice([0,1])[m
[32m+[m[32m                if(lin_temp==1):[m
[32m+[m[32m                    screenbuff[lin_temp][-1]=OBSTACLE_CHAR[m
[32m+[m[32m                    game["obstacle"]+=1[m
[32m+[m[32m        elif screenbuff[1][-2] != OBSTACLE_CHAR:[m
[32m+[m[32m            if game["obstacle"]<int(game["level"]) and random.choice([0,1]):[m
[32m+[m[32m                lin_temp=random.choice([0,1])[m
[32m+[m[32m                if(lin_temp==0):[m
[32m+[m[32m                    screenbuff[lin_temp][-1]=OBSTACLE_CHAR[m
[32m+[m[32m                    game["obstacle"]+=1[m
             [m
 [m
     #check for collision[m
