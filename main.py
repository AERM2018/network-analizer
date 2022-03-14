import threading
from tasks import network_commads,vulnerability, criptography
import os
from dotenv import load_dotenv
def main():
  load_dotenv()
  target_ip = os.getenv('TARGET_IP')
  net_exec = network_commads.Command_executer(target_ip)
  vul_exec= vulnerability.Vulnerability_executor(target_ip)
  crip_exec = criptography.Criptography_executor("HOLA MUNDO")
  target_netcommnads_funcs = [net_exec.tracert_ip,net_exec.ping_ip,net_exec.arp, net_exec.lsof]
  target_vulnerability_funcs = [vul_exec.exec_ddos_attack]
  target_criptography_funcs = [crip_exec.exec_cipher,crip_exec.generate_key]

  # Run networkin commands threads
  for i in range(len(target_netcommnads_funcs)):
    th = threading.Thread(target=target_netcommnads_funcs[i])
    th.start()
    th.join()

  # Run vulnerability funcs
  for func in target_vulnerability_funcs:
    th = threading.Thread(target=func)
    th.start()
    th.join()

# Run criptography funcs
  for func in target_criptography_funcs:
    th = threading.Thread(target=func)
    th.start()
    th.join()


if __name__ == '__main__':
    main()

