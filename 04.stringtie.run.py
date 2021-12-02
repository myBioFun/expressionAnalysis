#!/usr/bin/env python
# -*- coding=utf-8 -*-

import sys,os
from os.path import basename

stringtie="stringtie -e -B "
threads=20
stringtie_merged_gtf="stringtie_merged.gtf"  ## changed according to conditions
dir=sys.argv[1]

def readbam(dir):
	bamlist=[]	
	#pattern=re.compile(r'_.*1.clean.*.gz')
	if os.path.exists(dir):
		for root, dirs, files in os.walk(dir):
			for name in files:
				if name.endswith('.bam'):

					bamlist.append(os.path.join(root,name))					

	return bamlist


bamlist=readbam(dir)
if os.path.exists("ballgown"):
	pass
else:
	os.mkdir("ballgown")
for ll in bamlist:
	name=ll.replace('.bam','')
	name=basename(name)
	print(stringtie+"-p "+str(threads)+" -G "+stringtie_merged_gtf+" -o ballgown/"+name+'/'+name+'.gtf '+ll) ## create run command
	print(name + '\tballgown/'+name+'/'+name+'.gtf ')  ## create gtf.list

