import os

def execute_command(command, path=None):
  """Executes a shell command in the specified path.

  Args:
    command: The command to execute.
    path: The optional path to execute the command in. If not specified, the current
      working directory is used.

  Returns:
    The output of the command as a string.
  """

  if path:
    os.chdir(path)


  result = os.popen(command).read().strip()
  return result

# Example usage:
command = "mkdir TestTestTest"
custom_path = "G:\\My Drive\\Coding\\" + "Python Projects"

# output = execute_command(command, custom_path)
# print(output)

# name = input("Enter project name: ")
# projectType = input("""Enter project type:
#   [1] Python 
#   [2] Front-end Web Dev
#   [3] C Project
#   [4] C++ Project
#   [5] JS Project
# """)

# pcOrLaptop = input("PC or Laptop: ")

try:
    while True:
        projectName = input("Enter project name: ")
        projectType = int(input("""Enter project type:
  [1] Python Project
  [2] Front-End Project
  [3] C Project
  [4] C++ Project
  [5] JavaScript Project
"""))
        projectTypeArray = ["Python Projects", "Front-End Projects", "C Projects", "C++ Projects", "JavaScript Projects"]

        projectType = projectTypeArray[projectType-1]

        pcOrLaptop = input("PC or Laptop: ")

        if pcOrLaptop.lower() == "laptop":
            path = f"G:\\My Drive\\Coding\\{projectType}"
            os.chdir(path)
            exitCode = os.popen(f"mkdir \"{projectName}\"").read().strip()
            print(exitCode)
            
            
               


except KeyboardInterrupt:
    print("Program Terminated by User")







