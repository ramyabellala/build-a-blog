from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too
tasks= []
@app.route("/" , methods=['POST', 'GET'])
def index():

    if request.method =='POST':
        task = request.form['task']
        tasks.append(task)

    return render_template("todo.html",title="build a blog" , tasks=tasks)

app.run()

