import os

def deletefile():
    
    path = "/home/keepboard/Desktop/blackbox" 
    files = os.listdir(path)
    
    count=len(files)
    files = sorted(files, key=lambda x: os.path.getmtime(os.path.join(path, x)))
    if(3<=len(files)):
        for file in files:
            file_path = os.path.join(path, file)
            os.remove(file_path)
            break