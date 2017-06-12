#fab -f test.py -H 192.168.19.102 listadir



from fabric.api import run,env

#user of system
env.user='root'

def host_type():
	#run('uname -s')
	run('dir')

def listadir():
    local("ls")
