#!/usr/bin/python
import os, re
from remote_exe import create_thread
from subprocess import Popen, PIPE
from main import base_fun

class FIO_FUN(base_fun):

    def __init__(self):
        super(FIO_FUN, self).__init__()

    def get_all_nvme(self):
        self.nvme_list=[]
        dev_list =['kmsg','stdin','nvme0','nvme0n1', 'nvme1','nvme10','nvme10n1','nvme11','nvme11n1']
        p= re.compile(r'nvme\d+n\d')
        for dev in dev_list:
            match = p.search(dev)
            if match:
                self.nvme_list.append(dev)
        return self.nvme_list

    def run(self):

        self.get_all_nvme()
        argv_list=[]
        for nvme in self.nvme_list:
            argv= dict()
            argv.update(log_name= nvme)
            argv.update(command_line="echo "+ nvme)
            argv_list.append(argv)
    
        create_thread(argv_list)
        return "command executed"
