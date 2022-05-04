my_list=[]
my_dict={}
final_dict={}
with open('sample') as file:
        for i in file:
                my_list.append(i.strip())
with open('tcga_20220504_1.tsv') as file:
        for i in file:
                id=i.split('\t')[1]
                center=i.split('\t')[5]
                my_dict[id]=center


def my_function(in_put):
        for k,l in my_dict.items():
                if in_put.strip() in k:
                        final_dict[in_put.strip()]=l.strip()

for i in my_list:
        my_function(i)



print(len(final_dict))
with open('result','w') as file:
        for i,l in final_dict.items():
                file.writelines([i,'\t',l,'\n'])

~                                                                                                                                                                                                          
~                                                                                                                                                                                                          
~                                       
