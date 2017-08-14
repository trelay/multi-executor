from main import base_fun
import json
help_msg = """
Your command is not supported, refer below:
        nvme_fio: fio test for NVMe SSD
        echo: for echo test
"""

class HELP_FUN(base_fun):
    def __init__(self):
        pass
    def run(self):
        response_list_encodedjson = json.dumps(help_msg)
        return response_list_encodedjson
