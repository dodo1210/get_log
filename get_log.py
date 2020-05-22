import numpy as np 
import json
import re

file = open('qgames.log',"r")

class Task1:

    def endGame(self,players,total_kills,n_kill,n_killed,games):
        new = []
        for p in players:
            if p in players:
                new.append(p)
        players = new
        score = {}
        
        #n_kill.remove('<world>')
        count = 0

        for name in n_kill:
            if name != '<world>':
                count+= 1
                score[str(name)] = count
        count = 0
        for name in n_killed:
            score[str(name)] = count
            count-= 1
        r = {}
        r['id'] = games
        r['total_kills'] = total_kills
        r['players'] = players
        r['kills'] = score 
        result = r
        return result

    def eachN_kill(self,f):
        return f.split(':')[3].split(' killed')[0].split('\\')[0].strip()
    
    def eachN_killed(self,f):
        return f.split('killed ')[1].split(' by')[0].split('\\')[0]

    def task1(self,file):
        all = {}
        game = []
        players = []
        total_kills = 0
        n_kill = []
        n_killed = []
        games = 1

        for f in file.readlines():
            if str(f).find("killed")>0:
                game.append(f)
                n_kill.append(self.eachN_kill(f))
                n_killed.append(self.eachN_killed(f))
                total_kills+=1

            if str(f).find("ClientUserinfoChanged")>0:
                players.append(f.split('n\\')[1].split('t\\')[0].split('\\')[0])
            
            if str(f).find("InitGame")>0:
                name = str("game_"+str(games))
                all[name]=self.endGame(players,total_kills,n_kill,n_killed,games)
                games+=1
                players = []
                n_kill = []
                n_killed = []
                game = []
                total_kills = 0
        return all
        
class Task2:
    def task2(self,score):
        print(score)



t = Task1()
score = t.task1(file)   

t2 = Task2()
t2.task2(score)
