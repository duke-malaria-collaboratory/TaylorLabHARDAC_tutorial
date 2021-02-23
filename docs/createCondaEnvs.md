# Guide to creating new conda envs

### Navigate to the scripts directory from this repository

Type the following:

	cd /data/taylorlab/${USER}/TaylorLabHARDAC_tutorial/scripts
	./createCondaEnv.sh	

- New environments will be saved in /data/taylorlab/${USER}/conda/envs

### Load the Anaconda module
	module load Anaconda/4.3.0-fasrc01

### Create conda environment with Python version 3.6.1 that has the pandas library installed

	conda create -n new_env -c conda-forge python==3.6.1 pandas
	source activate /data/taylorlab/${USER}/conda/envs/main
	
### Install another package (e.g. Seaborn) into this environment while it's activated
	