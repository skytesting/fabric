#! /usr/local/bin/python 

#fab -f test.py -H 192.168.19.102 listadir



from fabric.api import run,env
from fabric.operations import local
from fabric.context_managers import cd
from fabric.contrib.files import exists
import logging

#user of system
#env.user='broker'
env.use_ssh_config = True

def host_type():
	#run('uname -s')
    with cd('/opt/deployment/fabric/'):
	if exists("nova_testa"):
	 #run('mkdir nova_testa')
         print ("no vale apena")
	else:
	  run('mkdir nova_testa')
	 #logging.warning('no vale apena')	
	listadir()

def listadir():
    run("ls -lart")
