#!/usr/bin/python
import shlex, os
from subprocess import Popen, PIPE
#from time import sleep
import threading

def exe_cmd(log_name, command_line):
    args = shlex.split(command_line)
    log_dir=os.path.join(os.path.dirname(__file__),"..", "log")
    if not os.path.isdir(log_dir):
        os.mkdir(log_dir)
    file_name= os.path.join(log_dir, log_name)

    f_d=open(file_name,"w+")
    p = Popen(args, stdout=f_d, stdin=PIPE, stderr=f_d)
        #Dump stdout and stderr to log file
    output = p.communicate()
    print command_line+ " " + "executed!"
    f_d.close()

def create_thread(argv_list):
    io_thread=[]
    for argv in argv_list:
        thread=threading.Thread(target=exe_cmd,kwargs =argv)
        io_thread.append(thread)

    for thread in io_thread: #Add this "for loop" for better understanding
        thread.start()

    for thread in io_thread:
        thread.join()
