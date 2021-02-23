#!/bin/bash
#
##SBATCH -p common               	# Partition to submit to (comma separated)
#SBATCH -J callVariants                 # Job name
#SBATCH -n 1                     	# Number of cores
#SBATCH -N 1                     	# Ensure that all cores are on one machine
#SBATCH -t 2-00:00              	# Runtime in D-HH:MM (or use minutes)
#SBATCH --mem 1000               	# Memory in MB
#SBATCH -o log/_varCall_%A_%a.out     	# File for STDOUT (with jobid = %j) 
#SBATCH -e errorLog/varCall_%A_%a.err 	# File for STDERR (with jobid = %j)    
#SBATCH --array=1-18%6			# Array tasks

module load bcftools/1.10.2-fasrc01
module load samtools/1.10-gcb01
module load bwa/0.7.12-gcb01
module load python/3.7.4-gcb01

echo "$SLURM_ARRAY_TASK_ID"
pair1=$(ls /data/taylorlab/${USER}/HARDAC_tutorial/data/reads/amplicon/1/*.fastq.gz |sort| sed -n ${SLURM_ARRAY_TASK_ID}p)
pair2=$(ls /data/taylorlab/${USER}/HARDAC_tutorial/data/reads/amplicon/2/*.fastq.gz |sort| sed -n ${SLURM_ARRAY_TASK_ID}p)

refdir="/data/taylorlab/${USER}/HARDAC_tutorial/data/refs"
out="/data/taylorlab/${USER}/variantCallResults"
bq=20

mkdir -p $out

.././variantArray.py \
-ref $refdir/pfcrt \
-p1 $pair1 \
-p2 $pair2 \
-bq $bq \
-o $out/pfcrt 

.././variantArray.py \
-ref $refdir/dhps \
-p1 $pair1 \
-p2 $pair2 \
-bq $bq \
-o $out/dhps

.././variantArray.py \
-ref $refdir/dhfr \
-p1 $pair1 \
-p2 $pair2 \
-bq $bq \
-o $out/dhfr

.././variantArray.py \
-ref $refdir/K13 \
-p1 $pair1 \
-p2 $pair2 \
-bq $bq \
-o $out/K13

.././variantArray.py \
-ref $refdir/pfmdr1 \
-p1 $pair1 \
-p2 $pair2 \
-bq $bq \
-o $out/pfmdr1
