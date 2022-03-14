function daterow=getrow(filename)
f=fopen(filename,'r');
head_index=0;
tline=fgetl(f);
while head_index<8
    head_index=head_index+1;
    tline=fgetl(f);
end
daterow=0;
while ~feof(f)
    tline = fgetl(f);
    daterow=daterow+1;
end
fclose(f);
end