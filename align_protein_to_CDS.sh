while getopts  ":p:n:t:h" o; do

    case "${o}" in

    p) p=${OPTARG}
            ;;
	n) n=${OPTARG}
            ;;
	t) t=${OPTARG}
            ;;
	h) echo "
			This script is used to align nucleotide MSA based on the relative protein MSA by a combination of transeq & mafft & pal2nal (conda insatallation tested).
			List of non-optional arguments:
                        -i	input folder, containing interleaved or onliner .fa / .fas /.fasta files (both interleaved and oneliner entires are allowed in the same file).
			-f	output folder, just specify a name to have it inside the current folder.
			-t	number of threads.
                        -h	help page.
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


################################################################################################################
mkdir ./alignment
cp $p/*.fa* alignment
cp $n/*.fa* alignment
cd alignment
for file in *.fa*; do mv "$file" "${file/>/}"; done
#sed -i 's/>.*|/>/g' *.fa*
#sed -i 's/>EFX/>/g' *.fa*
for j in *CDS.fa*; do export n=$(echo $j | awk -v OFS="_" -F "_" '{$(NF--)=""; print}');
  echo $n
  mafft ${n}prot.fa > $n.mafft.p.aln;

  pal2nal.pl $n.mafft.p.aln ${n}CDS.fa -output fasta >> $n.mafft.n.aln;

done;