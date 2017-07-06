from main import base_fun
help_msg = """
Your command is not supported, refer below:
        io_test: for fio test
        echo: for echo test
"""

class HELP_FUN(base_fun):
    def __init__(self):
        pass
    def run(self):
        return help_msg
