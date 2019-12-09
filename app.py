from flask import Flask,render_template, request, redirect, url_for

import os
project_dir = os.path.dirname(os.path.abspath(__file__))
myApp =  Flask(__name__)
myApp.secret_key = 'my school app'

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "schooldb.db"))

myApp.config["SQLALCHEMY_DATABASE_URI"] = database_file
myApp.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(myApp)

#db.create_all()

class User(db.Model):
    name = db.Column(db.String(40), nullable=False, primary_key = True)
    password = db.Column(db.String(40),unique=False, nullable=False)
    role = db.Column(db.String(40),unique=False, nullable=False)

#db.create_all()

#@myApp.route('/admin')
#def admin():
#    user1 = User()
#    user1.name = 'admin'
#    user1.password = 'admin'
#    user1.role = 'admin'
#    db.session.add(user1)
#    db.session.commit()
#    return render_template('admin.html')

@myApp.route('/adminlogin')
def adminlogin():
    return render_template('adminlogin.html')

@myApp.route('/admindashboard')
def admindashboard():
    users = User.query.all()
    return render_template('adminDashboard.html',users=users)

@myApp.route('/login')
def loging():
    return render_template('login.html')

@myApp.route('/account')
def account():
    return render_template('account.html')


@myApp.route('/doLogin',methods=['post'])
def doLogin():
    user = User.query.filter_by(name=request.form['username']).first()
    print(user)
    if user and user.password == request.form['password']:        
        return redirect(url_for('account')) 

    return render_template('login.html')

@myApp.route('/')
def index():
    return render_template('index.html')

@myApp.route('/processLogin',methods=['post'])
def processLogin():
    user = User.query.filter_by(name='admin').first()
    if user.password == request.form['password']:
        users = User.query.all()
        return redirect(url_for('admindashboard')) 

    return render_template('adminlogin.html')

@myApp.route('/addUser',methods=['post'])
def addUser():
    user1 = User()
    user1.name = request.form['username']
    user1.password = user1.name + '123'
    user1.role = request.form['role']
    db.session.add(user1)
    db.session.commit()    
    return redirect(url_for('admindashboard'))    

@myApp.route('/deleteuser',methods=['post'])
def deleteuser():
    user = User.query.filter_by(name=request.form['username']).first()
    if user:        
        db.session.delete(user)
        db.session.commit() 
    return redirect(url_for('admindashboard')) 

@myApp.route('/updateuser',methods=['post'])
def updateuser():
    user = User.query.filter_by(name=request.form['username']).first()
    if user:        
        user.password = request.form['username']
        user.role = request.form['role']
        db.session.commit() 
    return redirect(url_for('admindashboard')) 

@myApp.route('/logout')
def logout():
    return render_template('index.html')

if __name__ == "__main__":
    myApp.run(debug=True)


