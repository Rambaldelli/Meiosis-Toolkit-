import glob
import os
import  sys
import re



if __name__ == "__main__":
	main_folder= (sys.argv[1])  # require blast format 3

	path_target = main_folder + '/*.mafft.n.aln'
	folder = glob.glob(path_target)


with open('partition.prt', 'w' ) as out:
	for file in folder:
		with open(file, 'r' ) as inp:
			lines=inp.readlines()
			flag=0
			for line in lines:
				if flag==1 and line.startswith('>'):
					out.write(name+', prt1 = 0-'+str(lenght)+'\\3\n')   
					out.write(name+', prt2 = 1-'+str(lenght)+'\\3\n')  
					out.write(name+', prt3 = 3-'+str(lenght)+'\\3\n')        
					name=line.rstrip()
					lenght=0

				elif flag==0 and line.startswith('>'):
					name=line.rstrip()
					flag=1
					lenght=0

				elif flag==1 and len(line.rstrip())==0:
					print('error')

				elif flag==1:
					lenght=lenght+len(line.rstrip())
