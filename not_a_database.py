import csv
import getpass
# data.truncate()

class User:
    def __init__(self, user_name, password, full_name, phone_num):
        self.user_name = user_name
        self.password = password
        self.full_name = full_name
        self.phone_num = phone_num

class Notbase:
    def __init__(self, user_dict):
        self.user_dict = user_dict

    def login(self):
        while True:
            username = input("Username: ")
            password = getpass.getpass('Password:')
            try:
                if self.user_dict[username].password == password:
                    print("Success!")
                    self.menu()
                else:
                    print("Wrong")
            except KeyError:
                print("Wrong.")

    def menu(self):
        user_select = ""
        while user_select != "Q" and user_select != "add":
            user_select = input("Enter 'add' to add user, or 'Q' to logout: ")
        if user_select == "add":
            self.add_user()
        elif user_select == "Q":
            self.login()

    def add_user(self):
        user_in = ""
        while user_in != "2":
            new_user_name = ","
            while "," in new_user_name:
                while True:
                    new_user_name = input("New username(no commas): ")
                    if new_user_name not in self.user_dict.keys():
                        break
                    else:
                        print("Username already in use.")
            new_password = ","
            while "," in new_password:
                new_password = input("New password(no commas): ")
            new_full_name = ","
            while "," in new_full_name:
                new_full_name = input("New user's full name(First|Last)(no commas): ")
            new_phone_num = ","
            while "," in new_phone_num:
                new_phone_num = input("New user's phone number(really, no commas): ")
            self.user_dict[new_user_name] = User(new_user_name, new_password, new_full_name, new_phone_num)
            user_in = input("Add another(1), logout(2): ")
        self.write()
        self.login()

    def write(self):
        data = open("db.csv", "w")
        data.truncate()
        keys = self.user_dict.keys()
        for key in keys:
            line = ""
            line += self.user_dict[key].user_name
            line += ","
            line += self.user_dict[key].password
            line += ","
            line += self.user_dict[key].full_name
            line += ","
            line += self.user_dict[key].phone_num
            line += "\n"
            data.write(line)
        data.close()


def main():
    data = open("db.csv", "r+")
    reader = csv.reader(data)
    user_dict = {}
    for row in reader:
        user_dict[row[0]] = User(row[0], row[1], row[2], row[3])
    notbase = Notbase(user_dict)
    notbase.login()


main()
