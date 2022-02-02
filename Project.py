import enquiries
# to deal with dates enteed by the user
import datetime
import json
from Colors import bcolors

# create ProjectData class
class ProjectsData:
    # create the constructor
    def __init__(self,id,title,details,target,startDate,endDate):
        self.id = id
        self.title = title
        self.details = details
        self.target = target
        self.startDate = startDate
        self.endDate = endDate
    
            
    @staticmethod            
    def getTitle():
        TitleFlag = False
        while not TitleFlag:
            title = input("Enter the Project Title: ")
            # check if title is less than 3 characters
            if len(title) < 3:
                print(bcolors.FAIL + "Enter a proper title, minimum 3 characters" + bcolors.ENDC)
            else:
                TitleFlag = True
        return title

    @staticmethod
    def getDetails():
        DetailsFlag = False
        while not DetailsFlag:
            details = input("Enter the Project Details: ")
            # check if details is less than 10 characters
            if len(details) < 10:
                print(bcolors.FAIL + "Enter enough details, minimum 10 characters"+ bcolors.ENDC)
            else:
                DetailsFlag = True
        return details

    @staticmethod
    def getTarget():
        TargetFlag = False
        while not TargetFlag:
            target = input("Enter the Project Total Target: ")
            # check if target is less than 1000 EGP and if it is only digits
            if len(target) < 4 or target.isdigit() == False:
                print(bcolors.FAIL + "Enter a proper Target, minimum is 1000 EGP" + bcolors.ENDC)
            else:
                TargetFlag = True
        return target

    @staticmethod
    def get_start_date():
        DateFlag = False
        # get the current date to compare with it the user's entries
        CurrentDate = datetime.date.today()
        while not DateFlag:
            try:    
                startDate = input("Enter the Start Date of Campaign (in DD-MM-YYYY): ")
                # converting the user entry to date format
                startDate_to_datetime = datetime.datetime.strptime(startDate,"%d-%m-%Y").date()
                # global to compare with it the end date 
                global startDateValid
                # get the difference of dates in days
                startDateValid = (startDate_to_datetime - CurrentDate).days
                # check if the difference less than zero so the user has to enter a valid date that exceeds
                # the current date or same as it
                if startDateValid < 0:
                    print(bcolors.FAIL + "Enter a Valid Start Date" + bcolors.ENDC)
                else:
                    DateFlag = True
            except ValueError:
                print(bcolors.FAIL + "Enter a proper format for the date as shown" + bcolors.ENDC)  
        return startDate

    @staticmethod
    def get_end_date():
        DateFlag = False
        CurrentDate = datetime.date.today()
        while not DateFlag:
            try:    
                endDate = input("Enter the End Date of Campaign (in DD-MM-YYYY): ")
                endDate_to_datetime = datetime.datetime.strptime(endDate,"%d-%m-%Y").date()
                endDateValid = (endDate_to_datetime - CurrentDate).days
                # check if the end date exceeds the start date or in same date
                if endDateValid < startDateValid:
                    print(bcolors.FAIL + "Enter a Valid End Date" + bcolors.ENDC)
                else:
                    DateFlag = True
            except ValueError:
                print(bcolors.FAIL + "Enter a proper format for the date as shown" + bcolors.ENDC)
        return endDate   
          
    @staticmethod
    def createProject(new):
        # the new argument holds the project data
        # writing the project data in a dictionary
        newProject = {"User ID":new.id,"Title":new.title,"Details":new.details,"Total Target":new.target,"Start Date":new.startDate,"End Date":new.endDate}
        
        # writing the user data in json file
        with open("UserProjects.json","r") as ReadProjects:
            json_projects = ReadProjects.read()
            try:
                projects = json.loads(json_projects)
                projects.append(newProject)
            # if json file is empty, loads methods raise an error so, using try and except we can
            # initialize the file with empty list before appending new project
            except json.decoder.JSONDecodeError:
                projects = []
                projects.append(newProject)
                
        # writing in json file using dump() method from json library
        with open("UserProjects.json","w") as ProjectsFile:
            json.dump(projects, ProjectsFile,indent=4, separators=(',',': '))
            print(bcolors.OKGREEN + "Project Created Successfully" + bcolors.ENDC)
    
    @staticmethod     
    def viewProjects():
        # read the data from the projects file
        with open("UserProjects.json","r") as ReadProjects:
            json_projects = ReadProjects.read()
        try:
            projects = json.loads(json_projects)
        # if empty show no projects to show
        except json.decoder.JSONDecodeError:
            
            print(bcolors.FAIL + "No Projects to show" + bcolors.ENDC)
            from Main import Main
            main = Main()
    
        # viewing all projects in the json file
        for i in range(len(projects)):
            print(bcolors.OKBLUE + "{}".format(projects[i]) + bcolors.ENDC)
            print("--------------------------------------------------------------------------------------------")    

        # a try to print projects data in table form
        # from tabulate import tabulate
        # print(tabulate(projects, headers="keys"))
    
    @staticmethod
    def viewUserProject(id):
        with open("UserProjects.json","r") as ReadProjects:
            json_projects = ReadProjects.read()
        try:
            projects = json.loads(json_projects)
        # if empty show no projects to show
        except json.decoder.JSONDecodeError:
            
            print(bcolors.FAIL + "No Projects to show" + bcolors.ENDC)
            from Main import Main
            main = Main()
        projectFound = False
        # viewing user's projects in the json file
        for i in range(len(projects)):
            if projects[i]["User ID"] == id:
                print(bcolors.OKBLUE + "{}".format(projects[i]) + bcolors.ENDC)
                print("--------------------------------------------------------------------------------------------")    
                projectFound = True
                
        if projectFound != True:
            print(bcolors.FAIL + "No Projects found to this user" + bcolors.ENDC)
                