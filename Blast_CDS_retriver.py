import glob
import os
import  sys
import re

def add_element(dict, key, value):
    if key not in dict:
        dict[key] = ''
    dict[key] = dict[key] + value.strip()

if __name__ == "__main__":
    main_folder,protein_folder= (sys.argv[1],sys.argv[2])  # require blast format 3

    path_target = main_folder + '*'
    folders = glob.glob(path_target)

    exe_path=os.path.realpath(__file__)
    path=str(os.path.split(exe_path)[0])

    for folder in folders:
        os.chdir(folder)
        blasts_name = '*.fasta'
        blasts = glob.glob(blasts_name)
        folder_name=folder.split('/')[1] + '_CDS.fa'
        with open(folder_name, 'w' ) as out:
            for blast in blasts:
                specie_name=blast.split('_')[0]
                with open(blast,'r')as infas:
                    infa=infas.readlines()
                    arr=[]
                    for line in infa:
                        if len(line.strip())!=0:
                            arr.append(line.split('\t')[1])
                    db_path=path+'/'+protein_folder+specie_name+'_CDS.fa'
                    with open(db_path,'r') as db:
                        lines=db.readlines()
                        flag=0
                        for line in lines:
                            if line.startswith('>'):
                                entry=line.split('|')[1].rstrip()
                              #  print(entry)
                               # print(arr)

                            if line.startswith('>') and entry not in arr:   #protein: line.split(' ')[0]
                                flag=0
                            elif flag==1 and line.startswith('>') and entry in arr:
                                out.write(line.strip()+'\n')
                            elif flag==1:
                                out.write(line.strip() + '\n')
                            elif line.startswith('>') and entry in arr:
                                out.write(line.strip()+'\n')
                                flag=1

        os.chdir(path)



