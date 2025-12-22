from flask import Flask,request
from executeQuary import executeQuery
from executeSelectQuery import executeSelectQuery

server=Flask(__name__)

@server.get('/')
def home_page():
    return f"WELCOME.THIS IS HOME PAGE."

@server.post('/smart_home')
def create_data():
    device=request.form.get("device_name")
    light=request.form.get("light_status")
    fan=request.form.get("fan_status")
    temp=request.form.get("temp")

    query=f"insert into smart_home values('{device}','{light}','{fan}',{temp});"

    executeQuery(query=query)

    return "device is added successfully."

@server.get('/smart_home')
def get_data():
    query=f"select * from smart_home;"

    data=executeSelectQuery(query=query)

    return str(data)

@server.put('/smart_home')
def update_data():
    device=request.form.get("device_name")
    light=request.form.get("light_status")
    fan=request.form.get("fan_status")

    query=f"update smart_home SET light_status='{light}',fan_status='{fan}' where device_name='{device}';"

    executeQuery(query=query)

    return "device data updated successfully."

@server.delete('/smart_home')
def delete_data():
    device=request.form.get("device_name")

    query=f"delete from smart_home where device_name='{device}';"
    executeQuery(query=query)

    return "device deleted successfully."


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)
    