from flask import Flask, json, jsonify, render_template, request, redirect, url_for

app = Flask(__name__)

data = [{"id": 1, "name": "Buy groceries", "description": "task 1"},
         {"id": 2, "name": "Clean the house", "description": "task2"}]

@app.route('/')
def index():
    return "wel-Come to ToDo APP"

#get all the item
@app.route('/items', methods=['GET'])
def GetItems():
    return jsonify(data)

# get specific item by id
@app.route('/items/<int:item_id>' , methods=['GET'])
def GetItemById(item_id):
    print(item_id)
    item = [item for item in data if item['id'] == item_id]
    if item is None:
        raise jsonify({'error': "item not found"})
    return jsonify(item)

#post: create  a new task

@app.route('/items', methods=['POST'])
def AddTask():
    if not request.json or not 'name' is  request.json:
        return jsonify({"error": "item not found"})
    new_item = {
        "id" : data[-1]["id"] +1 if data else 1,
        "name" : request.json['name'],
        "description" : request.json['description']
    }
    data.append(new_item)
    return jsonify(data)

# Update task item 
@app.route('/items/<int:id>', methods=['PUT'])
def UpdateTask(id):
    item = next([item for item in data if item['id'] == id], None)
    if item is None:
        return jsonify({'error' : "item not found"})
    item['name']= request.json.get('name', item['name'])
    item['description']= request.json.get('description', item['description'])
    return jsonify(item)

#delete item
@app.route('/items/<int:id>', methods=['DELETE'])
def DeleteTask(id):
    global data
    item = [item for item in data if item['id'] != id]
    return jsonify({'result': "itme deleted"})


if __name__ == '__main__':
    app.run(debug=True)