"""
This module sets up a basic Flask web application with a single route to render the index page.
"""

from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the index page.
    
    Returns:
        str: The rendered HTML template for the index page.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', 3000)


