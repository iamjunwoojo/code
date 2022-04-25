import os
import sys
import textwrap
fasta=sys.argv[1]
with open(fasta) as file:
	kk=file.readlines()
my_dict={}
length=0
n=0
jj=1
for i in kk:
	if (i.startswith('>')):
		n+=1
		id_1=i.strip()
		my_dict[id_1]=""
	if (not i.startswith('>')) and  (jj == n):
		my_dict[id_1]=my_dict[id_1]+i.strip()
	if jj != n:
                jj=n


for i,l in my_dict.items():
    name=str(i.strip('>'))
    print(name)
    with open(name,'w') as file:
        file.writelines(textwrap.fill(l,width=70))

