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

if __name__ == '__main__':
    test_ToDOlist.main()
