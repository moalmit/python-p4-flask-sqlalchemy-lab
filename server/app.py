#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.filter_by(id=id).first()
    return f'<ul>ID: {id}</ul><ul>Name: {animal.name}</ul><ul>Zookeeper: {animal.zookeeper.name}</ul><ul>Species: {animal.species}</ul><ul>Enclosure: {animal.enclosure.environment}</ul>'

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.filter_by(id=id).first()
    animal_list = [f'<ul>Animal: {animal.name}</ul>' for animal in zookeeper.animals]
    formatted_list = '\n'.join(animal_list)
    return f'<ul>ID: {id}</ul><ul>Name: {zookeeper.name}</ul><ul>Birthday: {zookeeper.birthday}</ul>{formatted_list}'

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.filter_by(id=id).first()
    animal_list = [f'<ul>Animal: {animal.name}</ul>' for animal in enclosure.animals]
    formatted_list = '\n'.join(animal_list)
    return f'<ul>ID: {id}</ul><ul>Environment: {enclosure.environment}</ul><ul>Open to Visitors: {enclosure.open_to_visitors}</ul>{formatted_list}'


if __name__ == '__main__':
    app.run(port=5555, debug=True)