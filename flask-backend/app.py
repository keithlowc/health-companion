from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.sql import func
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#db
db = SQLAlchemy(app)

#marshamllow
ma = Marshmallow(app)

class Data(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	time = db.Column(db.DateTime(timezone = True), default=func.now())
	bpm = db.Column(db.Float)
	bodyTemp = db.Column(db.Float)

	def __init__(self, bpm, bodyTemp):
		self.bpm = bpm
		self.bodyTemp = bodyTemp

# Product schema

class DataSchema(ma.Schema):
	class Meta:
		fields = ('id','time', 'bpm', 'bodyTemp')

# init schema
data_schema = DataSchema(strict=True)
all_data_schema = DataSchema(many=True ,strict=True)

@app.route('/data',methods=['POST'])
def add_data():
	bpm = request.json['bpm']
	bodyTemp = request.json['bodyTemp']

	new_data = Data(bpm,bodyTemp)
	db.session.add(new_data)
	db.session.commit()

	return data_schema.jsonify(new_data)

#Get all products
@app.route('/data', methods=['GET'])
def get_all_data():
	all_data = Data.query.all()
	result = all_data_schema.dump(all_data)
	return jsonify(result.data)

#Get one product
@app.route('/data/<id>', methods=['GET'])
def get_data(id):
	data = Data.query.get(id)
	return data_schema.jsonify(product)

#Update a product
@app.route('/data/<id>',methods=['PUT'])
def update_product(id):

	data = Data.query.get(id)

	bpm = request.json['bpm']
	bodyTemp = request.json['bodyTemp']

	data.bpm = bpm
	data.bodyTemp = bodyTemp

	db.session.commit()

	return data_schema.jsonify(data)

@app.route('/data/<id>', methods=['DELETE'])
def delete_products(id):
	data = Data.query.get(id)
	db.session.delete(data)
	db.session.commit()

	return data_schema.jsonify(data)


if __name__ == '__main__':
	app.run(debug=True)



