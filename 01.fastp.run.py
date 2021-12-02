#! /usr/bin/env python
# -*- coding=utf-8 -*-

import os,sys,re

if(len(sys.argv) < 1):
    print("usage: python %s rawReadsDir\n"%sys.argv[0])
    exit(1)


fastp="fastp -f 10 -F 10 --detect_adapter_for_pe -x -h"
def get_files_from_dir(dir):
	for root,dirs,files in os.walk(dir):
		for file in files:
			filename=os.path.join(root,file)
			pattern=r".*_1.fastq.gz$"
			if re.search(pattern,filename):
				filename2=re.sub("_1","_2",filename)
				filename3=re.sub("_1.fastq.gz","_1.clean.fq.gz",filename)
				filename4=re.sub("_2.fastq.gz","_2.clean.fq.gz",filename2)
				filename5=re.sub("_1.*","",filename)
				print("%s %s.html -c -q 15 -u 40 -g -n 5 -i %s -I %s -o %s -O %s"%(fastp,filename5,filename,filename2,filename3,filename4))

dir=sys.argv[1]
get_files_from_dir(dir)
