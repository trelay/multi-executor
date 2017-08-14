#!/usr/bin/python
import os, re,sys
from remote_exe_new import create_thread
from subprocess import Popen, PIPE
from main import base_fun
from lib import get_current_time
import json


class INFO_FUN(base_fun):

    def __init__(self):
        super(INFO_FUN, self).__init__()

    def get_all_info(self):
        self.info_list=[]
        dev_list = os.listdir("/proc/")
        p= re.compile(r'info$')
        for dev in dev_list:
            match = p.search(dev)
            if match:
                self.info_list.append(dev)
        return self.info_list

    def run(self):
        #argv_list = [{'log_name': 'log_path', 'command_line':'fio_testcommnd'},]

        print >>sys.stderr,"Start Running"
        self.get_all_info()
        argv_list=[]

        for info in self.info_list:
            info_path=os.path.join("/proc/", info)
            command = "cat {0}".format(info_path)
            argv= dict()

            request = {}
            request['command'] = command
            request['request_time'] = get_current_time()
            
            argv["request"]= request
            argv.update(response={})

            argv_list.append(argv)

        create_thread(argv_list)

        print argv_list
        response_list_encodedjson = json.dumps(argv_list)
        return response_list_encodedjson
