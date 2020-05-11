while getopts  ":e:w:c:t:h" o; do

  case "${o}" in

  e) e=${OPTARG}
            ;;
	w) w=${OPTARG}
            ;;
	c) c=${OPTARG}
            ;;
  t) t=${OPTARG}
            ;;
	h) echo "
      -e : e value
      -w : word lenght Blast
      -c : coverage treshold
      -t : threads
			"
               exit
          ;;
       \?) echo "WARNING! -$OPTARG isn't a valid option"
           exit
          ;;
       :) echo "WARNING! missing -$OPTARG value"
          exit
          ;;
       esac
 done



python3 Blast_Luncher_split.py meiosis_toolkit_references/ protein/ $e $w

python3 Blast_proteins_retriver_coverage.py Blast_results/ protein/ $c
python3 Blast_CDS_retriver_coverage.py Blast_results/ CDS/ $c

mkdir ./Toolkit_Prot/
mkdir ./Toolkit_CDS/

cp Blast_results/*/*_prot.fa Toolkit_Prot/
cp Blast_results/*/*_CDS.fa Toolkit_CDS/

bash align_protein_to_CDS.sh -p Toolkit_Prot/ -n Toolkit_CDS/ -t $t

python3 Partition_creator_alignment.py alignment/

python3 IqTree_Luncher.py alignment/