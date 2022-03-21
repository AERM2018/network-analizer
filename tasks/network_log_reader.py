from tasks.pandas_analizer import Pandas_analizer
import pandas as pd
import colorama
class Network_log_reader():
  def __init__(self):
    colorama.init()
  def analizer(self,path=''):
    print(colorama.Fore.RESET,end='')
    pd_analizer = Pandas_analizer()
    firewall_logs = pd.read_csv(path)
    data_set = firewall_logs[firewall_logs['Action']=='allow']
    data_to_plot = pd_analizer.analize_data(data_set,['NAT Destination Port'],'Packets',None)
    data_to_plot = data_to_plot.sort_values(['Packets'],ascending=False).head(5)
    pd_analizer.plot_data(data_to_plot,'NAT Destination Port','Packets','Packets traffic','N. packets','NAT Destination Port')