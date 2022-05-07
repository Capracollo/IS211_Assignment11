from flask import Flask, render_template, redirect, request
import re

todo_list = [
    [1, "Buy Eggs", "email@google.com", "High"],
    [2, "Buy Milk", "none@such.net", "Low"],
    [3, "Buy Chicken", 'micro@microsoft.com', "Med"]
]

error_message = ""

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', todo_list=todo_list, error_message=error_message)


@app.route('/submit', methods=['POST'])
def submit():
    task = request.form["Task"]
    email = request.form["Email"]
    priority = request.form["Priority"]
    if todo_list != []:
        templist = max(todo_list)
        new_int = int(templist[0]) + 1
    else:
        new_int = 1
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if (re.fullmatch(regex, email)):
        if priority in ("Low", "Med", "High"):
            todo_list.append([new_int, task, email, priority])
            return redirect('/')
        else:
            error_message = "Please select a priority"
    else:
        error_message = "Invalid Email"
    return render_template('index.html', todo_list=todo_list, error_message=error_message)


@app.route('/delete', methods=['POST'])
def delete():
    tempID = int(request.form["ID"])
    mycount = 0
    for i in todo_list:
        if i[0] == tempID:
            break
        else:
            mycount += 1
    del todo_list[mycount]
    print(mycount)
    return redirect('/')


@app.route('/clear', methods=['POST'])
def clear():
    todo_list.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)