class CMDMAP(object):
    def __init__(self):
        self.cmds = {}

    def fun_get(self, cmd):
        if self.cmds.get(cmd)==None:
           cmd = 'help'
        return self.cmds.get(cmd)

    def fun_add(self, cmd, fun_handler):
        self.cmds[cmd] = fun_handler

cmd_map = CMDMAP()

def fun_get(cmd):
    return cmd_map.fun_get(cmd)

def fun_add(cmd, fun_handler):
    cmd_map.fun_add(cmd, fun_handler)

