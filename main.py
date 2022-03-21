import threading
from turtle import color
from tasks import network_commads,vulnerability, criptography,network_log_reader
import os
from dotenv import load_dotenv
import time
import colorama
def main():
  load_dotenv()
  colorama.init()
  target_ip = os.getenv('TARGET_IP')
  net_exec = network_commads.Command_executer([target_ip])
  vul_exec= vulnerability.Vulnerability_executor(target_ip)
  crip_exec = criptography.Criptography_executor()
  log_reader = network_log_reader.Network_log_reader()
  target_netcommnads_funcs = [net_exec.ping_ip,net_exec.arp, net_exec.lsof]
  target_vulnerability_funcs = [vul_exec.exec_port_scanner,vul_exec.exec_sniffer,vul_exec.exec_sqli,vul_exec.exec_wifi_scanner]
  target_criptography_funcs = [[crip_exec.exec_cipher,'HOLA MUNDO'],[crip_exec.generate_key,None],[crip_exec.generate_md5,'Example']]

  timei = time.time()
  # Run networkin commands threads
  for i in range(len(target_netcommnads_funcs)):
    thread_name = crip_exec.generate_md5('th-commands-{}'.format(i),True)
    th = threading.Thread(target=target_netcommnads_funcs[i],name=thread_name)
    print(colorama.Fore.GREEN+'Thread {} is starting up.'.format(thread_name))
    th.start()
    th.join()

  # Run vulnerability funcs
  # for i in range(len(target_vulnerability_funcs)):
  #   thread_name = crip_exec.generate_md5('th-vuln-{}'.format(i),True)
  #   th = threading.Thread(target=target_vulnerability_funcs[i],name=thread_name)
  #   print(colorama.Fore.GREEN+'Thread {} is starting up.'.format(thread_name))
  #   th.start()
  #   th.join()

# Run criptography funcs
  # for i in range(len(target_criptography_funcs)):
  #   thread_name = crip_exec.generate_md5('th-crypto-{}'.format(i),True)
  #   if target_criptography_funcs[i][1] != None:
  #     th = threading.Thread(target=target_criptography_funcs[i][0],args=[target_criptography_funcs[i][1]],name=thread_name)
  #   else:
  #     th = threading.Thread(target=target_criptography_funcs[i][0],name=thread_name)
  #   print(colorama.Fore.GREEN+'Thread {} is starting up.'.format(thread_name))
  #   th.start()
  #   th.join()

  # Run network log reader
  # thread_name = crip_exec.generate_md5('th-logger-1',True)
  # th = threading.Thread(target=log_reader.analizer,args=['./logs/firewall_logs.csv'],name=thread_name)
  # print(colorama.Fore.GREEN+'Thread {} is starting up.'.format(thread_name))
  # th.start()
  # th.join()

  timef = time.time()
  print(colorama.Fore.WHITE+'----------------------------\n')
  print(colorama.Fore.LIGHTMAGENTA_EX+'Time taken: {:.5f} secs.\n'.format(timef-timei))
  print(colorama.Fore.WHITE+'----------------------------\n')

if __name__ == '__main__':
    main()

