#!/usr/bin/env python
# -*- coding=utf-8 -*-

import sys,os,re
from os.path import basename

hisat2build="hisat2-build"
hisat2="hisat2"
parameter=" -p 8 --dta "
genome="genome.fa"
gtf="genome.gtf"
prefix="genome_prefix"
samtools="samtools"
stringtie="stringtie"
threads=20

dir=sys.argv[1] ###fastq dir


##读取左右两端序列
def readfastq(dir):
	filelist1=[]
	filelist2=[]

	if os.path.exists(dir):
		for root, dirs, files in os.walk(dir):
			for name in files:
				if name.endswith('_1.clean.fq.gz'): # please check your file pattern

					filelist1.append(os.path.join(root,name))					
					filelist2.append(os.path.join(root,name.replace('_1.clean.fq.gz','_2.clean.fq.gz')))


	return [filelist1,filelist2]



[leftfastq,rightfastq]=readfastq(dir)

i=0

while i < len(leftfastq):
	name=leftfastq[i].replace('_1.clean.fq.gz','')
	print(hisat2 +' -x ' + prefix+parameter + "-1 " + leftfastq[i]+" -2 " + rightfastq[i]+" -S " + basename(name)+ '.sam && '\
+samtools+' sort -@ '+str(threads)+' -O bam -T ' + basename(name)+ '.bam.tmp ' + basename(name)+ '.sam -o '+ basename(name)+ '.bam && ' + stringtie + ' -p '+ str(threads) + \
' -G '+gtf+' -o ' + basename(name)+ '.gtf -l ' + basename(name) + ' ' + basename(name)+ '.bam')
	i+=1
