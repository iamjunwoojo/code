less blast_out_tax|grep -v ";"|grep -Ev "Eukaryota|N/A"|cut -f 1,4,7 >blast_tax_metadata2
{}=my_dict
with open('blast_tax_metadata2') as file:
  for i in file2:
    id=i.split()[0].strip()
    species=i.split()[1].strip()
    phylumn=i.split()[2].strip()
    if id in my_dict:
      continue
    my_dict[id]=[species,phylumn]
with open('blast_tax_metadata3','w') as file:
  for i,l in my_dict.items():
    file.writelines([i,'\t',l[0],'\t',l[1],'\n')
