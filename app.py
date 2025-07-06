from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_note', methods=['POST'])
def add_note():
    title = request.form.get('title')
    if title:
        tasks.append({'title': title, 'color': "#d7abea", 'items': []})
    return redirect(url_for('index'))

@app.route('/add_item/<int:task_id>', methods=['POST'])
def add_item(task_id):
    item = request.form.get('item')
    if item and 0 <= task_id < len(tasks):
        tasks[task_id]['items'].append(item)
    return redirect(url_for('index'))

@app.route('/change_color/<int:task_id>/<color>')
def change_color(task_id, color):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['color'] = color
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
