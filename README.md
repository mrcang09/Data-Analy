# 介绍

1.本项目实例主要运用了matosploit，numpy，pandas进行数据的统计，并且以报表形式给出相应的结果

2.最后运用了pyinstaller打包，运用numpy和pandas打包的话文件达到了300MB，实在过大，在此记录下缩小体积的方法

    1.利用虚拟空间pipenv---下载python---下载依赖
    
    2.upx压缩，已经放弃了，不现实
    
3.柱形图的绘制用到了pylab中的arange （可以实现对X轴无序排列），否则自动排列的话问题太多了

4.打包编译后的文件路径使用 `os.path.dirname(os.path.realpath(sys.argv[0]))` 来表示 编译后的exe文件所在的目录，特此做个记录，目录使用"\\"

5.pandas 分组，数据透视表的创建，pandas 和 dataFrame 和numpy array 互转
