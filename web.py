from flask import Flask, jsonify, request
from urllib.request import urlopen, Request
import os
import numpy as np 
import json
import re

arq = open('qgames.log',"r")

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
                total_kills = len(n_kill)
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
    def task2(self,score):
        print(score)

t = Task1()

app = Flask(__name__)

@app.route('/all', methods=['GET'])
def game():
    score = t.task1(open('qgames.log',"r")) 
    return score

@app.route('/all/<int:id>', methods=['GET'])
def search_game(id):
    score = t.task1(arq) 
    return score[str(id)]


#PARTE4
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)