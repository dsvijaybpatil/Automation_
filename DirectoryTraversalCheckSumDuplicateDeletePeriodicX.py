import os
import sys
import time
import hashlib
import schedule  # type:ignore
   
def CalculateCheckSum(path,BlockSize=1024):
    fobj=open(path,"rb")
    
    hobj=hashlib.md5()

    buffer=fobj.read(BlockSize)
    while(len(buffer)>0):
        hobj.update(buffer)
        buffer=fobj.read(BlockSize)
    fobj.close()

    return hobj.hexdigest()

def DirectoryWatcher(DirectoryName="Marvellous"):
    flag=os.path.isabs(DirectoryName)
    if flag==False:
        DirectoryName=os.path.abspath(DirectoryName)              # this is only cocanate the previous path with current name
    flag=os.path.exists(DirectoryName)

    if flag==False:
        print("The path is invalid.")
        exit()
    
    flag=os.path.isdir(DirectoryName)
    if flag==False:
        print("Path is valid but the target is not a Directory.")
        exit()

    
    
    for FolderName , SubfolderNames , FileNames in os.walk(DirectoryName):
        
        for fname in FileNames:
            fname=os.path.join(FolderName,fname)
            checksum=CalculateCheckSum(fname)
            print("File name:",fname)
            print("Check sum is:",checksum)
            print()









            
    
    timestamp=time.ctime()
    
    fileName="MarvellousLog%s.log"%(timestamp)
    fileName=fileName.replace(" ","_")
    fileName=fileName.replace(":","_")

    
    fobj=open(fileName,"w")
    Border="-"*85
    fobj.write(Border+"\n")
    fobj.write("This is the log file of Marvellous Automation Script."+"\n")
    fobj.write("This is a Directory Cleaner Script."+"\n")
    
    fobj.write(Border+"\n")


    fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
   
    
    fobj.write("This is created at:\n"+timestamp+"\n")
    fobj.write(Border)

def FindDuplicate(DirectoryName="Marvellous"):
    flag=os.path.isabs(DirectoryName)
    if flag==False:
        DirectoryName=os.path.abspath(DirectoryName)              # this is only cocanate the previous path with current name
    flag=os.path.exists(DirectoryName)

    if flag==False:
        print("The path is invalid.")
        exit()
    
    flag=os.path.isdir(DirectoryName)
    if flag==False:
        print("Path is valid but the target is not a Directory.")
        exit()

    
    Duplicate={}
    for FolderName , SubfolderNames , FileNames in os.walk(DirectoryName):
        
        for fname in FileNames:
            fname=os.path.join(FolderName,fname)
            checksum=CalculateCheckSum(fname)

            if(checksum in Duplicate):
                Duplicate[checksum].append(fname)
            else:
                Duplicate[checksum]=[fname]

            
    return Duplicate
       
    
def DisplayResult(MyDict):
    Result=list(filter(lambda x:len(x)>1, MyDict.values()))

    count=0

    for value in Result:
        for subvalue in value:
            count+=1
            print(subvalue)
        print("---------------------------------------------------")
        print("Value of count is:",count)
        print("-----------------------------------------------")
        count=0
def DeleteDuplicate(path="Marvellous"):
    MyDict=FindDuplicate(path)
    Result=list(filter(lambda x:len(x)>1, MyDict.values()))

    count=0
    cnt=0

    for value in Result:
        for subvalue in value:
            count+=1
            if(count>1):
                print("Deleted File:",subvalue)
                os.remove(subvalue)
                cnt+=1
        count=0
    print("Total Deleted File:",cnt)

def main():
    
    Border="-"*85
    print(Border)
    print("----------------------------------------------------------------")
    print("-----------------------Marvellous Automation--------------------")
    print("----------------------------------------------------------------")
    print(Border)
    if (len(sys.argv)==2):
        if((sys.argv[1]=="--h") or sys.argv[1]=="--H"):
            print("This application is used to perform Directory Cleaning.")
            print("This is the Directory automation script")
        elif((sys.argv[1]=="--u") or sys.argv[1]=="--U"):
            print("Use the given script as")
            print("ScriptName.py NameofDirectory timeinterval")
            print("Please provide Absolute path")
    if (len(sys.argv)==3):
            
            schedule.every(int(sys.argv[2])).minutes.do(DeleteDuplicate)
            
            while True:
                schedule.run_pending()
                time.sleep(1)
    else:
        print("Invalid Number of Command line arguments.")         
        print("Use the given flag as:")
        print("--h: Use to Display the help.")
        print("--u: Use to Display the usage.")

    
    
    print("----------------------------------------------------------------")
    print("--------------------Thank You for Using Our Script--------------")
    print("--------------------------Marvellous Infosystem-----------------")
    print("----------------------------------------------------------------")

    
    
    
if __name__=="__main__":
    main()