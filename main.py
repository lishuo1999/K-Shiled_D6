import argparse
from argparse import ArgumentParser
import os
import subprocess as sp

def main():
    parser = argparse.ArgumentParser(description="Automatically collect Linux artifacts script")
    parser.add_argument('-p', '--process', dest = 'process', action = 'store_true', help = 'Collecting data about process')
    parser.add_argument('-n', '--network', dest = 'network', action = 'store_true', help = 'Collecting data about network')
    parser.add_argument('-s', '--system', dest = 'system', action = 'store_true', help = 'Collecting data about system')
    parser.add_argument('-f', '--file', dest = 'file', action = 'store_true', help = 'Collecting data about file')
    parser.add_argument('-u', '--user', dest = 'user', action = 'store_true', help = 'Collecting data about user')
    args = parser.parse_args() # 입력받은 인자값을 args에 저장

    try:
        if args.process:
            sp.call('python3 Process_info.py', shell=True)
        elif args.network:
            sp.call('python3 network_info.py', shell=True)
        elif args.system:
            sp.call('python3 system_info.py', shell=True)
        elif args.file:
            sp.call('python3 File_Info.py', shell=True)
        elif args.user:
            sp.call('python3 User_info.py', shell=True)

    except Exception as err:
        print("Error: {err}")
        return False
    
if __name__ == '__main__':
    main()
