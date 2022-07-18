import sys
import gzip
import time
from datetime import timedelta
samfile=sys.argv[1]
fastqfile=sys.argv[2]
start=time.process_time()
with gzip.open(fastqfile) as file:
        zxc=file.readlines()
end = time.process_time()
print("Iter 완성: ", timedelta(seconds=end-start))




with open(samfile) as file, open('NT_1087596_T','w') as file2:
        n=0
        for i in file:
                n+=1
                try:
                        if 'NT_1087596_T' in i:
                                file2.writelines([zxc[1+4*(n-1)].decode('utf-8').strip(),'\n'])
                                print(n)
                except:
                        pass

print('complete')
