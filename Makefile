#
# [FIXME]
#
#

SHELL = /bin/bash

# Many recipes need to be run in the virtual environment, 
# so run them as $(INVENV) command
INVENV = source env/bin/activate ;

##
##  Virtual environment
##     
env:
	python3 -m venv  env
	($(INVENV) pip install -r requirements.txt )

server/credentials.ini: 
	echo "You must manually create server/credentials.ini"

credentials: 	server/credentials.ini

install:	env credentials

start:	env credentials
	bash start.sh 

stop:	
	bash stop.sh

##
## Run test suite. 
## To make Python path search work as needed, we run
## from within the 'server' directory. 
##
test:	env
	$(INVENV) cd server;  nosetests

# 'clean' and 'veryclean' are typically used before checking 
# things into git.  'clean' should leave the project ready to 
# run, while 'veryclean' may leave project in a state that 
# requires re-running installation and configuration steps
# 
clean:
	rm -f *.pyc */*.pyc
	rm -rf __pycache__

veryclean:
	make clean
	rm -rf env



