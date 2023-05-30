import json
class SignOptions:
    def __init__(self):
        self.users = []

    def register(self, user, password):
        with open("accounts.txt", "a") as file:
            file.write(f"{user},{password}\n")
        with open(f"{user}_diary.txt", "w") as diary:
            diary.write(f"{user}'s Diary\n")




    def check_login(self, username, password):
            with open("accounts.txt", "r") as file:
                lines = file.readlines()
                print(lines)
                for line in lines:
                    if username == line.split(",")[0] and password == line.split(",")[1].rstrip():
                        return username





