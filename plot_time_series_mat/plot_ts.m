clear;clc;
dir='C:\Users\tang xingyou\Desktop\bj2021\point';
deform=readpointDir(dir);
hold on;
for index=1:size(deform,1)
    plot(deform(index).date,deform(index).value*1000,'-s','marker','.','markersize',12);
end
 xlabel('日期');
 ylabel('形变量(mm)');
 legend('P1','P2','P3')
 
 %% %%%%%%%%%%%%%%%%%%
 clear;clc;
 dir1='.\point\txy';
 dir2='.\point\df';
 dir3='.\point\wwh';
 deform1=readpointDir(dir1);
 deform2=readpointDir(dir2);
 deform3=readpointDir(dir3);
 