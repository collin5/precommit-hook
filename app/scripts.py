#@Author: Collins Abitekanza
#@Email: abtcolns@gmail.com

from distutils.command.install import install
import os

class Post_install(install):
    
    @staticmethod
    def add_pre_commit():

        #if .git directory exists
        if os.path.isdir(os.path.join(os.getcwd(), ".git")):
                #make hook directory if not exists
                if not os.path.isdir(os.path.join(os.getcwd(), ".git/hooks")):
                    os.system("mkdir .git/hooks")

                #finally copy and set permissions
                os.system("cp app/tmp/template.dat .git/hooks/pre-commit && sudo chmod +x .git/hooks/pre-commit")
        else:
            print("Error installing precommit-hook : .git directory not found in current working path")
            return False
        return True

    def run(self):
        install.run(self)
        #Pre install actions
        if Post_install.add_pre_commit():
            print("Bingo: Pre-commit successfully installed, bye bye ....")
        else:
            print("Failed to add hook,, continuing ...")
            

