# expressionAnalysis
1. trim the raw data with fastp
 
python 01.fastp.run.py DIR(raw  data) >01.fastp.run.sh

sh 01.fastp.run.sh

2. run hisat2 
 
python 02.hisat.run.py DIR(clean data) >02.hisat.run.sh

sh 02.hisat.run.sh

mkdir hisatResult
mv *.bam *.gtf hisatResult

3. merge the gtf from hisat2

ls hisatResult/*.gtf >gtfMerge.list

stringtie --merge -p NUM -G reference.gtf -o stringtie_merged.gtf gtfMerge.list

4. run stringtie 

python 04.stringtie.run.py hisatResult >04.stringtie.run.sh

sh 04.stringtie.run.sh


5. run prepDE.py

ls ballgown/*/*.gtf >gtf.list


awk -F '/'  '{print $2"\t"$0}' gtf.list >gtf.list1


mv gtf.list1 gtf.list
 
python prepDE.py -i gtf.list -l readlength
