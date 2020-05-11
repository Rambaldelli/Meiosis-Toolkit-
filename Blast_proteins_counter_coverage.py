import glob
import os
import  sys
import re


if __name__ == "__main__":
    main_folder,coverage= (sys.argv[1],sys.argv[2])  # require blast format 3

    path_target = main_folder + '*'
    folders = glob.glob(path_target)

    exe_path=os.path.realpath(__file__)
    path=str(os.path.split(exe_path)[0])
    stat={}
    out_name='test_coverage_'+str(coverage)+'.txt'
    with open(out_name, 'w' ) as out:
        for folder in folders:
            os.chdir(folder)
            blasts_name = '*.fasta'
            blasts = glob.glob(blasts_name)
            stat[folder.split('/')[1]]=[]
            for blast in blasts:
                specie_name=blast.split('_')[0]
                with open(blast,'r')as infas:
                    infa=infas.readlines()
                    arr=[]
                    tot=0
                    for line in infa:
                        if len(line.strip())!=0 and float(line.split(',')[2])>=float(coverage) and '>'+line.split(',')[1]+'|'+line.split(',')[2]+'|'+line.split(',')[10] not in arr:
                            arr.append('>'+line.split(',')[1]+'|'+line.split(',')[2]+'|'+line.split(',')[10])
                            tot=tot+1
                stat[folder.split('/')[1]].append(tot)

            os.chdir(path)
        out.write(str(list(stat.keys())))
        specie_el=[]
        for i in blasts:
            specie_el.append(i.split('_')[0])
        out.write(str(specie_el))
        for index in stat.keys():
            out.write(str(stat[index])+'\n')




