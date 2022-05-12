import sys
input_fasta=sys.argv[1]
input_trans=sys.argv[2]
n=0
my_dict={}
my_dict2={}


with open(input_fasta) as file:
	kk=file.readlines()
length=0
n=0
jj=1

for i in kk:
	if (i.startswith('>')):
		n+=1
		id_1=i.strip()
		my_dict[id_1]=''
	if (not i.startswith('>')) and  (jj == n):
		my_dict[id_1]+=i.strip()
	if jj != n:
       	        jj=n

with open(input_trans) as file:
        zz=file.readlines()
length=0
n=0
jj=1

for i in zz:
	if (i.startswith('>')):
		n+=1
		id_1=i.strip()
		my_dict2[id_1]=''
	if (not i.startswith('>')) and  (jj == n):
		my_dict2[id_1]+=i.strip()
	if jj != n:
		jj=n



my_dict=sorted(my_dict.items(),key = lambda item : len(item[1]))


with open('renamed_contg_translated','w') as file2,open('renamed_contig_fasta','w') as file3:
	n=0
	for i,l in my_dict:
		if len(l) <22:
			continue
		n+=1
		file3.writelines([f'>{n}','\n',l.strip(),'\n'])
		file2.writelines([f'>{n}','\n',my_dict2[i.strip()].strip(),'\n'])
