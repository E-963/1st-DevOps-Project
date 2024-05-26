import test_ToDOlist
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates')

todos = []
class TodoListTest(test_ToDOlist.TestCase):

    def setUp(self):
        self.app = app
        self.app.testing = True
        self.client = self.app.test_client()
        # Clear todos for each test
        todos.clear()

    def tearDown(self):
        pass  # No specific cleanup needed

    def test_index_renders_todos(self):
        # Add some todos
        todos.append({'task': 'Buy milk', 'done': False})
        todos.append({'task': 'Finish report', 'done': True})

        # Get the index page
        response = self.client.get('/')

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # Check that todos are rendered in the template
        self.assertIn(b'Buy milk', response.data)
        self.assertIn(b'Finish report (Done)', response.data)  # Check for "Done" mark

    def test_add_todo(self):
        # Add a new todo
        response = self.client.post('/add', data={'todo': 'Call mom'})

        # Check that the redirect is successful
        self.assertEqual(response.status_code, 302)

        # Check that the new todo is added
        self.assertEqual(todos[0]['task'], 'Call mom')

        # Check that the user is redirected to the index page
        self.assertEqual(response.location, url_for('index'))

    def test_edit_todo_get(self):
        # Add a todo
        todos.append({'task': 'Write blog post', 'done': False})

        # Get the edit page for the first todo
        response = self.client.get('/edit/0')

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # Check that the todo pre-populates the edit form
        self.assertIn(b'Write blog post', response.data)

    def test_edit_todo_post(self):
        # Add a todo
        todos.append({'task': 'Clean the house', 'done': False})

        # Edit the first todo
        response = self.client.post('/edit/0', data={'todo': 'Clean the attic'})

        # Check that the redirect is successful
        self.assertEqual(response.status_code, 302)

        # Check that the todo is updated
        self.assertEqual(todos[0]['task'], 'Clean the attic')

        # Check that the user is redirected to the index page
        self.assertEqual(response.location, url_for('index'))

    def test_check_todo(self):
        # Add a todo
        todos.append({'task': 'Go for a walk', 'done': False})

        # Check the first todo
        response = self.client.get('/check/0')

        # Check that the redirect is successful
        self.assertEqual(response.status_code, 302)

        # Check that the todo is marked as done
        self.assertEqual(todos[0]['done'], True)

        # Check that the user is redirected to the index page
        self.assertEqual(response.location, url_for('index'))

    def test_delete_todo(self):
        # Add some todos
        todos.append({'task': 'Pay bills', 'done': False})
        todos.append({'task': 'Grocery shopping', 'done': True})

        # Delete the second todo
        response = self.client.get('/delete/1')

        # Check that the redirect is successful
        self.assertEqual(response.status_code, 302)

        # Check that the second todo is deleted
        self.assertEqual(len(todos), 1)
        self.assertEqual(todos[0]['task'], 'Pay bills')

        # Check that the user is redirected to the index page
        self.assertEqual(response.location, url_for('index'))

if __name__ == '__main__':
    test_ToDOlist.main()
