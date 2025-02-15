cat result_summary2.txt | awk '{ bin = int($1/10)*10; printf "%d-%d\n", bin, bin+9 }' | sort -t- -k1,1n | datamash -g1 count 1
