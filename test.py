
from fabric.api import run,env

#user of system
env.user='root'

def host_type():
	#run('uname -s')
	run('dir')
