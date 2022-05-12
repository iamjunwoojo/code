delim=''
import os
import time
import concurrent.futures
import re

n=0
my_dict={}
def delim_zero(line):
	try:
		name=re.match('\S*\s',line).group().lstrip('>').strip()
		function=re.search('.*\\[',line).group().lstrip(f'>{name}').strip('[ ')
		species=re.search('\\[\D+.*',line).group().strip('[ ]')
		if species.count(']'):
			species=f'[{species}'
		my_dict[name]=[function,species]
	except:
		name=re.match('\S*\s',line).group().strip(' >')
		function=line.strip('>').lstrip(name)
		species='not defined'
		my_dict[name]=[function,species]







with open('changed_NR_annotation') as file:
	for i in file:
		i=i.strip()
		if i.startswith('>') and i.count(delim)==0:
			delim_zero(i)
		if i.startswith('>') and i.count(delim)>=1:
			for k in i.split(delim):
				delim_zero(k.strip())


	
with open('test_blast') as file, open('annotation','w') as file2,open('error_not_annotated','w') as file3:
	for i in  file:
		try:
			id=i.split('\t')[1].strip()
			function=my_dict[id][0].strip()
			species=my_dict[id][1].strip()
			file2.writelines([i.strip(),'\t',species,'\t',function,'\n'])
		except:
			file3.writelines([i.strip(),'\n'])
