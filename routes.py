# from app import myApp
# from flask import render_template, request
#
# @myApp.route('/')
# def index():
#     return render_template('index.html')
#
# @myApp.route('/login')
# def login():
#     return render_template('login.html')
#
#     #return "<h1>Hello login!</h1><h1>Hello login!</h1><h1>Hello login!</h1>"
#
# @myApp.route('/test1', methods=["POST", "GET"])
# def mySignup():
#     # print(request.form['username'])
#
#     if request.method == "POST":
#         user1 = User()
#         user1.name = request.form['username']
#         user1.password = request.form['pass']
#         user1.city = request.form['city']
#
#         db.session.add(user1)
#         db.session.commit()
#
#     return render_template('signup.html')
#
