#Made by Joseph Li, to help you index your instagram messages. To do so, request data from instagram and download
#the file. Unzip the file, and find the path to the inbox folder. Post that in rootdir and you're good to go!
import os
import linecache
import time
import glob
rootdir = #input path to your inbox eg. r"C:\Users\Test\Downloads\username_date\messages\inbox" make sure to add an r before the quotes!

username = input("Username shown in the text files whose messages that you want to find:\n")

n = int(input("Next, we will input the strings you want to find. How many words would you like to index?\n"))
appearances = 0

hasimages = []  # directories that have images
linesfound = []  # lines that have the user's text
listOfStr = []  # strings to find
for i in range(0, n):
    listOfStr.append(input("enter word " + str(i + 1) + ":\n"))

for filename in os.listdir(rootdir):
    textfiles = []  # files to be searched
    directory = rootdir + "\\" + filename
    for filename2 in os.listdir(directory): #loops through files in a directory
        if filename2.endswith(".json"): #adds textfile name to the list, open it after this
            textfiles.append(filename2) #adds file to list
        else:
            continue
        photo = directory + "\\photos"
        if os.path.isdir(photo) and not(photo in hasimages): #checks if folder has images folder
            hasimages.append(directory)  #adds it to a list if it does
    for txtfile in textfiles: #loops through textfiles in this directory
        txtdirectory = directory + "\\" + txtfile #gets directory of text file
        f = open(txtdirectory) #opens text file
        counter = 0
        for line in f: #loop through each line in text file
            counter+=1
            lowercase = line.lower() #ignore case
            lowercase = lowercase.replace(" ", "") #remove spaces
            for subStr in listOfStr: #go through list of words to find
                check = subStr.replace(" ", "")
                if check.lower() in lowercase: #is the words in the list?
                    checkUsername = linecache.getline(txtdirectory, counter-2) #see if username is the users
                    checkUsername = checkUsername.replace(" ","")
                    check1 = username.replace(" ","")
                    if(check1.lower() in checkUsername.lower()):
                        appearances += 1
                        add = txtdirectory + "\n" + line
                        linesfound.append(linecache.getline(txtdirectory, counter-2))
                        linedate = linecache.getline(txtdirectory, counter - 1)
                        ms = int(''.join(i for i in linedate if i.isdigit()))
                        date = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(ms/1000.0)) #convert ms to date
                        linesfound.append(date)#supposedly the date that is converted from ms.
                        linesfound.append(add)


with open("instances.txt","a") as f:
    for item in linesfound:
        f.write("%s\n" % item)
with open("instances.txt","a") as f:
    f.write("\n\n\n\n\n folders with images")
    for item in hasimages:
        f.write("%s\n" % item)
    f.write("number of appearances" + str(appearances))
print("Job done! Check the instances.txt file")
