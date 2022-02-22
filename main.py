import threading
from tasks import network_commads
import os
from dotenv import load_dotenv
def main():
  load_dotenv()
  target_ip = '192.168.0.14'
  net_exec = network_commads.Command_executer(target_ip)
  target_thread_funcs = [net_exec.lsof,net_exec.tracert_ip,net_exec.ping_ip,net_exec.arp]

  for i in range(4):
    th = threading.Thread(target=target_thread_funcs[i])
    th.start()
    th.join()

if __name__ == '__main__':
    main()

