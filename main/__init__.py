from main import base_fun
from gen_fun import fun_add

from main_help import HELP_FUN
from main_fio import FIO_FUN
from test_info import INFO_FUN

help_fun = HELP_FUN()
fio_fun = FIO_FUN()
info_fun = INFO_FUN()

fun_add("help",help_fun)
fun_add("nvme_fio",fio_fun)
fun_add("info_test",info_fun)

#fun_add("more_test",more_fun)
