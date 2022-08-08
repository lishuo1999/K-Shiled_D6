import optparse
import argparse
from argparse import ArgumentParser
import os
import subprocess as sp
import sys

white = "\033[1;37m"
green = '\033[1;32m'
red = '\033[1;31m'
blue = '\033[1;34m'
cyan = '\033[0;36m'
yellow = '\033[0;33m'
noclr = '\033[0m'   

class forensic_project:
    
    def __init__(self) -> None: #constructor
        self.storage_dir = f"{os.environ['HOME']}/K-Shiled_D6/usr_inf" # /home/leeseok/K-Shiled_D6/usr_inf 에 저장된 값 읽어옴

    def printsave(self, *tmp):
        file = open(self.storage_dir + '/stdout.txt', 'a', encoding = 'utf-8')
        print(*tmp)
        print(*tmp, file=file)
        file.close()

    def make_dir(self):
        try:
            if os.path.isdir(self.storage_dir) == False: # /usr_inf 존재하지 않을때 mkdir 실행  
                    sp.run([f"mkdir",  self.storage_dir])  # 수집된 정보들 저장할 디렉토리 생성
                    self.printsave("Making directory to store evidence: " + self.storage_dir)

        except Exception as err:
            self.printsave("Error creating directory: {err}")
            return False
    

    def find_login_inf(self):  # 로그인 정보 수집
        try:
            if os.path.isfile(self.storage_dir + '/login.txt') == False: # login.txt 없는 경우
                # 로그인에 관련된 정보 login.txt에 저장
                file = open(self.storage_dir + "/login.txt", 'w', encoding = 'utf-8')
                file.write("<Login Information>\n\n")	
                file.close()
            
            # lastb
            time = sp.getoutput(f"date")
            self.printsave(time + "  Collecting system login failure history via 'lastb' command ...")
            file = open(self.storage_dir + "/login.txt", 'a', encoding = 'utf-8')
            file.write("*****Result of command 'lastb'*****\n")	
            file.close()
            sp.run('sudo lastb >> ' + self.storage_dir + '/login.txt', shell=True)
                
            # lastlog
            time = sp.getoutput(f"date")
            self.printsave(time + "  Collecting system login history via 'lastlog' command ...")
            file = open(self.storage_dir + "/login.txt", 'a', encoding = 'utf-8')
            file.write("\n\n\n*****Result of command 'lastlog'*****\n")	
            file.close()
            sp.run('sudo lastlog >> ' + self.storage_dir + '/login.txt', shell=True)

            # who
            time = sp.getoutput(f"date")
            self.printsave(time + "  Collecting Login User Information via 'who' command ...")
            file = open(self.storage_dir + "/login.txt", 'a', encoding = 'utf-8')
            file.write("\n\n\n*****Result of command 'who'*****\n")	
            file.close()
            sp.run('who >> ' + self.storage_dir + '/login.txt', shell=True)

            # who -aH
            time = sp.getoutput(f"date")
            self.printsave(time + "  Collecting all Login User Information  via 'who -aH' command ...")
            file = open(self.storage_dir + "/login.txt", 'a', encoding = 'utf-8')
            file.write("\n\n\n*****Result of command 'who -aH'*****\n")	
            file.close()
            sp.run('who -aH >> ' + self.storage_dir + '/login.txt', shell=True)

            # who -q
            time = sp.getoutput(f"date")
            self.printsave(time + "  Collecting Login User accounts and number of users logged in via 'who -q' command ...")
            file = open(self.storage_dir + "/login.txt", 'a', encoding = 'utf-8')
            file.write("\n\n\n*****Result of command 'who -q'*****\n")	
            file.close()
            sp.run('who -q >> ' + self.storage_dir + '/login.txt', shell=True)

            # whoami
            time = sp.getoutput(f"date")
            self.printsave(time + "  Collecting Login User accounts via 'whoami' command ...")
            file = open(self.storage_dir + "/login.txt", 'a', encoding = 'utf-8')
            file.write("\n\n\n*****Result of command 'whoami'*****\n")	
            file.close()
            sp.run('whoami >> ' + self.storage_dir + '/login.txt', shell=True)


            # logname
            time = sp.getoutput(f"date")
            self.printsave(time + "  Collecting Login User accounts via 'logname' command ...")
            file = open(self.storage_dir + "/login.txt", 'a', encoding = 'utf-8')
            file.write("\n\n\n*****Result of command 'logname'*****\n")	
            file.close()
            sp.run('logname >> ' + self.storage_dir + '/login.txt', shell=True)

            # w
            time = sp.getoutput(f"date")
            self.printsave(time + "  Collecting Login User Information via 'w' command ...")
            file = open(self.storage_dir + "/login.txt", 'a', encoding = 'utf-8')
            file.write("\n\n\n*****Result of command 'w'*****\n")	
            file.close()
            sp.run('w >> ' + self.storage_dir + '/login.txt', shell=True)

            # users
            time = sp.getoutput(f"date")
            self.printsave(time + "  Collecting Login User accounts via 'users' command ...")
            file = open(self.storage_dir + "/login.txt", 'a', encoding = 'utf-8')
            file.write("\n\n\n*****Result of command 'users'*****\n")	
            file.close()
            sp.run('users >> ' + self.storage_dir + '/login.txt', shell=True)

            # users | wc -w
            time = sp.getoutput(f"date")
            self.printsave(time + "  Collecting the number of users logged in via 'users | wc -w' command ...")
            file = open(self.storage_dir + "/login.txt", 'a', encoding = 'utf-8')
            file.write("\n\n\n*****Result of command 'users | wc -w'*****\n")	    
            file.close()
            sp.run('users | wc -w >> ' + self.storage_dir + '/login.txt', shell=True)

            # last
            time = sp.getoutput(f"date")
            self.printsave(time + "  Collecting login and logout information via 'last' command ...")
            file = open(self.storage_dir + "/login.txt", 'a', encoding = 'utf-8')
            file.write("\n\n\n*****Result of command 'last'*****\n")	
            file.close()
            sp.run('last >> ' + self.storage_dir + '/login.txt', shell=True)

            # /var/log/auth.log 실패한 SSH 로그인 목록 출력
            time = sp.getoutput(f"date")
            self.printsave(time + "  Collecting file /etc/auth.log contents ...")
            file = open(self.storage_dir + "/login.txt", 'a', encoding = 'utf-8')
            file.write("\n\n\n*****Result of failed SSH login information in file /var/log/auth.log*****\n")	
            file.close()
            sp.run('cat /var/log/auth.log | grep "Failed password" >> ' + self.storage_dir + '/login.txt', shell=True)

        except Exception as err:
            self.printsave(f"Error creating file: {err}")
            return False
        
    def find_user_inf(self): # 사용자 정보 수집
        try:
            if os.path.isfile(self.storage_dir + '/user.txt') == False:
                # 사용자에 관련된 정보 user.txt에 저장
                file = open(self.storage_dir + "/user.txt", 'w', encoding = 'utf-8')
                file.write("*****<User Information>*****\n\n")	
                file.close()

            # id
            time = sp.getoutput(f"date")
            self.printsave(time + "  Collecting account information via 'id' command ...")
            file = open(self.storage_dir + "/user.txt", 'a', encoding = 'utf-8')
            file.write("*****Result of command 'id'*****\n")	
            file.close()
            sp.run('id >> ' + self.storage_dir + '/user.txt', shell=True)

            # /etc/passwd 정보 수집
            time = sp.getoutput(f"date")
            self.printsave(time + "  Collecting file /etc/passwd contents ...")
            file = open(self.storage_dir + "/user.txt", 'a', encoding = 'utf-8')
            file.write("*****Results of file /etc/passwd content collection*****\n")	
            file.close()
            sp.run('cat /etc/passwd >> ' + self.storage_dir + '/user.txt', shell=True)

            # /etc/shadow 정보 수집
            time = sp.getoutput(f"date")
            self.printsave(time + "  Collecting file /etc/shadow contents ...")
            file = open(self.storage_dir + "/user.txt", 'a', encoding = 'utf-8')
            file.write("\n\n\n*****Results of file /etc/shadow content collection*****\n")	
            file.close()
            sp.run('sudo cat /etc/shadow >> ' + self.storage_dir + '/user.txt', shell=True)

            # /etc/group 정보 수집
            time = sp.getoutput(f"date")
            self.printsave(time + "  Collecting file /etc/group contents ...")
            file = open(self.storage_dir + "/user.txt", 'a', encoding = 'utf-8')
            file.write("\n\n\n*****Results of file /etc/group content collection*****\n")	
            file.close()
            sp.run('cat /etc/group >> ' + self.storage_dir + '/user.txt', shell=True)

            # /etc/hosts 정보 수집
            time = sp.getoutput(f"date")
            self.printsave(time + "  Collecting file /etc/hosts contents ...")
            file = open(self.storage_dir + "/user.txt", 'a', encoding = 'utf-8')
            file.write("\n\n\n*****Results of file /etc/hosts content collection*****\n")	
            file.close()
            sp.run('cat /etc/hosts >> ' + self.storage_dir + '/user.txt', shell=True)

            # /etc/hosts.allow 정보 수집
            time = sp.getoutput(f"date")
            self.printsave(time + "  Collecting file /etc/hosts.allow contents ...")
            file = open(self.storage_dir + "/user.txt", 'a', encoding = 'utf-8')
            file.write("\n\n\n*****Results of file /etc/hosts.allow content collection*****\n")	
            file.close()
            sp.run('cat /etc/hosts.allow >> ' + self.storage_dir + '/user.txt', shell=True)

            # /etc/hosts.deny 정보 수집
            time = sp.getoutput(f"date")
            self.printsave(time + "  Collecting file /etc/hosts.deny contents ...")
            file = open(self.storage_dir + "/user.txt", 'a', encoding = 'utf-8')
            file.write("\n\n\n*****Results of /etc/hosts.deny file content collection*****\n")	
            file.close()
            sp.run('cat /etc/hosts.deny >> ' + self.storage_dir + '/user.txt', shell=True)
        
        except Exception as err:
            self.printsave(f"Error creating directory: {err}")
            return False
        
    

    def main(self):
        return self.make_dir(), self.find_login_inf(), self.find_user_inf()

        
if __name__ == '__main__':
    forensic_project().main()
    #forensic_project(argument..).main()

# parser = argparse.ArgumentParser(description="Takes a linux memory image and automate volatility3 to run against it")
# parser.add_argument('-a', '--application', dest = '' metavar = '' type = str, required = True, help = 'application name')
# parser.add_argument('-t', '--datetime', dest = '' type=str, help = 'format: YYYY-mm-ddTHH:MM:SS')
# parser.add_argument('-d', '--destination', dest = '' type=str, help = 'alpha or real')
# args = parser.parse_args() # 입력받은 인자값을 args에 저장
#VOLATILITY = args.volpath #dest
#source_image = args.filename
#profile = args.profile