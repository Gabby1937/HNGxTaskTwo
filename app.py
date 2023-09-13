from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://master:ekka@localhost:5432/HNGxtasktwodb'
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
@app.route('/api/persons', methods=['POST'])
def create_person():
    data = request.json
    name = data.get('name')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    person = Person(name=name)
    db.session.add(person)
    db.session.commit()
    return jsonify({'message': 'Person created successfully', 'id': person.id}), 201

# READ
@app.route('/api/persons/<int:person_id>', methods=['GET'])
def get_person(person_id):
    person = Person.query.get(person_id)
    if not person:
        return jsonify({'error': 'Person not found'}), 404

    return jsonify({'id': person.id, 'name': person.name})

# UPDATE
@app.route('/api/persons/<int:person_id>', methods=['PUT'])
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
@app.route('/api/persons/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    person = Person.query.get(person_id)
    if not person:
        return jsonify({'error': 'Person not found'}), 404

    db.session.delete(person)
    db.session.commit()
    return jsonify({'message': 'Person deleted successfully'})

if __name__ == "__main__":
    app.run(debug=True)

