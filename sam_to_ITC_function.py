import os
import sys
samfile=sys.argv[1]
countdict={}

if not os.path.isfile('./ITC_ANNOTATION'):
    raise Exception("현재 폴더에 ITC_ANNOTATIN 파일이 없습니다")

os.system("cat ITC_ANNOTATION |awk 'BEGIN{FS=\"\t\";OFS=\"\t\"}{if($2 != NA) print $1,$2}' > annotation2")


with open(samfile) as file:
    line=file.readlines()
    for i in line:
        if i.startswith('@'):
            continue
        name=i.split('\t')[2]
        if name.startswith('*'):
            continue
        if name not in countdict:
            countdict[name]=1
        elif name in countdict:
            countdict[name]=int(countdict[name])+1




my_dict={}
with open("annotation2") as file:
    k=file.readlines()
    for i in k:
        first=i.split('\t')[0].strip()
        second=i.split('\t')[1].strip()
        if (not second) or (not first):
            continue
        if (first not in my_dict) and (first not in  'read_id'):
            my_dict[first]=second
with open('my_annotation','w') as file:
    for i,l in my_dict.items():
        if str(l)=='NA':
            continue
        file.writelines([str(i),"\t",str(l),'\n'])
my_dict2={}
my_dict3={}

os.system("rm annotation2")
with open("my_annotation") as file:
    read3=file.readlines()
    for i in read3:
        read_name=i.split("\t")[0]
        function_name=i.split("\t")[1]
        my_dict2[read_name]=function_name

for i,l in countdict.items():
    if i  in my_dict2:
        name=my_dict2[i]
    else:
        name='Not defined'
    if (i in my_dict2) and (my_dict2[i] not in my_dict3):
        my_dict3[name]=l
    elif (i in my_dict2) and (my_dict2[i] in my_dict3):
        my_dict3[name]=int(my_dict3[name])+int(l)


with open("count_file",'w') as file:
    for i,l in my_dict3.items():
        file.writelines([str(i),'\t',str(l),'\n'])

os.system("rm my_annotation")


print('count_file 을 확인하세요')

