import os

def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"/Users/MKD/Coding/ProgrammingFoundations/prank")
    #print(file_list) #making sure we have all the files we need

    #Troubleshooting an error: figure out what folder I'm currently in
    saved_path = os.getcwd()
    #print('Current Working Directory is',saved_path)
    #above returns the folder this file is in, not the prank folder
    
    #fix the bug by changing the current working directory
    os.chdir(r"/Users/MKD/Coding/ProgrammingFoundations/prank")
    
    #(2) for each file, rename file
    for file_name in file_list:
        #use print to help me keep track of what's going on
        print('Old Name:', file_name)
        print('New Name:',file_name.translate(str.maketrans('','','0123456789')))
        os.rename(file_name, file_name.translate(str.maketrans('','','0123456789'))) 
    os.chdir(saved_path)
    
rename_files()
