from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://master:ekka@localhost:5432/HNGxtasktwodb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lxamjnofkexhwg:297496fa748dfba9d88b5fb241cd6e647e5318d0fcfbfc8003b7f51df4b1d39b@ec2-3-210-173-88.compute-1.amazonaws.com:5432/d8do2osfmr5e5q'
#"postgres://lxamjnofkexhwg:297496fa748dfba9d88b5fb241cd6e647e5318d0fcfbfc8003b7f51df4b1d39b@ec2-3-210-173-88.compute-1.amazonaws.com:5432/d8do2osfmr5e5q"
db = SQLAlchemy(app)

# Define your SQLAlchemy models (e.g., Person) here.

# Create the database tables
with app.app_context():
    db.create_all()

# Define the Person model
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    def __init__(self, name):
        self.name = name

# Define routes and CRUD operations here.


##############################

# CREATE
@app.route('/api', methods=['POST'])
def create_person():
    data = request.json
    name = data.get('name')

    if not name:
        return jsonify({'error': 'Name is required'}), 400
    
    if not isinstance(name, str):
        return jsonify({'error': 'Name should be a string'}), 400

    person = Person(name=name)
    db.session.add(person)
    db.session.commit()
    return jsonify({'message': 'Person created successfully', 'id': person.id}), 201

# READ
@app.route('/api/<int:person_id>', methods=['GET'])
def get_person(person_id):
    person = Person.query.get(person_id)
    if not person:
        return jsonify({'error': 'Person not found'}), 404

    return jsonify({'id': person.id, 'name': person.name})

# UPDATE
@app.route('/api/<int:person_id>', methods=['PUT'])
def update_person(person_id):
    data = request.json
    name = data.get('name')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    person = Person.query.get(person_id)
    if not person:
        return jsonify({'error': 'Person not found'}), 404

    person.name = name
    db.session.commit()
    return jsonify({'message': 'Person updated successfully'})

# DELETE
@app.route('/api/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    person = Person.query.get(person_id)
    if not person:
        return jsonify({'error': 'Person not found'}), 404

    db.session.delete(person)
    db.session.commit()
    return jsonify({'message': 'Person deleted successfully'})

if __name__ == "__main__":
    app.run(debug=True)

