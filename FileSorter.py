#
# Made by Wiktor Persak - Zer0AlmostNull
# email: wiktor.persak@gmail.com
#

import os.path, time, os, datetime, shutil 

WorkerFolderPath='./Worker'
ProgramName=os.path.basename(__file__)

print('\n',end='')
try:
    os.mkdir(WorkerFolderPath)
    print('Created worker folder', end='\n') 
except FileExistsError:
    pass

def GetModificationDate(file):
    t = os.path.getmtime(file)
    return datetime.datetime.fromtimestamp(t)

def MoveFiles(path: str,des: str):
    ld=os.listdir(path)
    for item in ld:
        if os.path.isdir(path+item)==True: #if dir
            MoveFiles(path+'/'+item+'/',des)
        else: #if not dir
            if not item == ProgramName:
                shutil.move(path+'/'+item,WorkerFolderPath+'/'+item)
                print(' Moved: '+item)

def DelUnnessaryFolder(path: str):
    ld=os.listdir(path)
    for item in ld:
        if os.path.isdir(path+item)==True and not (item==WorkerFolderPath.replace('./','')): #if dir
            DelUnnessaryFolder(path+item+'/')
            os.rmdir(path+item)
            print('Removed dir: '+item)

def SortFile(f: str,moveto: str):
    files=os.listdir(f)
    for item in files:
        if not item == ProgramName:
            date = GetModificationDate(WorkerFolderPath+'/'+item)
            try:
                os.mkdir(moveto+str(date.year))
                for i in range(1,12+1,1):
                    os.mkdir(moveto+str(date.year)+'/'+str(i))
                    print('Made dir: ',moveto+str(date.year)+'/'+str(i))
            except FileExistsError:
                pass
            shutil.move(WorkerFolderPath+'/'+item,moveto+str(date.year)+'/'+str(date.month))
            print('\nMoved form: ',WorkerFolderPath+'/'+item,' \n to: ',moveto+str(date.year)+'/'+str(date.month))


print('Write your input path: ',end='')
getpath=input()
MoveFiles(getpath,WorkerFolderPath)

DelUnnessaryFolder(getpath)

print('Write your destination path: ',end='')
SortFile(WorkerFolderPath,input())

print('Removed worker')
os.rmdir(WorkerFolderPath)

print('\n***Finished*** - Press Enter to exit')
input()

print('\n',end='')
