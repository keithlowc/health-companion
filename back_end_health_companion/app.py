from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.sql import func
from flask_heroku import Heroku
from flask_cors import CORS

import os

app = Flask(__name__)

# Comment this out for deployment
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)

heroku = Heroku(app)

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

@app.route('/', methods=['GET'])
def initial():
	return ''' <h1>Backend for Health Companion</h1>
	<h2>Created by Keith Low for healthcompanionfev1.herokuapp.com</h2>
	<ul>
		<li>Routes</li>
		<h2>healthCompanion.herokuapp.com/data</h2>
		<li>Shows all the data saved into the db</li>
		<h2>healthCompanion.herokuapp.com/data/1</h2>
		<li>Shows the piece of data with id 1</li>
		<h2>healthCompanion.herokuapp.com/data/averages</h2>
	</ul>

	'''


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
	return data_schema.jsonify(data)

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

@app.route('/data/averages', methods=['GET'])
def get_averages():
	all_data = Data.query.all()
	result = all_data_schema.dump(all_data)
	total_bpm = 0
	total_temperature = 0

	for x in range(len(result.data)):
		total_bpm += result.data[x]['bpm']
		total_temperature += result.data[x]['bodyTemp']

	total_bpm = total_bpm / len(result.data)
	total_temperature = total_temperature / len(result.data)

	return jsonify({
		'average_bpm': total_bpm,
		'average_temp': total_temperature,
		})


if __name__ == '__main__':
	app.run(debug=True)



