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



with open('renamed_contig','w') as file:
        for i,l in my_dict.items():
            if len(l) >= 0:
                name=i.split()[0].lstrip('>')
                i=f'>{fasta}_{name}'
                file.writelines([i.strip(),'\n',l,'\n'])
~                                                                                                                                                                                                          
~                                                                                                                                                                                                          
~               
