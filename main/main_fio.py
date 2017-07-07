#!/usr/bin/python
import os, re,sys
from remote_exe import create_thread
from subprocess import Popen, PIPE
from main import base_fun

fio_cmd = "fio --name=global --ioengine=sync --bs=4k --rw=read  --filename=/dev/{0} --runtime={1} --direct=1 -numjobs=1  -iodepth=4 --name=job"

stress_time = 60

class FIO_FUN(base_fun):

    def __init__(self):
        super(FIO_FUN, self).__init__()

    def get_all_nvme(self):
        self.nvme_list=[]
        dev_list = os.listdir("/dev/")
        #dev_list =['kmsg','stdin','nvme0','nvme0n1', 'nvme1','nvme10','nvme10n1','nvme11','nvme11n1']
        p= re.compile(r'nvme\d+n\d')
        for dev in dev_list:
            match = p.search(dev)
            if match:
                self.nvme_list.append(dev)
        return self.nvme_list

    def run(self):
        #argv_list = [{'log_name': 'log_path', 'command_line':'fio_testcommnd'},]

        print >>sys.stderr,"Start Running"
        self.get_all_nvme()
        argv_list=[]
        for nvme in self.nvme_list:
            argv= dict()
            argv.update(log_name= nvme)
            command = fio_cmd.format(nvme,stress_time)
            argv.update(command_line = command)
            argv_list.append(argv)

        create_thread(argv_list)
        return "command executed"
