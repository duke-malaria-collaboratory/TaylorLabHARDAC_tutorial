# Guide to creating new conda envs

### Navigate to the scripts directory from this repository

Type the following:

	cd /data/taylorlab/${USER}/TaylorLabHARDAC_tutorial/scripts
	./createCondaEnv.sh	
- New environments will be saved in /data/taylorlab/${USER}/conda/envs

### Load the Anaconda module
	module load Anaconda/4.3.0-fasrc01

### Create conda environment that has the pandas library installed
	conda create -n main -c conda-forge pandas
	conda activate 