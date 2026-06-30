import json
import time






class accounts():
    def __init__(self):
        try:
            self.password = self.whologgedin("request", "none", 1)[0]
        except:
            self.whologgedin("change", "Guest", 1) 
        self.user = self.whologgedin("request", "none", 0)
        if(not self.user == "Guest"):
            self.loggedin = True
        else:
            self.loggedin = False
        self.whoison = self.whologgedin("request", "none", 0)
        print(f"Welcome back {self.user}.")
        self.main()

    def usercheck(self):
        with open("Save.json", "a+") as save:
            save.seek(0)
            y = json.load(save)
        while True:
            user = input("Enter your desired user:\n")
            if (user in y.keys()):
                time.sleep(1)
                print(f"{user} already exists. Please enter a different user.")
            else:
                time.sleep(1)
                return user
                break
    def detailwrite(self, mode, info):
        with open("Save.json", "a+") as save:
            save.seek(0)
            y = json.load(save)
            if (mode == "account"):
                y[self.user] = [self.password]
            else:
                y[self.user] = [info]
            save.truncate(0)
            save.seek(0)
            json.dump(y, save, indent=4, sort_keys=True)

    def detaildel(self, mode):
        with open("Save.json", "a+") as save:
            save.seek(0)
            y = json.load(save)
            if (mode == "account"):
                y.pop(self.user)
            else:
                y[self.user] = []
            save.truncate(0)
            save.seek(0)
            json.dump(y, save, indent=4, sort_keys=True)
            
    def main(self): 
        while True:
            time.sleep(1)
            print("Account settings:\n[1] Login To Account\n[2] Reset Password\n[3] Delete Account\n[4] Logout Of Account\n[5] Create New Account\n[6] See account settings\n[7] Exit")
            z = input()
            if (z == "1"):
                if (self.loggedin == True):
                    time.sleep(1)
                    print("You are already logged in.")
                else:
                    self.login()
                    self.whologgedin("change", self.user, 1)
            elif (z == "2"):
                self.reset()
            elif (z == "3"):
                self.delete()
            elif (z == "4"):
                if (self.loggedin == True):
                    self.loggedin = False
                else:
                    time.sleep(1)
                    print("You are not logged in.")
                    
            elif (z == "5"):
                if (self.loggedin == True):
                    time.sleep(1)
                    print("You are already logged in.")
                else:
                    self.user = self.usercheck()
                    time.sleep(1)
                    self.password = input("Enter your desired password:\n")
                    self.detailwrite("account", 1)
                    time.sleep(1)
                    print(f"Account {self.user} has been created.")
                    self.loggedin = True
                    self.whoison = self.user
                    self.whologgedin("change", self.user, 1)
            elif (z == "6"):
                time.sleep(1)
                if(self.loggedin == True):
                    if(input("Please enter your password to see account details\n") == self.password):
                        print(f"User: {self.user}\nPassword: {self.password}")
                    else:
                        print("Incorrect password")
                else:
                    print("You are not logged in.")
            elif (z == "7"):
                time.sleep(1)
                print("Exiting...")
                if(self.loggedin == False):
                    self.whologgedin("change", "Guest", 1)
                time.sleep(3)
                break


    def login(self):
        with open("Save.json", "a+") as save:
            save.seek(0)
            y = json.load(save)
        while True:
            time.sleep(1)
            user = input("Enter your user or 'Exit' to cancel login:\n")
            if (user == "Exit"):
                time.sleep(1)
                break
            elif (user in y.keys()):
                time.sleep(1)
                password = input("Enter your password:\n")
                if (password == y[user][0]):
                    self.user = user
                    self.password = password
                    time.sleep(1)
                    print(f"Logged in as {self.user}.")
                    self.loggedin = True
                    self.whoison = self.user
                    break
                else:
                    time.sleep(1)
                    print("Incorrect password. Please try again.")
            else:
                time.sleep(1)
                print("User does not exist. Please try again.")
                break

    def whologgedin(self, mode, acc, info):
        with open("Save.json", "a+") as save:
            save.seek(0)
            y = json.load(save)
            if (mode == "request"):
                for i in y.items():
                    if (len(i[1]) > 1):
                        return i[info]
            elif (mode == "change"):
                for i in y.items():
                    if (len(i[1]) > 1):
                        x = [i[1][0]]
                        y[i[0]] = x 
                y[acc].append(1)
                save.truncate(0)
                json.dump(y, save, indent=4, sort_keys=True)



    def __str__(wegetsilly):
        return f"Hello {wegetsilly.user}, this is the registering class. You should not be here."
    
    def reset(self):
        time.sleep(1)
        if(self.loggedin == True):
            if (input("Please enter your user to confirm you would like to reset your password:\n") == self.user):
                time.sleep(1)
                temppassword = input("Enter your new password:\n")
                self.password = temppassword
                self.detailwrite("password", temppassword)
                time.sleep(1)
                print("Your account has been reset.")
            else:
                time.sleep(1)
                print("Incorrect password. Account not reset.")
        else:
            print("You are not logged in.")

    def delete(self):
        time.sleep(1)
        if(self.loggedin == True):
            if (input("Please enter your password to delete your account:\n") == self.password):
                self.detaildel("account")
                self.whologgedin("change", "Guest", 1)
                time.sleep(1)
                print(f"Account {self.user} has been deleted.")
            else:
                time.sleep(1)
                print("Incorrect password. Account not deleted.")
        else:
            print("You are not logged in.")


p1 = accounts()

