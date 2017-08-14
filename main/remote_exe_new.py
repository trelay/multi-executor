#!/usr/bin/python
import shlex, os
from subprocess import Popen, PIPE
#from time import sleep
import threading
from lib import get_current_time

def exe_cmd(request, response):
    cmd_line = shlex.split(request['command'])
    p = Popen(cmd_line, stdout=PIPE, stdin=PIPE, stderr=PIPE)
    output = p.communicate()
    returncode = p.returncode

    response.update(stdout=output[0])
    response.update(stderr=output[1])
    response.update(returncode=returncode)
    response.update(exe_time = get_current_time())
    

def create_thread(argv_list):
    io_thread=[]
    for argv in argv_list:
        thread=threading.Thread(target=exe_cmd,kwargs =argv)
        io_thread.append(thread)

    for thread in io_thread: #Add this "for loop" for better understanding
        thread.start()

    for thread in io_thread:
        thread.join()
