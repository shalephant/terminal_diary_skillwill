class SignOptions:
    def __init__(self):
        self.users = []

    def register(self, user, password):
        self.users.append({"username": user,
                           "password": password})
        with open(f"{user}_diary", "w") as file:
            file.write(f"User: {user} Password: {password}")



    def check_login(self, username, password):
        if len(self.users) == 0:
            print("No accounts registered")
        else:
            for each in self.users:
               if username == self.users[each]["username"] and password == self.users[each]["password"]:
                   print("success")
                   return True
               return False




