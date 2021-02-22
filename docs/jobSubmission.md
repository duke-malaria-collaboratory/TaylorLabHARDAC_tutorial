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
	- BBMap - very powerful and useful toolkit for NGS data

	- Let's create a directory to hold software
	

#
### Check the status of your job