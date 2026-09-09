# from base_register import register
# from db_postgre import authenticate_user, create_user, initialize_database

# initialize_database()

# while True:
#     user, email, password = register()
#     try:
#         create_user(user, email, password)
#         print("User registered successfully.")
#         break
#     except Exception as error:
#         if "duplicate key" in str(error).lower():
#             print("That username or email is already registered. Try again.")
#         else:
#             raise

# while True:
#     login_username = input("Introduce your username: ").strip()
#     login_password = input("Introduce your password: ")
#     if authenticate_user(login_username, login_password):
#         print(f"Welcome: {login_username}")
#         break
#     print("Invalid username or password, try again!")


