from flask import Flask, jsonify, request, jsonify, Response
from flask_pymongo import PyMongo
from bson import json_util
from datetime import datetime
import string
import random

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://root:root@backend.sdlbn.mongodb.net/test"
mongo = PyMongo(app)

@app.route('/user', methods=['POST'])
def create_user():
  #Recebe dados
  data = request.json
  name = request.json['name']
  company = request.json['company']
  amount_products = request.json['amount_products']
  #Criando um ID aleatório de 16 caracteres
  id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16)) 
  #Pegando a data e hora no momento da criação
  date = datetime.now()
  created_at = datetime.isoformat(date)

  data['id'] = id
  data['created_at'] = created_at

  if name and company and amount_products:
    user = mongo.db.users.insert_one(request.json)

    response = {
      '_id': str(user.inserted_id),
      'id': id,
      'name': name,
      'company': company,
      'created_at': created_at,
      'amount_products': amount_products
    }
  
    return response
  else:
    bad_request()

@app.route('/user', methods=['GET'])
def list_users():
  users = mongo.db.users.find()
  response = json_util.dumps(users)
  return Response(response, mimetype='application/json')

@app.route('/user/<id>', methods=['GET'])
def list_user(id):
  user = mongo.db.users.find_one({ 'id': id })
  response = json_util.dumps(user)
  return Response(response, mimetype='application/json')

@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
  mongo.db.users.delete_one({ 'id': id })
  response = jsonify({
    'message': 'User deleted'
  })
  return response

@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
  data = request.json
  name = request.json['name']
  company = request.json['company']
  amount_products = request.json['amount_products']

  if name and company and amount_products:
    user = mongo.db.users.update_one({ 'id': id },
    {'$set': data })

    response = {
      'id': id,
      'name': name,
      'company': company,
      'amount_products': amount_products
    }
    return response

@app.errorhandler(400)
def bad_request(error=None):
  response = jsonify({
    'message': 'Bad Request: ' + request.url,
    'status': 400
  })
  response.status_code = 400
  return response

@app.errorhandler(404)
def not_found(error=None):
  response = jsonify({
    'message': 'Resource Not Found: ' + request.url,
    'status': 404
  })
  response.status_code = 404
  return response

if __name__ == "__main__":
  app.run()

