
from fabric.api import run,env

#user of system
env.user='meupc'
'''env.password='ooolwq'''


def host_type():
	#run('uname -s')
	run('dir')
