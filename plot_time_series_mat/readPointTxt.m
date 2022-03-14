function [date,value]=readPointTxt(filename)
%   读取时间序列图中的时间和形变累积量值并输出在date和value中，读取单个文件(一个点）
% filename='G:\InSAR Function\point\alt point\p231_201.txt';
rows=getrow(filename);
date=zeros(rows,1);%日期
value=zeros(rows,1);%形变量值
fid=fopen(filename,'r');
head_index=0;
tline=fgetl(fid);
while head_index<8
    head_index=head_index+1;
    tline=fgetl(fid);
end
index=1;
while ~feof(fid)
    tline = fgetl(fid);
    date1=tline(7:16);
    date2=str2double(date1(1:4))+(str2double(date1(6:7))-1)/12+str2double(date1(9:10))/365;
    date(index,:)=date2;
    value1=tline(63:74);
    value(index,:)=str2double(value1);
    index=index+1;
end
fclose(fid);

