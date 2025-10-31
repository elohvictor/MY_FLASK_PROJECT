from flask import Flask , request , jsonify

app = Flask(__name__)

items = [
    # {
    # "name": "Rice",
    # "quantity": 10,
    # "unit_price": 65000,
    # "total_price": 650000,
    # "description": "50kg bag of rice"
    # }
]
item_id_counter = 1

#retrieving item
@app.route('/item/all',methods=['GET'])
def retrieve_all_item():
    if not items:
        return "Empty item"
    return items

#add new item

@app.route('/items/add', methods=['POST'])
def create_item():
    global item_id_counter  

    data = request.get_json()  
    # return data
    new_item = {
        "id": len(items) + 1,
        'name': data['name'],
        'quantity': data.get('quantity', 1),
        'unit_price': data['unit_price'],
        'description': data.get('description', ''),
        'total_price': data['quantity'] * data['unit_price']
    }

    items.append(new_item)
    return new_item


#retrieving single items
@app.route('/item/<int:item_id>', methods=['GET'])
def retrieve_item(item_id):
    single_item = next((item for item in items if item['id'] == item_id), None)
    if single_item:
        return jsonify(single_item)
    return ({"Error" : "Item not found"})


#Update item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    for item in items:
        if item['id'] == item_id:
            
            item['name'] = data.get('name', item['name'])
            item['description'] = data.get('description', item['description'])
            item['quantity'] = data.get('quantity', item['quantity'])
            item['unit_price'] = data.get('unit_price', item['unit_price'])
            item['total_price'] = data.get('total_price', item['total_price'])
            return jsonify(item)
        
    return ({"Error" : "Item not found"})


#delete item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    item = next((d for d in items if d['id'] == item_id), None)
    
    if item:
        items =[d for d in items if d['id'] != item_id]
        return jsonify({"message": f"Item with id {item_id} deleted successfully"})
    else:
        return jsonify({"error": "Item not found"})