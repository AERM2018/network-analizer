import os
from helpers import exec_command
from helpers.ssh import get_SSH_client
class Command_executer():
    def __init__(self,target_ip):
        self.target_ip = target_ip

    def ping_ip(self):
        log_file = open('./logs/ping_log.txt','w')
        log_file.write(exec_command.execute(['ping',self.target_ip],return_result=True))
        log_file.close()

    def tracert_ip(self):
        log_file = open('./logs/tracert_log.txt','w')
        log_file.write(exec_command.execute(['tracert',self.target_ip],return_result=True))
        log_file.close()

    def lsof(self):
        ssh = get_SSH_client(self.target_ip,[os.getenv('SSH_USERNAME'),os.getenv('SSH_PASSWD')])
        stdin, stdout, stderr = ssh.exec_command("sudo lsof -i | grep LISTEN",get_pty = True)
        stdin.write(os.getenv('SSH_PASSWD') + "\n")
        stdin.flush()
        listado =stdout.readlines()
        log_file = open('./logs/lsof_log.txt','w')
        for i in listado: 
            log_file.write(i+"\n")
        log_file.close()
        ssh.close() 

    def arp(self):
        log_file = open('./logs/arp_log.txt','w')
        log_file.write(exec_command.execute(['arp','-a'],return_result=True))
        log_file.close()


        