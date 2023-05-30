from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# Lista de tareas
tasks = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Obtener los datos del formulario
        task_name = request.form['taskName']
        description = request.form['description']
        deadline = request.form['deadline']
        
        # Crear un diccionario con los datos de la tarea
        task = {
            'task_name': task_name,
            'description': description,
            'deadline': deadline,
            'completed': False
        }
        
        # Agregar la tarea a la lista
        tasks.append(task)
        
    completed_tasks_count = len([task for task in tasks if task['completed']])
    overdue_tasks_count = len([task for task in tasks if not task['completed'] and task['deadline'] < datetime.now().strftime('%Y-%m-%d')])
    
    return render_template('home.html', tasks=tasks, completed_tasks_count=completed_tasks_count, overdue_tasks_count=overdue_tasks_count)

@app.route('/complete/<int:index>')
def complete_task(index):
    if index < len(tasks):
        tasks[index]['completed'] = True
    completed_tasks_count = len([task for task in tasks if task['completed']])
    overdue_tasks_count = len([task for task in tasks if not task['completed'] and task['deadline'] < datetime.now().strftime('%Y-%m-%d')])
    return render_template('home.html', tasks=tasks, completed_tasks_count=completed_tasks_count, overdue_tasks_count=overdue_tasks_count)

@app.route('/delete/<int:index>')
def delete_task(index):
    if index < len(tasks):
        del tasks[index]
    completed_tasks_count = len([task for task in tasks if task['completed']])
    overdue_tasks_count = len([task for task in tasks if not task['completed'] and task['deadline'] < datetime.now().strftime('%Y-%m-%d')])
    return render_template('home.html', tasks=tasks, completed_tasks_count=completed_tasks_count, overdue_tasks_count=overdue_tasks_count)

if __name__ == '__main__':
    app.run()
