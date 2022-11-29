from flask import Flask, url_for, redirect, render_template, request

app = Flask(__name__)
students = []


@app.route("/")
def index():
    return render_template("index.html", students=students)


@app.route("/addStudent", methods=["POST", "GET"])
def addStudent():
    if request.method == "POST":
        name = request.form['StudentName']
        students.append(name)
    return redirect(url_for('index'))


@app.route("/deleteStudent/<studentName>", methods=["POST", "GET"])
def deleteStudent(studentName):
    # if request.method == "POST":
    name = studentName
    students.remove(name)
    return redirect(url_for('index'))


@app.route("/moveDown/<studentName>")
def moveDown(studentName):
    ind = students.index(studentName)
    cur_item = students[ind]
    previous_item = students[ind + 1]

    students[ind + 1], students[ind] = cur_item, previous_item

    return redirect(url_for('index'))

@app.route("/moveUp/<studentName>")
def moveUp(studentName):
    ind = students.index(studentName)
    cur_item = students[ind]
    previous_item = students[ind - 1]

    students[ind - 1], students[ind] = cur_item, previous_item

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
