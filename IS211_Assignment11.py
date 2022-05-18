from flask import Flask, render_template, redirect, request
import re

todo_list = [
    [1, "buy some food", "email@google.com", "High"],
    [2, "do some chores", 'yahoo@microsoft.com', "Medium"],
    [3, "shop for clothes", "none@nothing.net", "Low"]

]
error_msg = ""
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', todo_list=todo_list, error_message=error_msg)


@app.route('/submit', methods=['POST'])
def submit():
    task = request.form["Task"]
    email = request.form["Email"]
    priority = request.form["Priority"]
    if todo_list != []:
        temp_list = max(todo_list)
        new_int = int(temp_list[0]) + 1
    else:
        new_int = 1
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if re.fullmatch(regex, email):
        if priority in ("Low", "Medium", "High"):
            todo_list.append([new_int, task, email, priority])
            error_msg = ""
            return redirect('/')
        else:
            error_msg = "Please select a priority"
    else:
        error_msg = "Invalid Email"
    return render_template('index.html', todo_list=todo_list, error_message=error_msg)


@app.route('/delete', methods=['POST'])
def delete():
    temp_id = int(request.form["ID"])
    my_count = 0
    for i in todo_list:
        if i[0] == temp_id:
            break
        else:
            my_count += 1
    del todo_list[my_count]
    print(my_count)
    return redirect('/')


@app.route('/clear', methods=['POST'])
def clear():
    todo_list.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
