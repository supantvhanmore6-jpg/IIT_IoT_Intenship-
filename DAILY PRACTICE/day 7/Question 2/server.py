from flask import Flask,request
from executeQuery import executeQuery
from executeSelectQuery import executeSelectQuery
from datetime import datetime

server=Flask(__name__)

@server.get('/')
def homepage():
    return "Welcome.This is home page."

@server.post('/iot')
def create_data():
    id=request.form.get("id")
    moisture=request.form.get("moisture")

    query=f"insert into  smart_agriculure values({id},{moisture},'{datetime.now()}');"
    executeQuery(query=query)

    return "data is added successfully"

@server.put('/iot')
def update_data():
    id=request.form.get('id')
    moisture=request.form.get('moisture')
    query=f"update  smart_agriculure SET moisture_lvl={moisture} where id={id};"

    executeQuery(query=query)

    return "moisture is updated successfully"

@server.get('/iot')
def get_data():
    query=f"select * from  smart_agriculure; "

    data=executeSelectQuery(query=query)
    
    return str(data)

@server.delete('/iot')
def delete_data():
    id=request.form.get('id')

    query=f"delete from  smart_agriculure where id={id};"

    executeQuery(query=query)

    return "data deleted successfully"

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)
