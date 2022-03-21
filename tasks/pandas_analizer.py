import matplotlib.pyplot as plt
import numpy as np
class Pandas_analizer():

  def analize_data(self,data_set,group_by,aggregation_param,take):
    if(take==None):
      return data_set.groupby(group_by,as_index=False)[aggregation_param].sum()
    return data_set.groupby(group_by,as_index=False)[aggregation_param].sum().head(take)

  def plot_data(self,data,group_by,aggregation_param,title,ylabel,xlabel):
    data_x_list = [str(value) for value in data[group_by].values.tolist()]
    data_y_list = data[aggregation_param]
    x = np.array(data_x_list)
    y = np.array(data_y_list)
    plt.bar(x,y)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.show()

  def plot_data_as_pie_chart(self,data,labels,title):
    plt.pie(data,labels=labels,shadow=True,startangle=90,autopct='%1.1f%%')
    plt.title(title)
    plt.show()