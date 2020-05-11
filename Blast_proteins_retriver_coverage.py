import glob
import os
import  sys
import re

def add_element(dict, key, value):
    if key not in dict:
        dict[key] = ''
    dict[key] = dict[key] + value.strip()

if __name__ == "__main__":
    main_folder,protein_folder,coverage= (sys.argv[1],sys.argv[2],sys.argv[3])  # require blast format 3

    path_target = main_folder + '*'
    folders = glob.glob(path_target)

    exe_path=os.path.realpath(__file__)
    path=str(os.path.split(exe_path)[0])

    for folder in folders:
        os.chdir(folder)
        blasts_name = '*.fasta'
        blasts = glob.glob(blasts_name)
        folder_name = folder.split('/')[1] + '_prot.fa'
        with open(folder_name, 'w' ) as out:
            for blast in blasts:
                specie_name=blast.split('_')[0]
                with open(blast,'r')as infas:
                    infa=infas.readlines()
                    arr=[]
                    for line in infa:
                        if len(line.strip())!=0 and float(line.split(',')[2])>=float(coverage) and '>'+line.split(',')[1]+'|'+line.split(',')[2]+'|'+line.split(',')[10] not in arr:
                            arr.append('>'+line.split(',')[1]+'|'+line.split(',')[2]+'|'+line.split(',')[10])
                    db_path=path+'/'+protein_folder+specie_name+'_proteins.fa'
                    with open(db_path,'r') as db:
                        lines=db.readlines()
                        flag=0
                        for line in lines:
                            if line.startswith('>'):
                                name = line.split(' ')[0].rstrip()
                                for hit in arr:
                                    if name == hit.split('|')[0].rstrip():
                                        flag=1 
                                        p_name=name.replace(">", "")
                                        p_name='>'+specie_name+'|'+p_name+'|'+hit.split('|')[1]+'|'+hit.split('|')[2]+'\n'
                                        out.write(p_name)
                                        break
                                    else:
                                        flag=0
                            elif flag==1:
                                out.write(line.strip() + '\n')
        os.chdir(path)



