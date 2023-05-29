import sys
from diarybook import DiaryBook, Diary
import utils
from sign import SignOptions

class Menu:
    def __init__(self):
        self.diarybook = DiaryBook()

        self.choices = {
            "1": self.show_all_diaries_id,
            "2": self.show_all_diaries_memo,
            "3": self.add_diary,
            "4": self.search_diaries,
            "5": self.quit
        }

    def show_all_diaries_memo(self):
        sorted_by_memos = []
        if len(self.diarybook.diaries) == 0:
            print("There are no diaries in the database.")
        else:
            for diary in self.diarybook.diaries:
                sorted_by_memos.append((diary.memo, diary.tags))
            sorted_by_memos.sort()
        for each in sorted_by_memos:
            print(f"{each[0]} - {each[1]}")

    def show_all_diaries_id(self):
        if len(self.diarybook.diaries) == 0:
            print("There are no diaries in the database.")
        else:
            for diary in self.diarybook.diaries:
                print(f"{diary.id} - {diary.memo} - {diary.tags}")


    def add_diary(self):
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        self.diarybook.new_diary(memo, tags)

    def search_diaries(self):
        keyword = input("Enter a keyword: ")
        filtered_diaries = self.diarybook.search_diary(keyword)
        if len(filtered_diaries) == 0:
            print("No diaries found")
        else:
            for diary in filtered_diaries:
                print(f"{diary.id} - {diary.memo}")

    def populate_database(self):
        diaries = utils.read_from_json_into_app("data.json")
        for diary in diaries:
            self.diarybook.diaries.append(diary)

    def quit(self):
        print("Thanks for using our DiaryBook!...")
        sys.exit(0)

    def display_menu(self):
        print("""
            Diarybook Menu:
            
            1. Show diaries by id
            2. Show diaries by memo
            3. Add diary
            4. Filter using keyword
            5. Quit program
            
            """)

    def run(self):
        while True:
            login = input("Type 1 for login or 2 for register: ")
            if login == "1":
                username = input("Enter username: ")
                password = input("Enter password: ")
                self.user = SignOptions()
                if self.user.check_login(username, password):
                    print(f"welcome {username}")
                    pass
                else:
                    print("Register first")
                    sys.exit()

            elif login == "2":
                username = input("Enter username: ")
                password = input("Enter password: ")
                password2 = input("Enter password again: ")
                if password != password2:
                    print("Passwords do not match, try again")
                    sys.exit()
                else:
                    self.user = SignOptions()
                    self.user.register(username, password)
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))



if __name__ == "__main__":

    Menu().run()