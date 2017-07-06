from main import base_fun
from gen_fun import fun_add

from main_fio import FIO_FUN
from main_help import HELP_FUN

fio_fun = FIO_FUN()
help_fun = HELP_FUN()

fun_add("help",help_fun)
fun_add("io_test",fio_fun)

#fun_add("more_test",more_fun)
