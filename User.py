# for json file error checking
from simplejson import JSONDecodeError
# for hiding password while entering them
import getpass
import json
from Colors import bcolors

# create UserData class
class UserData:
    # create the constructor
    def __init__(self,id,name,email,password,phone):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        
    # Registration Methods
    
    # using static methods because our methods are only related to User/Project class (Check on inputs) not for dealing 
    # with class instances
      
    @staticmethod
    def getName():
        FNameFlag = False
        fullName = []
        while not FNameFlag:
            fname = input("Enter your First Name: ")
            # check if first name is less than 3 characters
            if len(fname) < 3:
                print(bcolors.FAIL + "Enter a valid first name, minimum 3 characters" + bcolors.ENDC)
            else:
                # append the first name in full name list
                fullName.append(fname)
                LNameFlag = False
                while not LNameFlag:
                    lname = input("Enter your Last Name: ")
                    if len(lname) < 3:
                        print(bcolors.FAIL + "Enter a valid last name, minimum 3 characters" + bcolors.ENDC)
                    else:
                        LNameFlag = True
                        FNameFlag = True
                        # append the last name in full name list
                        fullName.append(lname)
        # join the first and last name with a space ' ' between them to get full name
        Name = ' '.join(fullName)
        return Name
    
    @staticmethod
    def getEmail():
        EmailFlag = False
        while not EmailFlag:
            email = input("Enter your Email: ")
            # check if email contains @ character
            checkAt = email.find("@")
            # check if email contains .com or we can use endswith() method instead of find()
            checkCom = email.find(".com")
            # if any of them is not found, find() returns -1 
            if checkAt == -1 or checkCom == -1:
                print(bcolors.FAIL + "Invalid Email, must include @ and .com" + bcolors.ENDC)
            else:
                EmailFlag = True
        return email
    
    @staticmethod   
    def getPassword():
        PassFlag = False
        while not PassFlag:
            # password is global to enable confirming it in another method
            # or we can pass it as argument to confirmPassword method
            global password
            # hiding the user entry of password using getpass library
            password = getpass.getpass("Enter your Password: ")
            # check if password is less than 6 characters
            if len(password) < 6 :
                print(bcolors.FAIL + "Minimum length of password is 6 characters" + bcolors.ENDC)
            else:
                PassFlag = True
        
        # calling confirm password method before returning the password
        UserData.getConfirmPass()
        return password
        
    @staticmethod
    def getConfirmPass():
        ConfirmFlag = False
        while not ConfirmFlag:
            confirm = getpass.getpass("Confirm your Password: ")
            # check for matching the password and confirm password
            if confirm == password:
                print(bcolors.OKGREEN + "Password Confirmed" + bcolors.ENDC)
                ConfirmFlag = True
            else:
                print(bcolors.FAIL + "Passwords don't match" + bcolors.ENDC)

    @staticmethod
    def getMobilePhone():
        PhoneFlag = False
        while not PhoneFlag:
            phone = input("Enter your Mobile Phone: ")
            # check if phone start with egyptian codes
            phonestart = phone.startswith("010") or phone.startswith("011") or phone.startswith("012") or phone.startswith("015")
            # check if the input is only digits and is 11 numbers only
            if phone.isdigit() == False or len(phone) != 11 or phonestart == False:
                print(bcolors.FAIL + "Invalid Phone Number" + bcolors.ENDC)
            else:
                PhoneFlag = True
                print(bcolors.OKGREEN + "Successful Registration" + bcolors.ENDC)
        return phone

    @staticmethod
    def getID():
        # a method for getting user id 
        with open("UserData.json","r") as ReadUser:
            json_data = ReadUser.read()
            try:
                data = json.loads(json_data)
            except json.decoder.JSONDecodeError:
                data = []
        return len(data)+1
    
    @staticmethod
    def AddUser(new):
        # the new argument holds the user data
        # writing the user data in a dictionary
        userdata = {"ID":new.id,"Name":new.name,"Email":new.email,"Password":new.password,"Mobile Phone":new.phone}

        # writing the user data in json file
        with open("UserData.json","r") as ReadUser:
            json_data = ReadUser.read()
            try:
                data = json.loads(json_data)
                data.append(userdata)
            # if json file is empty, loads methods raise an error so, using try and except we can
            # initialize the file with empty list before appending new user
            except json.decoder.JSONDecodeError:
                data = []
                data.append(userdata)
            # writing in json file using dump() method from json library
            with open("UserData.json","w") as newUser:
                json.dump(data, newUser,indent=4, separators=(',',': '))
                
    # Log In Methods
    @staticmethod
    def LogInEmail():
        EmailFound = False
        EmailLogFlag = False
        while not EmailLogFlag:
            loginemail = input("Enter your Email: ")
            # check if the input email is valid as a format
            checkAt = loginemail.find("@")
            checkCom = loginemail.find(".com")
            
            if checkAt == -1 or checkCom == -1:
                print(bcolors.FAIL + "Invalid Email, must include @ and .com" + bcolors.ENDC)
            else:
                EmailFlag = True
                # read the data from users file 
                with open("UserData.json","r") as ReadUser:
                    json_data = ReadUser.read()
                    # making data global to use it again in password section
                    global Data
                    try:
                        Data = json.loads(json_data)
                    # if userdata file is empty return to main menu and tell the user that no data found
                    except json.decoder.JSONDecodeError:
                        print(bcolors.FAIL + "No Users Data found yet" + bcolors.ENDC)
                        from Main import Main
                        main = Main()
                # check if the entered email already exists or not found
                for i in range(len(Data)):
                    if loginemail == Data[i]["Email"]:
                        EmailFound = True
                        # save the password of that matched email to compare it with the user entry
                        # in password section
                        global userpass
                        userpass = Data[i]["Password"]
                        userid = Data[i]["ID"]
                        break
                    
                if EmailFound:
                    EmailLogFlag = True
                else:
                    print(bcolors.FAIL + "Email Not Found" + bcolors.ENDC)
        # return the user id to be saved with projects to refer to the user which created that project
        return userid

    @staticmethod
    def LogInpass():
        PassFound = False
        PassLogFlag = False
        while not PassLogFlag:
            loginpass = getpass.getpass("Enter your Password: ")
        
            for i in range(len(Data)):
                # check if the entered password matches the password of the entered email
                if loginpass == userpass:
                    PassFound = True
                    break
            
            if PassFound:
                PassLogFlag = True
            else:
                print(bcolors.FAIL + "Password Not Found or Invalid" + bcolors.ENDC)
        print(bcolors.OKGREEN + "Successful Log In" + bcolors.ENDC)
    
    # a method for creating the files before reading or entering data
    @staticmethod
    def createDataFiles():
        with open("UserData.json","a"):
            pass
        with open("UserProjects.json","a"):
            pass
    
