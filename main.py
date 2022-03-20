import threading
from tasks import network_commads,vulnerability, criptography
import os
from dotenv import load_dotenv
def main():
  load_dotenv()
  target_ip = os.getenv('TARGET_IP')
  net_exec = network_commads.Command_executer(target_ip)
  vul_exec= vulnerability.Vulnerability_executor(target_ip)
  crip_exec = criptography.Criptography_executor()
  target_netcommnads_funcs = [net_exec.tracert_ip,net_exec.ping_ip,net_exec.arp, net_exec.lsof]
  target_vulnerability_funcs = [vul_exec.exec_sqli]
  target_criptography_funcs = [[crip_exec.exec_cipher,'HOLA MUNDO'],[crip_exec.generate_key,None],[crip_exec.generate_md5,'Example']]

  # Run networkin commands threads
  # for i in range(len(target_netcommnads_funcs)):
  #   th = threading.Thread(target=target_netcommnads_funcs[i])
  #   th.start()
  #   th.join()

  # Run vulnerability funcs
  for i in range(len(target_vulnerability_funcs)):
    thread_name = crip_exec.generate_md5('th-vuln-{}'.format(i),True)
    th = threading.Thread(target=target_vulnerability_funcs[i],name=thread_name)
    print('Thread {} is starting up.'.format(thread_name))
    th.start()
    th.join()

# Run criptography funcs
  # for i in range(len(target_criptography_funcs)):
  #   thread_name = crip_exec.generate_md5('th-crypto-{}'.format(i),True)
  #   if target_criptography_funcs[i][1] != None:
  #     th = threading.Thread(target=target_criptography_funcs[i][0],args=[target_criptography_funcs[i][1]],name=thread_name)
  #   else:
  #     th = threading.Thread(target=target_criptography_funcs[i][0],name=thread_name)
  #   print('Thread {} is starting up.'.format(thread_name))
  #   th.start()
  #   th.join()


if __name__ == '__main__':
    main()

