# Submitting a job to HARDAC with Slurm


### Change into your user directory on /data drive
	cd /data/taylorlab/${USER}

### Clone this repository into your user directory
    git clone https://github.com/jws48/TaylorLabHARDAC_tutorial.git
    
### Change directory into the repository directory
	cd TaylorLabHARDAC_tutorial
	
### Take a look around
#### List the contents
	ls .
- List the contents of the scripts and slurm job directories
	ls scripts/
	
	ls scripts/slurm

### Print to the screen the program that splits and synchronizes paired-end reads from pooled amplicon libraries
	cat splitSyncMultiRefArray.py

### Before we can run it, we need to install some software
#### BBMap - very powerful and useful toolkit for NGS data
	mkdir /data/taylorlab/${USER}/software	
	cd /data/taylorlab/${USER}/software
	wget https://sourceforge.net/projects/bbmap/files/BBMap_38.90.tar.gz
	tar -xf BBMap_38.90.tar.gz
	rm BBMap_38.90.tar.gz
	echo "export PATH="/data/taylorlab/${USER}/software/bbmap:$PATH"" >> ~/.bashrc
	source ~/.bashrc

### Move into the directory that holds the slurm scripts
	cd /data//taylorlab/${USER}/scripts/slurm

### Submit a job to the cluster that will split our raw fastq reads by amplicon target
	sbatch pySplitSlurm.sh 

### Check the status of your job
	squeue -u ${USER}
- There will likely only be the interactive session displayed, since this practice job we submitted should be complete before you have time to type this out

### Using the reads we've just split into their respective targets, call variants for each sample
	sbatch pyVarCallSlurm.sh
- Note: This job must be called *after* the pySplitSlurm.sh script, since this one uses the splitReadsResults fastq files as input, which won't exist until that script is run

