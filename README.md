Executive 
=========

Preserve your precious executive function with a command-line task system that decides for you. (Original Source Code by Toon Alfrink)

**Compatibility update**
=========
For your convenience, we have made this version of our precious Executive Function compatible both with Python 2.7 and Python 3.6+

**Python 3 Transition**

`futurize` has been used to make the source code compatible with Python 3 as well as Pyton 2.7. For details please visit https://python-future.org/futurize.html

**Installation**
=========

Install Python 2.7 from here: https://www.python.org/downloads/release/python-2717/

Install Python 3.6.12 from here: https://www.python.org/downloads/release/python-3612/
For newer versions of Python please visit https://www.python.org

**Pull everything from Github**

`git clone https://github.com/AhmadrezaRahabri/executive /path/to/executive`

**Make sure your pythonpath contains the directory you just pulled**

unix: `export PYTHONPATH=/path/to/executive`

windows: `set export PYTHONPATH=/path/to/executive`

Mac: `PYTHONPATH="/path/to/executive:${PYTHONPATH}"`

**Install dependencies**

`pip install peewee`
`pip install pytz`

To install these packages with conda run:

`conda install -c conda-forge`  `peewee conda install -c anaconda pytz`

**on mac you may have some locale issues**

  `export LC_ALL=en_US.UTF-8`
  `export LANG=en_us.UTF-8`

**Usage**
=========

```
$ python executive/actions/decide.py
 
 1: 2020-09-07: Add a first project using 'ex addproject (name) [parent id]'
$ python executive/actions/addproject.py demo
created project 1: demo
$ python executive/actions/decide.py
> demo 
 2: 2020-09-07: Add an action to project 1: demo
$ python executive/actions/add.py
name? 
 > demonstrate usage of executive
deadline? 
 > 2020-10-01
project? 
 > 1
context? 
 > 
$ python executive/actions/decide.py
 
 1: 2020-09-07: Add a first project using 'ex addproject (name) [parent id]'
$ python executive/actions/done.py 1
Well done!
Set action 'Add a first project using 'ex addproject (name) [parent id]'' to completed.
call decide.py for your next action
$ python executive/actions/decide.py
> demo 
 2: 2020-09-07: Add an action to project 1: demo
$ python executive/actions/done.py 2
Well done!
Set action 'Add an action to project 1: demo' to completed.
call decide.py for your next action
$ python executive/actions/decide.py
> demo 
 3: 2020-10-01: demonstrate usage of executive
$ python executive/actions/add.py
name? 
 > come up with some backlog items for executive
deadline? 
 > 2020-10-02
project? 
 > 1
context? 
 > 
$ python executive/actions/add.py
name? 
 > have someone do a test run of the installation instructions
deadline? 
 > 2020-10-03
project? 
 > 1
context? 
 > 
$ python executive/actions/decide.py
> demo 
 3: 2020-10-01: demonstrate usage of executive
$ python executive/actions/done.py 3
Well done!
Set action 'demonstrate usage of executive' to completed.
call decide.py for your next action
```



