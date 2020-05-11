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
			file_name=file.split('_')[:-1]
			file_name='_'.join(file_name)
			os.system('iqtree -s '+file_name+'_.mafft.n.aln -spp '+file_name+'.prt -m MFP+MERGE -bb 1000 -bnni -alrt 1000')

