es=(0.001 0.0000001 0.0000000001 0.000000000000000000001 0.0000000000000000000000000000000000000000000000001)
cs=(10 20 30 40 50 60 70 80 90)


for e in "${es[@]}"
do
  python3 Blast_Luncher_split.py meiosis_toolkit_references/ protein/ $e 3

  mkdir ./Test_e_value_$e


  for c in "${cs[@]}"
  do
    python3 Blast_proteins_counter_coverage.py Blast_results/ $c
    mv test_coverage_$c.txt Test_e_value_$e

  done

done