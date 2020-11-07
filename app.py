from flask import Flask, request, jsonify
from flask_restx import Resource, Api
from flask_cors import CORS
import json
import requests
import pymysql

app = Flask(__name__)
api = Api(app)
CORS(app, resources={r"/*": {"origins": "*"}})

DB_HOST = 'mdb-test.c6vunyturrl6.us-west-1.rds.amazonaws.com' 
DB_USER = 'bsale_test' 
DB_PASS = 'bsale_test' 
DB_NAME = 'bsale_test'

@api.route('/getProducts/orderBy/<string:orderBy>',methods=['GET'])
class searchProducts(Resource):
    def get(self,orderBy):
        if not orderBy: 
            return "orderBy parameter missing",400

        orderByOpts = ['id','name','price','discount','category']
        
        flag = 0 
        for item in orderByOpts:
            if item == orderBy.lower():
                flag = 1
        
        if flag == 0:
            return "Not a valid orderBy parameter. Options are: id, name, price, discount, category", 400
        
        queryText = "SELECT * FROM product ORDER BY " + orderBy +";"
        data = dbQuery(queryText)

        if data == 400:
            return 'Sorry, database provider access error due to communication failure. Please check you internet connection and/or retry later.', 400
        
        result = []
        for row in data:
            line = {"id": row[0],"name":row[1],"url_image":row[2],"price":row[3],"discount":row[4],"category":row[5]}
            result.append(line)

        return result,200

def dbQuery(queryText):
    try:
        db = pymysql.connect(DB_HOST,DB_USER,DB_PASS,DB_NAME)
        cursor = db.cursor()
        cursor.execute(queryText)
        results = cursor.fetchall()
    except:
        print("Database connection error!")
        return 400
    return results


############
##  MAIN  ##
############

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
