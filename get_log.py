import numpy as np 
import re

class Task1:
    def endGame(self,players,total_kills,n_kill,n_killed,games):
        players = np.unique(players)
        new = []
        for p in players:
            if p in players:
                new.append(p)
        players = new

        score = {}
        for p in players:
            if p != '<world>':
                score[str(p)] = n_kill.count(p)-n_killed.count(p)
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
        verify = 1

        for f in file.readlines():
            if str(f).find("InitGame")>0:
                verify = 0
            if str(f).find("killed")>0:
                game.append(f)
                n_kill.append(self.eachN_kill(f))
                n_killed.append(self.eachN_killed(f))
                total_kills+= 1
            if str(f).find("ClientUserinfoChanged")>0:
                players.append(f.split('n\\')[1].split('t\\')[0].split('\\')[0])
            if str(f).find("-------------------------")>0 and verify==0:
                all[str(games)]=self.endGame(players,total_kills,n_kill,n_killed,games)
                games+=1
                players = []
                n_kill = []
                n_killed = []
                game = []
                total_kills = 0
                verify = 1
        return all
        
class Task2:
    def task2(self,file):
        n_kill = []
        for f in file.readlines():
            if str(f).find("killed")>0:
                n_kill.append(Task1().eachN_kill(f))
        players = np.unique(n_kill)
        for p in players:
            if p != '<world>':
                print(p+" matou "+str(n_kill.count(p)))

class Bonus:
    def bonus(self,file):
        death = []
        cause_death = "MOD_UNKNOWN,MOD_SHOTGUN,MOD_GAUNTLET,MOD_MACHINEGUN,MOD_GRENADE,MOD_GRENADE_SPLASH,MOD_ROCKET,MOD_ROCKET_SPLASH,MOD_PLASMA,MOD_PLASMA_SPLASH,MOD_RAILGUN,MOD_LIGHTNING,MOD_BFG,MOD_BFG_SPLASH,MOD_WATER,MOD_SLIME,MOD_LAVA,MOD_CRUSH,MOD_TELEFRAG,MOD_FALLING,MOD_SUICIDE,MOD_TARGET_LASER,MOD_TRIGGER_HURT,MOD_NAIL,MOD_CHAINGUN,MOD_PROXIMITY_MINE,MOD_KAMIKAZE,MOD_JUICED,MOD_GRAPPLE"
        all = {}
        game = 0
        verify = 1

        for f in file.readlines():
            if str(f).find("InitGame")>0:
                verify = 0
            if f.find("killed")>0:
                name = re.sub('\n',"",f.split('by ')[1])
                for cs in cause_death.split(','):
                    if cs == name:
                        death.append(name)

            if str(f).find("-------------------------")>0 and verify==0:
                game+=1
                score = {}
                name = "game_"+str(game)
                count = 0
                for n in death:
                    score[str(n)] = death.count(n)
                count = 0
                all['id'] = game
                all[name] = score
                death = []
                verify = 1
        return all

t = Task1()
score = t.task1(open('qgames.log',"r"))   

t2 = Task2()
t2.task2(open('qgames.log',"r"))

b = Bonus()
print(b.bonus(open('qgames.log',"r")))