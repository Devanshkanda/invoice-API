# invoice-API
this is an invoice api.

## Setup the project

Clone the git repository into your local system
```
git clone https://github.com/Devanshkanda/invoice-API.git
```


Create your python virtual environment

type virtualenv for python3.8 version else use venv for versions above 3.8
```
python3 -m (virtualenv or venv) <name of your environment>
```

Activate virtual environment (for MacOS or Linux)
```
source env/bin/activate
```

Install python libraries using the requirements.txt file
```
pip install -r requirements.txt
```

Run the django server
```
python3 manage.py runserver
```
Done setting Up the project..
your project is running on your localhost on port No 8000

# Naviagating to API Endpoints

## Get Request

http method GET Request
```
http:127.0.0.1:8000/api/invoice/
```

Response
![image](https://github.com/Devanshkanda/invoice-API/assets/101200047/af93b524-ac4a-4129-bd5d-30f0a615ce74)

## GET Request by ID

http method: GET Request with id 
```
http:127.0.0.1:8000/api/invoice/<invoice id>/
```

Response
![image](https://github.com/Devanshkanda/invoice-API/assets/101200047/f782c035-43bd-4e42-8376-8703909a30c0)


## POST Request

http method: POST Request
```
http:127.0.0.1:8000/api/invoice/
```

request body: it should contain keys: customer_name, desc (descriptiion), quantity, unit_price
total price will be calculated automatically
```
Sample Data

{
    "customer_name": "harsh",
    "desc": "invoice of Dominos. ordered cheeze burst pizza",
    "quantity": 2,
    "unit_price": 250
}
```

Response
![image](https://github.com/Devanshkanda/invoice-API/assets/101200047/c6db016f-e980-4ebb-a7a6-416b9a792b39)

## PUT Request

http method: PUT Request. 

important: invoice id should need to be passed in the URL to update the information

```
http:127.0.0.1:8000/api/invoice/76f4e645-f4cb-449b-8db7-9214aadd8c9f/
```

Request body: it should contain any of the mentioned keys, combinations or all: customer_name, desc (descriptiion), quantity, unit_price

```
Before Updating:

{
    "customer_name": "harsh",
    "desc": "invoice of Dominos. ordered cheeze burst pizza",
    "quantity": 2,
    "unit_price": 250
}

After updating:

{
    "customer_name": "harsh",
    "desc": "invoice of Dominos. ordered cheeze burst pizza and Margarita cheeze pizza",
    "quantity": 3,
    "unit_price": 255,
    "invoice": "76f4e645-f4cb-449b-8db7-9214aadd8c9f" (invoice id of the person)
}
```

Response
![image](https://github.com/Devanshkanda/invoice-API/assets/101200047/2977fdb1-5982-4f40-a0a2-6abdf73e8e21)

## DELETE Request

http method: DELETE

important: pass the invoice id in the URL to delete the invoice

```
http:127.0.0.1:8000/api/invoice/76f4e645-f4cb-449b-8db7-9214aadd8c9f/
```

Response
![image](https://github.com/Devanshkanda/invoice-API/assets/101200047/a0ad62e2-3773-4677-9122-c72bde6d29d8)
