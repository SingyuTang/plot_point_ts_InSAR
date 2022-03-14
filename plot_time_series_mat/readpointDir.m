function deform = readpointDir(dirname)
% clear;clc;
% dirname='G:\InSAR Function\point\wwh';
tmp=dir(dirname);
for i=3:size(tmp)
    pname(i,:)=tmp(i).name;
    filenames(i-2,:)=fullfile(dirname,tmp(i).name);
end
pname(:,end-3:end)=[];
for i=1:size(filenames,1)
    deform(i).pname=pname(i+2,:);
    [deform(i).date,deform(i).value]=readPointTxt(filenames(i,:));
end
deform=deform';
