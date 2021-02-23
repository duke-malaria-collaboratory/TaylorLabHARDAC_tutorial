# Getting acquainted with the command line

### Basic commands to navigate HARDAC and submit jobs


### Open the command line on your computer

- Search Terminal in  Spotlight search on Mac, or type Ctrl-Alt-T on Linux


### Check which directory you're in
	pwd
	
### Change into your home directory
	cd
		
### See what files and/or directories are around
	ls

### Change directories
	cd Documents
	ls
	
### Move back into your home directory
	cd ..
	
### Change into the Desktop directory and see what files are there
	cd ~/Desktop
	ls

### Download this document to your Desktop
	wget https://raw.githubusercontent.com/jws48/TaylorLabHARDAC_tutorial/main/docs/test.txt

### Print document to your Terminal window
	cat test.txt
	
### Try to autocomplete with tab:
	cat tes *tab*
	
- If you hit the tab key once you've started typing the name of a file, the rest of the name will automatically fill in
- This will save you time and prevent typos, especially with long file names 

### Create a directory
	mkdir TestDir

### Move test.txt into new directory
	mv ../test.txt .

### In addition to a file's location, "mv" can also change a file name. Change the name of test.txt to newDoc.txt
	mv test.txt newDoc.txt

### Connecting to HARDAC
- Connect to the cluster by typing 