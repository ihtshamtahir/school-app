from flask import Flask,render_template, request

print(__file__)

import os
project_dir = os.path.dirname(os.path.abspath(__file__))
myApp =  Flask(__name__)

print(project_dir)


from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))

myApp.config["SQLALCHEMY_DATABASE_URI"] = database_file
myApp.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False



db = SQLAlchemy(myApp)

# db.create_all()

class User(db.Model):
    name = db.Column(db.String(40), nullable=False, primary_key = True)
    password = db.Column(db.String(40),unique=False, nullable=False)
    role = db.Column(db.String(40),unique=False, nullable=False)

# db.create_all()

@myApp.route('/admin')
def admin():
    user1 = User()
    user1.name = request.form['username']
    user1.password = 'admin'
    user1.role = 'admin'
    return render_template('admin.html')

@myApp.route('/users')
def users():
    myUsers = User.query.all()
    return render_template('users.html', users=myUsers)

@myApp.route('/delete', methods=["POST"])
def delete_user():
    user_name = request.form['target_user']

    user_found = User.query.filter_by(name=user_name).first()

    db.session.delete(user_found)
    db.session.commit()

    myUsers = User.query.all()

    return render_template('users.html', users=myUsers)

@myApp.route('/')
def index():
    return render_template('index.html')

@myApp.route('/login')
def login():
    return render_template('login.html')

    #return "<h1>Hello login!</h1><h1>Hello login!</h1><h1>Hello login!</h1>"

@myApp.route('/test1', methods=["POST", "GET"])
def mySignup():
    # print(request.form['username'])

    if request.method == "POST":
        user1 = User()
        user1.name = request.form['username']
        user1.password = request.form['pass']
        user1.city = request.form['city']

        db.session.add(user1)
        db.session.commit()

    return render_template('signup.html')


# print(__name__)

if __name__ == "__main__":
    myApp.run(debug=True)


