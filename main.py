import pymysql
from api_test import app
from config import mysql
from flask import jsonify
from flask import flash, request
from contextlib import closing

@app.route('/create', methods=['POST'])
def create_test():
    try:        
        _json = request.json
        _name = _json['name']
        _age = _json['age']
        
        if _name and _age and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)		
            sqlQuery = "INSERT INTO test(name, age) VALUES(%s, %s)"
            bindData = (_name, _age)            
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('added successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()          
     
@app.route('/test')
def test():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id, name, age FROM test")
        testRows = cursor.fetchall()
        respone = jsonify(testRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()  

@app.route('/update', methods=['PUT'])
def update_test():
    try:
        _json = request.json
        _id = _json['id']
        _name = _json['name']
        _age = _json['age']
       
        if _name and _age  and _id and request.method == 'PUT':			
            sqlQuery = "UPDATE test SET name=%s, age=%s WHERE id=%s"
            bindData = (_name, _age, _id,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('updated successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 

@app.route('/delete/', methods=['DELETE'])
def delete_test(id_test):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM test WHERE id =%s", (id_test,))
		conn.commit()
		respone = jsonify('deleted successfully!')
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
        
       
@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone
        
if __name__ == "__main__":
    app.run()