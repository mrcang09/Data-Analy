import pandas as pd
import matplotlib as plt
import xlrd as xr
import numpy as np
import seaborn as sns
import sys,os
from pylab import *
from matplotlib import pyplot as plt


def cur_file_dir():
    # 获取脚本路径

    path = sys.path[0]

    # 判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径

    if os.path.isdir(path):

        return path

    elif os.path.isfile(path):

        return os.path.dirname(path)

# data_name = 'data.xlsx'
#
# path2 = cur_file_dir() + "\\" + data_name
# path1 = os.path.dirname(os.path.realpath(__file__))
# path = path1 + "\\" + data_name
# print(path2)
#
#
# data = pd.read_excel(path2)
#
# Date_ = 'DATE'
# Leader_ = 'MGR'
#
# dataGroup = data.groupby(by=Date_)
# dataGroup2 = data.groupby(by=Leader_)
#
# list1 = list(dataGroup.groups.keys())
# list2 = list(dataGroup2.groups.keys())
#
# # data = pd.DataFrame(np.arange())
# print("=======================================")
# print("开始解析数据..")
# print("获取到的Leader人员..")
# print(list2)
# print("=======================================")
# row = str(len(data))
# col = str(data.columns.size)
# print("数据中行数：" + row)
# print("数据中列数：" + col)
# print("=======================================")
# print("获取到的日期种类")
# print(list1)
# print("=======================================")
#
# Leader_Num = len(list2)
# print("leader的数目是：")
# print(Leader_Num)
# for i in range(0,Leader_Num):
#     print("当前的Leader序号")
#     print(i)
#
# print("获取一个leader的组")
# sort = dataGroup2.get_group(list2[0])
# print(sort)
# print("=======================================")
# print("将本leader组在转换成dataFrame格式")
# sort_new = pd.DataFrame(sort)
# print(sort_new)
# print("=======================================")
# print("根据日期对Leader表的分类")
# dataGroup3 = sort_new.groupby(by=Date_)
# list3 = list(dataGroup3.groups.keys())
# sort = dataGroup3.get_group(list3[0])
# print(sort)
# print("=======================================")
# print("再次转换-")
# sort = pd.DataFrame(sort)
#
# print("=======================================")
# row = str(len(sort))
# print("本leader所管辖 - 当天员工数目:" + row)
# print("=======================================")
# print("获取所有员工编号")
# NEW = sort['RTE NBR ']
# print(NEW)
# print("获取所有员工STOP点数")
# NEW1 = sort['TOTAL STOP']
# print(NEW1)
# print("获取所有员工PKG数目")
# NEW2 = sort['TOTAL PKG']
# print(NEW2)
#
# print("=======================================")
# print("转换为列表..")
#
#
#
# print("转换员工编号")
# RTE_NBR = list(NEW)
# print(RTE_NBR)
# print("转换员工STOP点数")
# TOTAL_STOP = list(NEW1)
# print(TOTAL_STOP)
# print("转换员工PKG数目")
# TOTAL_PKG = list(NEW2)
# print(TOTAL_PKG)
#
# print("=======================================")
# print("开始绘制..")
#
#
#
# RTE_NBR_Num=[int(i) for i in RTE_NBR]  #提取员工坐标进行转化
# # value=sort.T.values   #将冠亚季军所吃热狗的数量转化成matrix，也就是[[25,24,22],[50.0,31.0,23.5],...]
# print("输出转置后的数据")
# one = np.array(TOTAL_STOP)
# two = np.array(TOTAL_PKG)
# Second = one + two
# TOTAL_PKG_LIST = Second.tolist()
# print(TOTAL_PKG_LIST)

#
# mode = 1
# if mode == 1:
#     print("=======================================")
#     print("测试绘制1")
#     fig,ax=plt.subplots()
#     #解决自动顺序排列
#     plt.xticks(arange(len(RTE_NBR)), RTE_NBR)
#
#     #注意绘制顺序
#     ax.bar(arange(len(RTE_NBR)),TOTAL_PKG_LIST,color="red")
#     ax.bar(arange(len(RTE_NBR)),TOTAL_STOP,color="green")
#     # plt.text(4, 1, str(list2[0]), ha='center', wrap=True)
#
#     ax.set(xlabel="RTE NBR",title="( MGR:"+str(list2[0])+" ) "+"Fedex "+str(list3[0])+" Working Detail")
#
#     # plt.text(5, 10, str(list2[0]), fontsize=18, style='oblique', ha='center',va='top',wrap=True)
#
#
#     #用于解决柱状图的间距太窄的问题
#     text = ax.text(0.02,0.90,"")  #设置文字
#     text.set_position((0.9,.9))#不能超过1，和上面的设置是一样的
#     for x, y,z,v in zip(arange(len(RTE_NBR)), TOTAL_PKG_LIST,TOTAL_PKG,TOTAL_STOP):
#         plt.text(x-0.5, y, '%d/%d'%(z,v))
#     # for x,y in zip(arange(len(RTE_NBR)),)
#
#     ax.legend(["TOTAL PKG","TOTAL STOP"])  #设置图例
#
#
#     plt.show()
#
#     fig.savefig("Working_Detail.png")
# else:
#     print("=======================================")
#     # NEW = sort['RTE NBR ']
#     #     # print(NEW)
#     #     # print("获取所有员工STOP点数")
#     #     # NEW1 = sort['TOTAL STOP']
#     #     # print(NEW1)
#     #     # print("获取所有员工PKG数目")
#     #     # NEW2 = sort['TOTAL PKG']
#     f, ax = plt.subplots(figsize=(12, 6))
#     print("测试绘制2")
#     sns.set(style='white', font_scale=1.2)
#     # 保证可以显示中文字体
#     plt.rcParams['font.sans-serif'] = 'simhei'
#     # 设置字体大小
#     font1 = {'family': 'simhei',
#              'weight': 'normal',
#              'size': 18, }
#     # 使用数据透视表 (透视表的意思就是将数据进行转置，程序员对齐进行筛选)
#     region_pivot = pd.pivot_table(sort, values='TOTAL STOP',index='RTE NBR ').reset_index().sort_values(
#         ascending=False, by='TOTAL STOP')
#
#     region_pivot1 = pd.pivot_table(sort, values='TOTAL PKG', index='RTE NBR ').reset_index().sort_values(
#         ascending=False,by='TOTAL PKG')
#
#
#
#
#     RTE_NBR = region_pivot['RTE NBR '].values
#     plt.xticks(arange(len(RTE_NBR)), RTE_NBR)
#     print("=======================================")
#     print("查看透视表")
#     print(RTE_NBR)
#     # 画柱形图
#
#
#     #这里需要改变下
#     bar1 = plt.bar(arange(len(RTE_NBR)), region_pivot['TOTAL STOP'].values + region_pivot1['TOTAL PKG'].values, color='Red')
#     bar = plt.bar(arange(len(RTE_NBR)), region_pivot['TOTAL STOP'].values, color='dodgerblue')
#
#
#
#     # bar.set_color('green')
#     # 给条形图添加数据标注
#     for x, y in enumerate(region_pivot['TOTAL STOP'].values):
#         print("=======================================")
#         print("输出x测试数据")
#         print(x)
#         print("输出y测试数据")
#         print(y)
#         plt.text(x-0.2, y, "%d" % y)
#     # 删除所有边框
#     ax.spines['right'].set_visible(False)
#     ax.spines['top'].set_visible(False)
#     ax.spines['bottom'].set_visible(False)
#     ax.spines['left'].set_visible(False)
#
#     plt.tick_params(labelsize=14)
#     plt.xlabel('MGR', font1)
#     plt.ylabel('Total PKG && STOP', font1)
#     plt.title("( MGR:"+str(list2[0])+" ) "+"Fedex "+str(list3[0])+" Working Detail", font1)
#
#     ax.legend(["TOTAL PKG", "TOTAL STOP"])  # 设置图例
#
#     plt.show()


def Plant(RTE_NBR,TOTAL_PKG_STOP_LIST,TOTAL_STOP,Current_MGR,Current_DATE):
    print("=======================================")
    print("测试绘制1")

    CM1 = str(Current_MGR)
    CD1 = str(Current_DATE)

    CM = str(Current_MGR).replace(" ", "")+"_"
    CD = str(Current_DATE).replace(" ", "").replace(":","_").replace("/","_")+"_"

    fig, ax = plt.subplots()
    # 解决自动顺序排列
    plt.xticks(arange(len(RTE_NBR)), RTE_NBR)

    # 注意绘制顺序
    ax.bar(arange(len(RTE_NBR)), TOTAL_PKG_STOP_LIST, color="red")
    ax.bar(arange(len(RTE_NBR)), TOTAL_STOP, color="green")
    # plt.text(4, 1, str(list2[0]), ha='center', wrap=True)

    ax.set(xlabel="RTE NBR", title="(MGR:" + CM1 + ")" + "Fedex" + CD1 + "Working_Detail")

    # plt.text(5, 10, str(list2[0]), fontsize=18, style='oblique', ha='center',va='top',wrap=True)

    # 用于解决柱状图的间距太窄的问题
    text = ax.text(0.02, 0.90, "")  # 设置文字
    text.set_position((0.9, .9))  # 不能超过1，和上面的设置是一样的
    for x, y, z, v in zip(arange(len(RTE_NBR)), TOTAL_PKG_STOP_LIST, TOTAL_PKG, TOTAL_STOP):
        plt.text(x - 0.5, y, '%d/%d' % (v, z))
    # for x,y in zip(arange(len(RTE_NBR)),)

    ax.legend(["TOTAL PKG", "TOTAL STOP"])  # 设置图例

    # plt.show()



    fig.savefig("MGR_"+CM+CD+"Working_Detail.png")
    pass


if __name__ == '__main__':
    data_name = 'data.xlsx'
    # path2 = cur_file_dir() + "\\" + data_name
    # path1 = os.path.dirname(os.path.realpath(__file__))
    # path = path1 + "\\" + data_name
    # print("当前路径：")
    # print(path2)
    path1 = os.path.dirname(os.path.realpath(sys.argv[0]))
    path2 = path1 + "\\" + data_name

    data = pd.read_excel(path2)

    Date_ = 'DATE'
    Leader_ = 'MGR'

    dataGroup = data.groupby(by=Date_)
    dataGroup2 = data.groupby(by=Leader_)

    list1 = list(dataGroup.groups.keys())
    list2 = list(dataGroup2.groups.keys())


    print("=======================================")
    print("开始解析数据..")
    print("获取到的Leader人员..")
    print(list2)
    print("=======================================")
    row = str(len(data))
    col = str(data.columns.size)
    print("数据中行数：" + row)
    print("数据中列数：" + col)
    print("=======================================")
    print("获取到的日期种类")
    print(list1)
    print("=======================================")


    Leader_Num = len(list2)
    print("leader的数目是：")
    print(Leader_Num)
    for i in range(0, Leader_Num):
        print("当前的Leader序号")
        print(i)


        """           12/26/19"""
        """           12/26/19"""


        print("获取一个leader的组")
        sort = dataGroup2.get_group(list2[i])
        print(sort)
        print("=======================================")
        print("将本leader组在转换成dataFrame格式")
        sort_new = pd.DataFrame(sort)
        print(sort_new)
        print("=======================================")
        print("根据日期对Leader表的分类")
        dataGroup3 = sort_new.groupby(by=Date_)
        list3 = list(dataGroup3.groups.keys())

        Date_Num = len(list3)
        print("当前leader的日期数量")
        print(Date_Num)

        for num_date in range(0,Date_Num):

            print("打印本日期下的Sort和Num_Date")

            print(sort)
            print(list3[num_date])

            if "/" in str(list3[num_date]):
                Fore_Date_Num = str(list3[num_date])
            else:
                Fore_Date_Num = list3[num_date]
            print("=======================================")
            print("新的Fore——Date——Num")
            print(Fore_Date_Num)

            print("=======================================")
            print("再次转换-")

            sort2 = dataGroup3.get_group(Fore_Date_Num)
            print(sort2)
            print("=======================================")
            print("再次转换-")
            sort3 = pd.DataFrame(sort2)

            print("=======================================")
            row = str(len(sort3))
            print("本leader所管辖 - 当天员工数目:" + row)
            print("=======================================")
            print("获取所有员工编号")
            NEW = sort3['RTE NBR ']
            print(NEW)
            print("获取所有员工STOP点数")
            NEW1 = sort3['TOTAL STOP']
            print(NEW1)
            print("获取所有员工PKG数目")
            NEW2 = sort3['TOTAL PKG']
            print(NEW2)

            print("=======================================")
            print("转换为列表..")

            print("转换员工编号")
            RTE_NBR = list(NEW)
            print(RTE_NBR)
            print("转换员工STOP点数")
            TOTAL_STOP = list(NEW1)
            print(TOTAL_STOP)
            print("转换员工PKG数目")
            TOTAL_PKG = list(NEW2)
            print(TOTAL_PKG)

            print("=======================================")
            print("开始绘制..")

            RTE_NBR_Num = [int(i) for i in RTE_NBR]  # 提取员工坐标进行转化
            # value=sort.T.values   #将冠亚季军所吃热狗的数量转化成matrix，也就是[[25,24,22],[50.0,31.0,23.5],...]
            print("输出转置后的数据")
            one = np.array(TOTAL_STOP)
            two = np.array(TOTAL_PKG)
            Second = one + two
            TOTAL_PKG_STOP_LIST = Second.tolist()
            print(TOTAL_PKG_STOP_LIST)

            Plant(RTE_NBR, TOTAL_PKG_STOP_LIST, TOTAL_STOP, list2[i], list3[num_date])
