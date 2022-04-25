import os
import sys
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
		my_dict[id_1]=0
	if (not i.startswith('>')) and  (jj == n):
		my_dict[id_1]=int(my_dict[id_1])+len(i.strip())
	if jj != n:
                length=0
                jj=n
for i,l in my_dict.items():
	print(i,' : ',l)
