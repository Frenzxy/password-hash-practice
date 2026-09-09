import re, bcrypt
from flask import Flask, render_template, request, redirect

from db_postgre import authenticate_user, create_user, initialize_database

app = Flask(__name__)

user_pattern = r"^[A-Za-z0-9_.-]{3,30}$"
email_pattern = r"^[A-Za-z0-9._%+-ñ]+@(gmail|hotmail|outlook)\.[A-Za-z]{2,}$"
password_pattern = r"^(?=.*[A-Za-z])(?=.*\d).{8,}$"



@app.route("/", methods=["GET", "POST"])
def registro():
    error = None
    username = ""
    email = ""

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        is_valid = (
            re.fullmatch(user_pattern, username)
            and re.fullmatch(email_pattern, email)
            and re.fullmatch(password_pattern, password)
        )

        if is_valid:
            try:
                salt = bcrypt.gensalt()
                hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt).decode("ascii")
                create_user(username, email, hashed_password)
                return redirect("/login")
            except Exception as database_error:
                if "duplicate key" in str(database_error).lower():
                    error = "The username or email is already registered."
                else:
                    error = "Could not save the user. Please try again."
        if error is None:
            error = "Invalid input. Please check your username, email and password."
        
    return render_template(
        "registro.html",
        error=error,
        username=username,
        email=email,
    )
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login_username = request.form.get("username", "").strip()
        login_password = request.form.get("password", "")
        

        if authenticate_user(login_username, login_password):
            return f"Login successful. Welcome, {login_username}!"

        return render_template(
            "login.html",
            error="Invalid username or password.",
        ), 401

    return render_template("login.html")

if __name__ == "__main__":
    initialize_database()
    app.run(debug=False, use_reloader=False)


