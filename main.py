from flask import Flask, render_template

app = Flask(__name__)

# Placeholder task list (replace with actual logic)
tasks = []

@app.route('/')
def index():
  return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
  app.run('0.0.0.0', 3000)
