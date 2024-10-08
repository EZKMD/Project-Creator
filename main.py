import os
import time as t


while True:
    try:
        # To created named folder as well as the location to put it in:
        projectName = input("Enter project name: ")
        projectType = int(input("""Enter project type:
    [1] Python Project
    [2] Front-End Project
    [3] C Project
    [4] C++ Project
    [5] JavaScript Project
"""))   
        # Usage of array allows avoidance of multiple if statements
        projectTypeArray = ["Python Projects", "Front-End Projects", "C Projects", "C++ Projects", "JavaScript Projects"]

        # Assigning number option to actual string value to append to file paths
        projectType = projectTypeArray[projectType-1]

        pcOrLaptop = input("PC or Laptop: ")

        if pcOrLaptop.lower() == "laptop":
            path = f"G:\\My Drive\\Coding\\{projectType}"
        else:
            path = f"G:\\My Drive\\Coding\\Coding\\{projectType}"

        # Changes directory to path defined
        os.chdir(path)

        # Creates project folder
        os.popen(f"mkdir \"{projectName}\"").read().strip()
        
        # Changes path to include project folder
        path = path + "\\" + projectName

        # Changes current working directory to path defined (again)
        os.chdir(path)


        # If project is that of front-end, creates css, js folders and an index.html file
        if projectType == "Front-End Projects":
            os.popen("mkdir css").read().strip()
            os.popen("mkdir js").read().strip()
            try:
                with open("index.html", "x") as f:
                    f.write("*/This file was automatically created*/")
            except FileExistsError:
                pass
        # Creates main.py if project is python
        elif projectType == "Python Projects":
            try:
                with open("main.py", "x") as f:
                    f.write("#This file was automatically created")
            except FileExistsError:
                pass


        # Initialises git 
        os.popen("git init").read().strip()

        # Opens folder in vscode for further action       
        os.popen("code .").read().strip()
                
    # Allows program to end
    except KeyboardInterrupt:
        print("\nProgram Terminated by User ☠️")
        quit()


    # Incorrect value entered by mistake
    except ValueError:
        print("\nValue entered was invalid, please try another ")
        t.sleep(0.25)
        pass





