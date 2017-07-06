# Multi executor

Please read this before use:

 * This tool is an extension for Celesitca Function test platform, as it doesn't support multi-task
 * This can save about more than 80% of the test time for product N****
 * IF you just wanna refer my code, not use it directly, it should be OK


As the test time in Celesitca test platform is so long that I can't withstand, I decide to write an extension for the poor test platform.

I'd like to put it in Github to be a open project since the most of the code was done in my free time(Thanks to my kid, he went to hometown with my wife, so I can work untill 10 o'clock in night.:joy:)

How to add new module to this tool, there are two files are related:

 * multi-executor/main/test.py
 * multi-executor/main/\__init__.py


Code example for test.py:
```python
from main import base_fun    # test.py will be the file you create that handles the function
                             # below is an example, or refer multi-executor/main/main_fio.py, it's been tested.
                             # The infrastructure is defined in file "multi-executor/main/main.py", I'll change it to ABC

class HELP_FUN(base_fun):
    def __init__(self):
        pass
    def run(self):
        return help_msg

```

And et this tool know you have enhanced something, in this format:

```python
from main_test import HELP_FUN   # import the class you made
help_fun = HELP_FUN()            # Create a instance of the class
fun_add('help', help_fun)        # Add thie instance handler to function

```

### At end:
Let me know if there is any bug: trelwan@celestica.com

My wechat & Skype: __Trelay__

