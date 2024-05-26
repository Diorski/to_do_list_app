import unittest
from app import app, db, Task

class ToDoTestCase(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        self.app.testing = True
        
        # Create an in-memory database
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.create_all()

    def tearDown(self):
        # Clean up the database
        db.session.remove()
        db.drop_all()

    def test_add_task(self):
        response = self.app.post('/add', data=dict(task='Test Task'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Task', response.data)

    def test_delete_task(self):
        task = Task(task='Test Task')
        db.session.add(task)
        db.session.commit()
        response = self.app.get(f'/delete/{task.id}', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Test Task', response.data)

    def test_edit_task(self):
        task = Task(task='Test Task')
        db.session.add(task)
        db.session.commit()
        response = self.app.post(f'/edit/{task.id}', data=dict(task='Updated Task'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Updated Task', response.data)
        self.assertNotIn(b'Test Task', response.data)

    def test_complete_task(self):
        task = Task(task='Test Task')
        db.session.add(task)
        db.session.commit()
        response = self.app.get(f'/complete/{task.id}', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'style="text-decoration: line-through;"', response.data)

    def test_incomplete_task(self):
        task = Task(task='Test Task', completed=True)
        db.session.add(task)
        db.session.commit()
        response = self.app.get(f'/incomplete/{task.id}', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'style="text-decoration: line-through;"', response.data)

if __name__ == '__main__':
    unittest.main()
