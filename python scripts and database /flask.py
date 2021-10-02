from flask import Flask
from flask_cors import CORS
from flask_cors import cross_origin
import mysql.connector
import json
import random

app = Flask(__name__)
CORS(app)
@app.route('/')
@cross_origin()
def myApi():
    mydb = mysql.connector.connect(
      host="wpra.mysql.pythonanywhere-services.com",
      user="wpra",
      password="#######",
      database="wpra$default"
    )
    cur = mydb.cursor()
    #select 6 random users
    sql = "SELECT * FROM Users     ORDER BY RAND ( )     LIMIT 6;"
    cur.execute(sql)
    ans = []
    for x in cur:


        # a Python object (dict):
        x = {
          "name": x[0],
          "score": random.randint(0, 100),
          "imageUrl": x[1]
        }

        


        ans.append(x)
    #converts ans to json
    ans = json.dumps(ans)
    return(str(ans))
