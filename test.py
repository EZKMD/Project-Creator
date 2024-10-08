import os

projectType = 1

projectTypeArray = ["Python Projects", "Front-End Projects", "C Projects", "C++ Projects", "JavaScript Projects"]

projectType = projectTypeArray[projectType-1]

name = "TestTest"

path = "G:\\My Drive\\Coding\\" + projectType
os.chdir(path)

command = "mkdir "+ name

result = os.popen(command).read().strip()