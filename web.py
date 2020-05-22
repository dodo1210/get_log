from flask import Flask
import numpy as np 
import re
from get_log import Task1

app = Flask(__name__)

@app.route('/all', methods=['GET'])
def game():
    t = Task1()
    f = open('qgames.log',"r")
    score = t.task1(f) 
    return score

@app.route('/all/<int:id>', methods=['GET'])
def search_game(id):
    t = Task1()
    f = open('qgames.log',"r")
    score = t.task1(f)
    return score[str(id)]

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)