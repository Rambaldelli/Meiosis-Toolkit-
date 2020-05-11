import glob
import os
import  sys
import re



if __name__ == "__main__":
	main_folder= (sys.argv[1])  # require blast format 3
	os.chdir(main_folder)
	path_target = '*.mafft.n.aln'
	folder = glob.glob(path_target)



for file in folder:
	file_name=file.split('/')[-1]
	file_name=file_name.split('_')[:-1]
	file_name='_'.join(file_name)
	with open(file_name+'.prt', 'w' ) as out:
		with open(file, 'r' ) as inp:
			lines=inp.readlines()
			flag=2
			lenght=0
			for line in lines:
				if flag==1 and line.startswith('>'):
					out.write('DNA, prt1 = 1-'+str(lenght)+'\\3\n')   
					out.write('DNA, prt2 = 2-'+str(lenght)+'\\3\n')  
					out.write('DNA, prt3 = 3-'+str(lenght)+'\\3\n')        
					flag=0

				elif flag==2 and line.startswith('>'):
					flag=1

				elif flag==1 and len(line.rstrip())==0:
					print('error')

				elif flag==1:
					lenght=lenght+len(line.rstrip())
