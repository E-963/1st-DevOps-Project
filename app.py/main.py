from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data for tasks (you can use a database in a real application)
tasks = [
    {'id': 1, 'task': 'work on my project'},
    {'id': 2, 'task': 'read quran'},
    {'id': 3, 'task': 'go to shopping'}

]

# Helper function to get task by ID
def get_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None

# Route to display index.html and handle task operations
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action') == 'add':
            new_task = request.form.get('task')
            tasks.append({'id': len(tasks) + 1, 'task': new_task})
        elif request.form.get('action') == 'edit':
            task_id = int(request.form.get('task_id'))
            edited_task = request.form.get('edited_task')
            task = get_task(task_id)
            if task:
                task['task'] = edited_task
        elif request.form.get('action') == 'delete':
            task_id = int(request.form.get('task_id'))
            task = get_task(task_id)
            if task:
                tasks.remove(task)

        return redirect(url_for('index'))  # Redirect to GET index to render updated tasks

    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run("0.0.0.0", port="8000" )
