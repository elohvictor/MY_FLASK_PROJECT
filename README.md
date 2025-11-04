  ****FLASK API - STOCK MANAGEMENT****
  
**Overview**

A simple flask-based REST API that allows you to perform basic **CRUD operation**(Create, read, update and delete)for managing stock invenory. \

This project demonstrates the basics of CRUD operation using python and flask.  

**Features**
  - **Create** a new item
  - **Retrieve** all or each item
  - **Update** an existing item
  - **Delete** an item

**Technologies Used**

 -Flask(for building API)
 
 -Postman(for testing endpoint)

**Setup Instructions**

 1. Create and activate a virtual environment:
    
    python3 -m venv venv
    
    source venv/bin/activate

 3. Install Flask:
    
    pip install flask

 3.Run the application:
 
   python3 <file-name>

4. The API will start running at:
   
    http://127.0.0.1:5000

Testing endpoint with(Postman)

  1.Retrieve item (GET)
  
  -URL:http://127.0.0.1:5000/item/1
    
  -Method:GET
    
  -Respnse Example:
  
      {
        "id": 1,
        "name": "corn",
        "quantity": 10,
        "total_price": 650000,
        "unit_price": 65000,
        "description": "50kg bag of corn"
      }


  2.Create a new item (POST)
  
  -URL:http://127.0.0.1:5000/items/add
  
  -Method:POST
  
  -Body(raw JSON):
  
      {
        "name": "corn",
        "quantity": 10,
        "unit_price": 65000,
        "description": "50kg bag of corn"
      }
      
    -Response:
    
      {
          "id": 2,
          "name": "Beans",
          "quantity": 10,
          "total_price": 650000,
          "unit_price": 65000,
          "description": "50kg bag of beans"
      }

  3.Update an item (PUT)
  
  -URL: http://127.0.0.1:5000/items/1
  
  -Method: PUT
  
  -Body (raw JSON):
  
      {
        "name": "Beans",
        "quantity": 10,
        "unit_price": 65000,
        "description": "50kg bag of beans"
      }
      
    -Response:
    
      {
        "id": 1,
        "name": "Beans",
        "quantity": 10,
        "total_price": 650000,
        "unit_price": 65000,
        "description": "50kg bag of beans"
      }


  4. Delete an item (DELETE)
     
    -URL: http://127.0.0.1:5000/items/1
    
    -Method: DELETE
    
    -Response:
    
       {
        "message": "Item with id 1 deleted successfully"
       }



Notes

-All data is stored in memory — restarting the server resets it.

-Use a database (like SQLite or PostgreSQL) for persistence.

-You can extend this project using Flask-RESTful or FastAPI for more features.


Author

Name: Eloh Victor
