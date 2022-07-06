# A simple backup script
import shutil
from datetime import date

class Backup:
    def __init__(self):
        self.fromfolder = input("Please enter Source folder path:")
        self.tofolder   = input("Please enter Backup folder path:")
        self.backupday  = date.today()
        self.newfolder  = self.backupday.strftime("%B%d")
        self.tofolder   = self.tofolder + self.newfolder
        #print('to folder-',self.tofolder)
        self.backup()

    def backup(self):
        shutil.copytree(self.fromfolder,self.tofolder,copy_function = shutil.copy,dirs_exist_ok=True) #copying
        shutil.make_archive(self.tofolder,'zip',self.tofolder) #zipping
        print("Backup created as zip file at-",self.tofolder)
        shutil.rmtree(self.tofolder) #cleaning

if __name__ == "__main__":
    b = Backup()
     
