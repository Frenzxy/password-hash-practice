# import bcrypt
# from flask import Flask, render_template, request, app
# from db_postgre import authenticate_user


# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         login_username = request.form.get("username", "").strip()
#         login_password = request.form.get("password", "")
        

#         if authenticate_user(login_username, login_password):
#             return f"Login successful. Welcome, {login_username}!"

#         return render_template(
#             "login.html",
#             error="Invalid username or password.",
#         ), 401

#     return render_template("login.html")


