import os
import shutil

deadFileName = "deadEmployees.txt"
# deadFileName = input("Enter DeadFile: )

dataGood = False

try:
    deadFile = open(deadFileName, "r")  # Import file
    userList = deadFile.readlines()  # Read lines from file
    deadFile.close()  # close file
    dataGood = True  # Set data to good after processing file

except:
    print("Error. DeadFile not available or corrupted")

if dataGood:
    # The following line was removed because linux is case sensitive
    # userList = [user.lower() for user in userList]  # make usernames all lowercase
    userList = sorted(userList)  # sort userList alphabetically
    listIndex = 0  # To keep track of position in list
    for user in userList:
        # print(user)
        unformattedUser = user
        head, sep, tail = unformattedUser.partition('@')  # split username from domain
        user = head  # take only username
        # print(user)

        userList[listIndex] = user
        listIndex += 1  # increment position in list
        # print(userList)

    for user in userList:
        deadPath = os.path.join(os.path.expanduser('~'), 'Documents', 'Database and Scripting', 'users2data', 'Users2', user)
        print("Deleting User Directory --> " + user)
        shutil.rmtree(deadPath)  # removes an empty directory
