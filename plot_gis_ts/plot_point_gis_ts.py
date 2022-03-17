import time
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import bendent
import pandas as pd
import sys
import matplotlib.ticker as ticker

plt.rcParams['font.family']=['Times New Roman']
ts_filepath=r"bj_ts_2018_2021.txt"
time_filepath=r"time.txt"
plot_title='Time-series cumulative surface deformation'
img_path=r'23.jpg'#配色图
legend=['p1','p2','p3','p4','p5','p6']#设置图例,不设置则为空
savefig_path='time series of point_18_21.jpg'
major_spacing,minor_spacing=120,100
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
        print()
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

    def plot_ts(self,is_override=False):
        #is_override：是否重写，默认不重写
        self.readpoint()
        self.readtime()
        len_time=len(self.ls_datetime_time)#获取time文件中的时间个数
        len_data=np.shape(np.array(self.ls_ts_str_data))[1]#获取时序文件中的时间点数目
        # print(len_data,len_time)
        if len_time == len_data:
            fig=plt.figure()
            if is_override is False:
                for ts_single_point in self.ls_ts_str_data:
                    plt.plot(self.ls_datetime_time,ts_single_point)
                return fig
            else:
                ax=plt.gca()
                # plt.minorticks_on()#显示次刻度线,打开此功能会覆盖ax.xaxis.set_major_locator(ticker.MultipleLocator(major_spacing))中的设置
                # plt.tick_params(which='both',direction='in')#设置次刻度线朝向，in，out，inout;
                # plt.tick_params(direction='in')  # 设置主坐标轴刻度线朝向，major,minor,both表示主刻度线，次刻度线和都选择
                plt.tick_params(top=True, bottom=True, left=True, right=True,which='both',direction='in')  # 在哪些轴显示刻度线
                ax.grid(color=(136 / 255, 136 / 255, 136 / 255), linestyle='--', linewidth=1, alpha=0.3)
                #主副刻度密度的设置，但是不在中间，原因未知，故不采用
                # ax.xaxis.set_major_locator(ticker.MultipleLocator(major_spacing))
                # ax.xaxis.set_minor_locator(ticker.MultipleLocator(minor_spacing))
                # ax.yaxis.set_minor_locator(ticker.MultipleLocator(minor_spacing))
                return fig,self.ls_datetime_time,self.ls_ts_str_data
        else:
            print('time文件中的时间数不等于ts文件中的时间数，请检查文件。')
            sys.exit(1)

class plot_gis_ts_2(plot_gis_ts):
    '''
    继承了plot_gis_ts类，这个类主要用于对画图进行精化
    '''
    def __init__(self,ts_filepath,time_filepath,title,imgPath,legend=[],savefigPath='Output.jpg'):
        super().__init__(ts_filepath,time_filepath)
        self.plot_title=title
        self.imgPath=imgPath
        self.legend=legend
        self.savefigPath=savefigPath
    def plot_ts_2(self):
        dominant,palette=bendent.palette(self.imgPath)
        list_rgb_palette=np.array(pd.DataFrame(palette).iloc[:,1]).tolist()#panda必须先转为numpy才能转为list
        _,ls_time,ls_data=super().plot_ts(is_override=True)#重写绘制函数
        ls_data=(np.array(ls_data)*1000).tolist()#换算单位
        # print(ls_data)
        # plt.plot()实际上会通过plt.gca()获得当前的Axes对象ax，然后再调用ax.plot()方法实现真正的绘图。
        # plt.gca()获取当前Axes，plt.gcf()，获取当前Figure
        # print(dir(plt.gca()))#很多属性设置都包含在plt.gca()中，如'set_label'，'set_xlim'，'xaxis'等，一般用法先利用plt.gca()获取句柄，再进行属性设置精化图形绘制
        # print(plt.gcf())  # plt.gcf()获取的和plt.figure()创建的类型相同
        ax=plt.gca()
        # print(dir(ax))
        ax.set_title(self.plot_title)#等价于plt.title()
        num_point,num_time=np.array(ls_data).shape[0],np.array(ls_data).shape[1]
        # print(list_rgb_palette[1])
        if num_point<=len(list_rgb_palette):
            for i in range(num_point):
                r,g,b=list_rgb_palette[i][0]/255,list_rgb_palette[i][1]/255,list_rgb_palette[i][2]/255
                ax.plot(ls_time,ls_data[i],color=(r,g,b),marker='o',linewidth=1.5,markersize=3,markerfacecolor='white',markeredgewidth=0.8)


        ax.set_xlabel('Date')
        ax.set_ylabel('Accumulated subsidence : mm')
        ax.legend(self.legend, frameon=True,edgecolor='black',fancybox=False)
        print('图片正在保存...')
        plt.savefig(self.savefigPath,dpi=300)#dpi:图片分辨率
        print("{}已保存。".format(savefig_path))
        # print(dir(plt.rcParams.__dict__))
        # plt.show()
        return plt.gcf(),plt.gca()


plt_ts=plot_gis_ts_2(ts_filepath,time_filepath,plot_title,img_path,legend=legend,savefigPath=savefig_path)
#如果调用plt_ts.plot_ts()则没有plt.show()功能，而plt_ts.plot_ts_2()则包含plt.show()功能
plt_ts.plot_ts_2()

