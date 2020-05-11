import glob
import os
import  sys



if __name__ == "__main__":
    reference,folder,evalue,word=(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])  #cv,type,Gamma,C,datat, datap

    path_target=folder +'*.fa'
    files = glob.glob(path_target)

    path_ref=reference +'*.fasta'
    refs = glob.glob(path_ref)

    exe_path=os.path.realpath(__file__)
    path=str(os.path.split(exe_path)[0])

    os.system("mkdir Blast_results")
    os.chdir('Blast_results')

    for ref in refs:
        name_ref_comp = ref.split('/')[-1]
        name_folder=name_ref_comp.split('.')[0]+ '.' + name_ref_comp.split('.')[1]
        os.system('mkdir "'+name_folder+'"')
    
    for file in files:
        name_specie_comp = file.split('/')[-1]
        name_specie=name_specie_comp.split('.')[0]
        os.system('makeblastdb -in "' + path +  '/' +file + '" -dbtype prot -out "' + name_specie_comp + '.db"')
        for ref in refs:
            name_ref_comp = ref.split('/')[-1]
            name_folder = name_ref_comp.split('.')[0]+ '.' + name_ref_comp.split('.')[1]
            #os.chdir(name_folder) 
            os.system('blastp -db "'+name_specie_comp+'.db" -query "'+path + '/' +ref+'" -out "'+name_specie + '_' + name_ref_comp+'" -evalue '+evalue+' -word_size '+word+' -outfmt 10')
            os.system('mv "'+name_specie + '_' + name_ref_comp + '"  "' + name_folder + '"')
        os.system('rm ' + name_specie_comp + '.db.*')
