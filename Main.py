# pip install enquiries 
import enquiries

# create Main class
class Main:
    # create the constructor of main class
    def __init__(self):
        # call Main Menu (Instance Method) once an object is created 
        Main.MainMenu(self)
    
    # Main Menu method for handling navigation and selections
    def MainMenu(self):
        
        while True:
            options = ["Registeration", "Log In"]
            choice = enquiries.choose("Choose one of these options: ", options)

            # import UserData class just before using it
            # importing it at the begginning of file will execute it directly
            from User import UserData
            UserData.createDataFiles()
            if choice == "Registeration":
                # creating an object from UserData class 
                # passing the static methods for input check and return them back if valid
                newuser = UserData(UserData.getID(),UserData.getName(),UserData.getEmail(),UserData.getPassword(),UserData.getMobilePhone())
                # calling the method that writes the new user data in file
                UserData.AddUser(newuser)

            elif choice == "Log In":
                # calling the login method to check the existence of the user email and return his ID
                userid = UserData.LogInEmail()
                # calling the password method to check the matching of entered password with the pre-entered email
                UserData.LogInpass()
                # importing ProjectData class just before using it
                from Project import ProjectsData
                while True:
                    options = ["Create Project", "View All Projects", "View user's Projects","Return to Main Menu"]
                    choice = enquiries.choose("Choose one of these options: ", options)
                    
                    if choice == "Create Project":
                        # creating an object from ProjectData class
                        # passing the static methods for input check and return them back if valid
                        newproject = ProjectsData(userid,ProjectsData.getTitle(),ProjectsData.getDetails(),ProjectsData.getTarget(),ProjectsData.get_start_date(),ProjectsData.get_end_date()) 
                        # calling the method that writes the new project with in file
                        ProjectsData.createProject(newproject)
        
                    elif choice == "View All Projects":
                        # calling the method that view all projects
                        ProjectsData.viewProjects()
                    
                    elif choice == "View user's Projects":
                        # calling the method that view user's projects
                        ProjectsData.viewUserProject(userid)
                        
                    elif choice == "Return to Main Menu":
                        # calling the main menu again
                        main = Main()
# creating an object from the Main class so the Main Menu method get executed immeditely           
main = Main()