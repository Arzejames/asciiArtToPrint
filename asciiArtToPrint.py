import os

#Get the text file where the user stored the ascii art
inputFile = input("What file you would like to convert?: ")
#Get how the users language deals with printing text
#TODO add multi line support for languages such as assembly 
#TODO maybe add a language selector to automatically know how to print for that language
languagePrintCommand = input('How does your language print text? Add INSERT_TEXT where you would like text (Make sure to use quotes "" around INSERT_TEXT if used): ')
#Get the output file name for the outputted print code
outputFileName = input("Where would you like to save the print commands?: ")

#Check if file exists, if not, tell the user it does not exist
if os.path.exists(inputFile):
    print(f"{inputFile} Found!")
    
    #Opens output file to write to, if no filename is supplied, output.txt is the default
    if outputFileName != "":
        outputFile = open(outputFileName, "a")
    else:
        outputFile = open("output.txt", "a")
    
    if languagePrintCommand.find("INSERT_TEXT") == -1:
        print("ERROR: Inputted language print command does not contain INSERT_TEXT")
    #Convert ascii art to print commands
    print(f"Converting {inputFile}")
    count = 0
    with open(inputFile) as file:
        for item in file:
            #Make text to write by replace INSERT_TEXT with text
            text = languagePrintCommand.replace("INSERT_TEXT",item.replace("\n", ""))
            outputFile.write(text+'\n')
            count+=1
    print(f"Wrote {count} lines to {outputFileName}")
else:
    print(f"ERROR: File was not found! File inputed was {inputFile}")