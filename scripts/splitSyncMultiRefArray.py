#!/usr/bin/env python

import os
import subprocess
import argparse
import sys
import glob
import os.path
from os import path

"""
This script is called as a single sample submission or Slurm array job, and takes in
an integer for the number of reference targets, a comma separated list of the reference 
fasta files, path to R1 reads, path to R2 reads, the fasta files containing the forward 
primers to be trimmed, the fasta file containing the reverse primers to be trimmed, 
and the output directory. 

Synchronized fastq paired-end read files are output into the specified directory.

*************************************************************************************
Forward and reverse reads must be stored in separate directories.
*************************************************************************************

command: ./splitSyncMultiRefArray.py -numTargets <numTargs> -refSeqs <ref_seqs> -r1 <read1> -r2 <read2> -fPrimers <for> -rPrimers <rev> -o <out_dir>
"""

#Functions--------------------------------------------------------------------------
def checkVersion():
	if sys.version_info[0] < 3:
		print("\nType: module load python\n")
		raise Exception("Must be using Python 3")

def getRefs(numRefs, refs):
	i = 0
	names = []
	refList = refs.split(',')
	for i in range(len(refList)):
		namesExt = os.path.basename(refList[i])
		names.append(namesExt.split('.')[0])
	return(refList, names)

def makeOutDirs(topOut, refIDs):
	out = topOut
	refNames = refIDs
	if not os.path.exists(os.path.join(out, "fastq")):
		os.makedirs(os.path.join(out, "fastq"))
	for i in range(len(refNames)):
		if not os.path.exists(os.path.join(topOut, "fastq", refNames[i])):
			os.makedirs(os.path.join(out, "fastq", refNames[i]))
	if not os.path.exists(os.path.join(out, "cut")):
		os.makedirs(os.path.join(out, "cut"))
		os.makedirs(os.path.join(out, "cut", "1"))
		os.makedirs(os.path.join(out, "cut", "2"))
	if not os.path.exists(os.path.join(out, "trim")):
		os.makedirs(os.path.join(out, "trim", "1"))
		os.makedirs(os.path.join(out, "trim", "2"))
		os.makedirs(os.path.join(out, "trim", "singleton"))
		os.makedirs(os.path.join(out, "trim", "Log"))
		os.makedirs(os.path.join(out, "trim", "Summary"))
	if not os.path.exists(os.path.join(out, "Results")):
		os.makedirs(os.path.join(out, "Results"))

def trimReads(read1, read2, out_dir, primF, primR):
	toTrim1 = read1
	toTrim2 = read2
	out = out_dir
	F = primF
	R = primR
	trimmomatic = "/gpfs/fs1/data/taylorlab/software/Trimmomatic-0.38/trimmomatic-0.38.jar"
	sample1 = os.path.basename(toTrim1).split('_')[0]
	sample2 = os.path.basename(toTrim2).split('_')[0]
	assert sample1 == sample2
	
	os.system("cutadapt -g file:{} -G file:{} -o {}/cut/1/{}_1.fastq.gz ".format(F, R, out, sample1) + \
		"-p {}/cut/2/{}_2.fastq.gz {} {}".format(out, sample2, toTrim1, toTrim2))

	os.system("java -jar {} PE -phred33 -summary {}/trim/Summary/{}.summary ".format(trimmomatic, out, sample1) + \
		"{}/cut/1/{}_1.fastq.gz {}/cut/2/{}_2.fastq.gz ".format(out, sample1, out, sample2) + \
		"{}/trim/1/{}_1.fastq.gz {}/trim/singleton/{}_1_unpaired.fq.gz ".format(out, sample1, out, sample1) + \
		"{}/trim/2/{}_2.fastq.gz {}/trim/singleton/{}_2_unpaired.fq.gz ".format(out, sample2, out, sample2) + \
		"LEADING:10 TRAILING:10 SLIDINGWINDOW:4:15 MINLEN:80")

	trim1 = "{}/trim/1/{}_1.fastq.gz".format(out, sample1)
	trim2 = "{}/trim/2/{}_2.fastq.gz".format(out, sample2)

	return(trim1, trim2)

def splitReads(refs, refIDs, trim1, trim2, maxIndel, out):
	i = 0
	sample = os.path.basename(trim1).split('_')[0]
	sep = ','
	refList = refs
	print(refList)
	
	os.system("/data/taylorlab/software/bbmap/bbsplit.sh -Xmx8000m in={} in2={} ref={} ".format(trim1, trim2, refList) + \
			"maxindel={} basename={}_%_#.fastq ".format(maxIndel,  sample) + \
			">& {}/Results/{}.txt".format(out, sample))
	for i in range(len(refIDs)):
		outfile1 = glob.glob("*{}_{}_1*".format(sample, refIDs[i]))[0]
		outfile2 = glob.glob("*{}_{}_2*".format(sample, refIDs[i]))[0]

		os.system("mv {} {}/fastq/{}".format(outfile1, out, refIDs[i]))
		os.system("mv {} {}/fastq/{}".format(outfile2, out, refIDs[i]))
		os.system("gzip {}/fastq/{}/*.fastq".format(out, refIDs[i]))
		if not os.path.exists(os.path.join(out, "fastq", refIDs[i], "1")):
			os.makedirs(os.path.join(out, "fastq", refIDs[i], "1"))
		if not os.path.exists(os.path.join(out, "fastq", refIDs[i], "2")):
			os.makedirs(os.path.join(out, "fastq", refIDs[i], "2"))
		file1 = glob.glob(os.path.join("{}/fastq/{}/".format(out, refIDs[i]), "*{}_{}_1.fastq.gz".format(sample, refIDs[i])))[0]
		file2 = glob.glob(os.path.join("{}/fastq/{}/".format(out, refIDs[i]), "*{}_{}_2.fastq.gz".format(sample, refIDs[i])))[0]
		os.system("mv {} {}/fastq/{}/1".format(file1, out, refIDs[i]))
		os.system("mv {} {}/fastq/{}/2".format(file2, out, refIDs[i]))
		path = "{}/fastq/{}".format(out, refIDs[i])
		r1 = glob.glob(os.path.join(path, "1", "*{}*".format(sample)))[0]
		r2 = glob.glob(os.path.join(path, "2", "*{}*".format(sample)))[0]

		syncReads("{}/1".format(path), "{}/2".format(path), r1, r2)

def syncReads(read1Dir, read2Dir, read1, read2):
	sample1 = os.path.basename(read1).split('.')[0]
	sample2 = os.path.basename(read2).split('.')[0]

	os.system("repair.sh in={} in2={} out={}/{}.paired.fastq.gz out2={}/{}.paired.fastq.gz repair".format(read1, read2, read1Dir, sample1, read2Dir, sample2))
	if path.exists('singletons.fq'):
		os.system("rm singletons.fq")
	os.system("rm {} {}".format(read1, read2))
	os.system("mv {}/{}.paired.fastq.gz {}".format(read1Dir, sample1, read1))
	os.system("mv {}/{}.paired.fastq.gz {}".format(read2Dir, sample2, read2))

#Main-------------------------------------------------------------------------------
if __name__ == "__main__":

	description = "Splits and synchronizes paired-end amplicon sequence data by target" \

	parser = argparse.ArgumentParser(prog="Reference splitter", description=description)
	# user-defined parameters
	parser.add_argument("-numTargets", "--numTargs",
		type=int,
		default=None,
		required=True,
		help="Number of amplicon targets")

	parser.add_argument("-refSeqs", "--ref_seqs",
		type=str,
		default=None,
		required=True,
		help="Comma separated list of paths to reference fasta files")

	parser.add_argument("-r1", "--read1",
		type=str,
		default=None,
		required=True,
		help="Path to forward reads")

	parser.add_argument("-r2", "--read2",
		type=str,
		default=None,
		required=True,
		help="Path to reverse reads")

	parser.add_argument("-fPrimers", "--forw",
		type=str,
		default=None,
		required=True,
		help="Path to forward primers fasta file")

	parser.add_argument("-rPrimers", "--rev",
		type=str,
		default=None,
		required=True,
		help="Path to reverse primers fasta file")

	parser.add_argument("-maxIndel", "--indel",
		type=int,
		default=None,
		required=True,
		help="Maximum indel (in nt) for read mapping")

	parser.add_argument("-o", "--out_dir",
		type=str,
		default=None,
		required=True,
		help="Directory to save output")


	args = parser.parse_args()

	numTargets = args.numTargs
	refSeqs = args.ref_seqs
	read1 = args.read1
	read2 = args.read2
	primF = args.forw
	primR = args.rev
	maxIndel = args.indel
	out_dir = args.out_dir

	# create the output directory if needed
	if not os.path.exists(out_dir):
		os.makedirs(out_dir)

	checkVersion()
	refs, refIDs = getRefs(numTargets, refSeqs)
	makeOutDirs(out_dir, refIDs)
	(trim1, trim2) = trimReads(read1, read2, out_dir, primF, primR)
	splitReads(refSeqs, refIDs, trim1, trim2, maxIndel, out_dir)

 
