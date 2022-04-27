
import os
import sys
import textwrap
fasta=sys.argv[1]

with open('human_nr','w') as file, open(fasta) as file2:
	for i in file2:
		if (i.startswith('>')) and ('Homo' in i) and ('sapiens' in i):
			id_1=i.strip()
			file.writelines([i.strip(),'\n'])
		if (i.startswith('>')):
                	id_1=i.strip()
		if (not i.startswith('>')) and ('Homo' in id_1) and ('sapiens' in id_1):
			file.writelines([i.strip(),'\n'])
		if (not i.startswith('>')) and ('Homo' not  in id_1):
			continue

