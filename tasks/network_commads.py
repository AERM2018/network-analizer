import math
import os
from helpers import exec_command
from helpers.ssh import get_SSH_client
from tasks.pandas_analizer import Pandas_analizer
import colorama
class Command_executer():
    colorama.init()
    def __init__(self,target_ips):
        self.target_ips = target_ips

    def ping_ip(self):
        n_tries = 20
        log_file = open('./logs/ping_log.txt','w')
        for target_ip in self.target_ips:
            log_file.write(exec_command.execute(['ping',target_ip,'-n','{}'.format(n_tries)],return_result=True))
        print(colorama.Fore.LIGHTYELLOW_EX+'--> Log saved in the ping_log.txt file in logs folder <--')
        log_file.close()
        log_file = open('./logs/ping_log.txt','r')
        log_lines = log_file.readlines()[2:(n_tries+1)]
        response_times = []
        time = ''
        for line in log_lines:
            if(line not in 'Tiempo de espera agotado para esta solicitud.'):
                response_line = line.split(' ')[-2]
                if ('=' in response_line) :
                    response_times.append(int(response_line.split('=')[1].split('m')[0]))
                elif('<' in response_line):
                    response_times.append(int(response_line.split('<')[1].split('m')[0]))

                    
        log_file.close()
        avg = math.floor(sum(response_times)/len(response_times))
        pd_analizer = Pandas_analizer()
        pie_labels = 'packets with rs >= {}'.format(avg),'packets with rs < {}'.format(avg)
        pd_analizer.plot_data_as_pie_chart(
            data=[
                int(len([res for res in response_times if res >= avg])*100/len(response_times)),
                int(len([res for res in response_times if res < avg])*100/len(response_times))],
            labels=pie_labels,
            title='Packets response time against response time average'
        )

    def tracert_ip(self):
        log_file = open('./logs/tracert_log.txt','w')
        for target_ip in self.target_ips:
            log_file.write(exec_command.execute(['tracert',target_ip],return_result=True))
        print(colorama.Fore.LIGHTYELLOW_EX+'--> Log saved in the tracert_log.txt file in logs folder <--')
        log_file.close()

    def lsof(self):
        for target_ip in self.target_ips:
            ssh = get_SSH_client(target_ip,[os.getenv('SSH_USERNAME'),os.getenv('SSH_PASSWD')])
            stdin, stdout, stderr = ssh.exec_command("sudo lsof -i | grep LISTEN",get_pty = True)
            stdin.write(os.getenv('SSH_PASSWD') + "\n")
            stdin.flush()
            listado =stdout.readlines()
            log_file = open('./logs/lsof_log.txt','w')
            for i in listado: 
                log_file.write(i+"\n")
            print(colorama.Fore.LIGHTYELLOW_EX+'--> Log saved in the lsof_log.txt file in logs folder <--')
            log_file.close()
            ssh.close() 

    def arp(self):
        log_file = open('./logs/arp_log.txt','w')
        log_file.write(exec_command.execute(['arp','-a'],return_result=True))
        print(colorama.Fore.LIGHTYELLOW_EX+'--> Log saved in the arp_log.txt file in logs folder <--')
        log_file.close()

    def nslookup(self,):
        log_file = open('./logs/nslookup_log.txt','w')
        print(self.target_ips)
        for target_ip in self.target_ips:
            log_file.write('Resolution of {}...\n'.format(target_ip))
            log_file.write(exec_command.execute(['nslookup','-type=any',target_ip],return_result=True))
            log_file.write('----------------------\n')
        log_file.close()

    def route(self):
        log_file = open('./logs/route_table_log.txt','w')
        for target_ip in self.target_ips:
            log_file.write(exec_command.execute(['route','PRINT'],return_result=True))
        print(colorama.Fore.LIGHTYELLOW_EX+'--> Log saved in the route_table_log.txt file in logs folder <--')
        log_file.close()

    def get_host_name(self):
        return exec_command.execute('hostname',return_result=True)

        