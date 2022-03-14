import time
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
plt.rcParams['font.family']=['STFangsong']
ts_filepath=r"G:\InSAR Function\plot_gis_ts\Output_ts_point1.txt"
time_filepath=r"G:\InSAR Function\plot_gis_ts\time.txt"
#list->numpy : np.array(x)
#numpy-> : y.tolist()
# np_ts_data=np.array(ts_data)
# for tmp1 in np_ts_data:
#     plt.plot(tmp1)
# plt.show()

class plot_gis_ts:
    def __init__(self,ts_filepath,time_filepath):
        self.ts_filepath=ts_filepath
        self.time_filepath=time_filepath
    def readpoint(self):
        '''
        提取文件中的第一行（head）和点的时序数据（只包含value）并返回
        :return: str_head : str ; ts_data_ls : list
        '''
        with open(self.ts_filepath) as f:
            file_content = f.readlines()
            f.close()
        str_head = file_content[0]
        list_data = file_content[1:]
        num_point = len(file_content) - 1
        list_head_tmp = str_head.split(',')
        num_ts = len(list_head_tmp) - 2
        ts_data_ls = []
        list_point_id = []
        for data_line in list_data:
            point_id = data_line.split(',')[1]
            list_point_id.append(point_id)
            list_data = data_line.split(',')[2:]
            float_data = [float(x) for x in list_data]
            ts_data_ls.append(float_data)
        self.str_head,self.ls_ts_str_data=str_head,ts_data_ls
        # return str_head,ts_data_ls

    def readtime(self):
        '''
        读取文件中的影像时间并返回对应的时间元组列表，以列表形式返回，列表中的元素为datetime，如2018-11-11 00:00:00，可直接在matplot模块中作为横坐标
        :return:
        '''
        with open(self.time_filepath) as f:
            time_text=f.readlines()
            f.close()
        float_time=[float(x) for x in time_text]
        np_time=np.array(float_time)#ndarray类型
        np_int_year=np.floor(np_time/10000).astype('int16')#ndarray类型
        np_int_month=np.floor(np_time/100-np_int_year*100).astype('int16')
        np_int_day=np.floor(np_time-np_int_year*10000-np_int_month*100).astype('int16')
        ls_datetime_time=[]
        for year,month,day in zip(np_int_year,np_int_month,np_int_day):
            Y_M_D=str(year)+'-'+str(month)+'-'+str(day)
            tm_time=datetime.strptime(Y_M_D,"%Y-%m-%d")
            ls_datetime_time.append(tm_time)
        self.ls_datetime_time=ls_datetime_time
        # return ls_datetime_time

    def plot_ts(self):
        self.readpoint()
        self.readtime()
        for ts_single_point in self.ls_ts_str_data:
            plt.plot(self.ls_datetime_time,ts_single_point)


plt_ts=plot_gis_ts(ts_filepath,time_filepath)
plt_ts.plot_ts()
plt.show()
