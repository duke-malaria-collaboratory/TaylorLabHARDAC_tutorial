# Install R libraries on HARDAC

### You'll likely need to install your own R packages on the cluster at some point
- To do so, follow these steps
	
## Step 1:
#### Create a directory for the packages in your /data/taylorlab/usr directory
	mkdir -p /data/taylorlab/${USER}/r_libs
#### Load R module
	module load R/3.5.3-gcb02 # Version 3.5 required for Bioconductor
#### If you need a specific version of R for the package(s) you'll use, search for the available versions by typing:
	module spider R	
- Once you identify the version your package requires, replace the version above with the one you've found
	
## Step 2:
#### Set the path for the location from Step 1 of your R packages for "R_LIBS_USER" by typing:
	export R_LIBS_USER=/data/taylorlab/${USER}/r_libs:$R_LIBS_USER	

## Step 3:
#### Start an R session:
	R
#### Install a package (e.g. Biobase) from Bioconductor
	if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")
	BiocManager::install("Biobase")

## Step 4:
#### Check that the package has been installed:
	q()
	ls /data/taylorlab/${USER}/r_libs
