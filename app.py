from flask import Flask, render_template,request,redirect,url_for
from flask_mysqldb import MySQL
from config import config
app=Flask(__name__)
app.config.from_object(config)
mysql = MySQL(app)
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students")
    record = cur.fetchall()
    cur.close()
    return render_template('index.html', data=record)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method=="POST":
        name = request.form['name']
        email = request.form['email']
        ph = request.form['phone']
        courses = request.form['courses']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students (name, email, phone, course) VALUES (%s, %s, %s, %s)",(name,email,ph,courses))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))
    return render_template('add.html')
@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/edit')
def edit():
    return render_template('edit.html')

if __name__ == '__main__':
    app.run(debug=True)