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



with open('contig_above_1500','w') as file:
	for i,l in my_dict.items():
		if len(l) >= 1500:
			file.writelines([i.strip(),'\n',textwrap.fill(l.strip(),width=80),'\n'])
