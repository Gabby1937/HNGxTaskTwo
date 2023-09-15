import unittest
import json
from app import app, db, Person

class APITestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://master:ekka@localhost:5432/testdb'  # Use a separate test database
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()  # Push the application context
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()  # Pop the application context

    def test_create_person(self):
        response = self.app.post('/api', data=json.dumps({'name': 'John Doe'}), content_type='application/json')
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['message'], 'Person created successfully')

    def test_create_person_missing_name(self):
        response = self.app.post('/api', data=json.dumps({}), content_type='application/json')
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Name is required')

    def test_get_person(self):
        person = Person(name='Alice')
        db.session.add(person)
        db.session.commit()

        response = self.app.get(f'/api/persons/{person.id}')
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['id'], person.id)
        self.assertEqual(data['name'], person.name)

    def test_get_person_not_found(self):
        response = self.app.get('/api/persons/999')
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['error'], 'Person not found')

    def test_update_person(self):
        person = Person(name='Bob')
        db.session.add(person)
        db.session.commit()

        response = self.app.put(f'/api/persons/{person.id}', data=json.dumps({'name': 'Updated Bob'}), content_type='application/json')
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Person updated successfully')

        updated_person = Person.query.get(person.id)
        self.assertEqual(updated_person.name, 'Updated Bob')

    def test_delete_person(self):
        person = Person(name='Eve')
        db.session.add(person)
        db.session.commit()

        response = self.app.delete(f'/api/persons/{person.id}')
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Person deleted successfully')

        deleted_person = Person.query.get(person.id)
        self.assertIsNone(deleted_person)

    def test_delete_person_not_found(self):
        response = self.app.delete('/api/persons/999')
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['error'], 'Person not found')

if __name__ == '__main__':
    unittest.main()
