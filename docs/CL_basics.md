# Getting acquainted with the command line

### Basic commands to navigate HARDAC and submit jobs


### Open the command line on your computer

- Search Terminal in  Spotlight search on Mac, or type Ctrl-Alt-T on Linux


### Change into your home directory
	cd ~/

### Check which directory you're in
	pwd
		
### See what files and/or directories are around
	ls

### Change directories
	cd Documents
	ls
	
### Move back one directory level to your home directory
	cd ..
	
### Change into the Desktop directory and see what files are there
	cd ~/Desktop
	ls

### Download this document to your Desktop
	wget https://raw.githubusercontent.com/jws48/TaylorLabHARDAC_tutorial/main/docs/test.txt

### Print document to your Terminal window
	cat test.txt
	
### Display file contents in temporary window, one page at a time
	less test.txt
	
### Try to autocomplete with tab:
	less tes *tab*
	
- If you hit the tab key once you've started typing the name of a file, the rest of the name will automatically fill in
- This will save you time and prevent typos, especially with long file names 

### Create a directory and change directories into it
	mkdir TestDir
	cd TestDir

### Move test.txt into new directory
	mv ../test.txt .

### In addition to a file's location, "mv" can also change a file name. Change the name of test.txt to newDoc.txt
	mv test.txt newDoc.txt
	echo "And you've uploaded this doc to HARDAC"\!"" >> newDoc.txt

## Connecting to HARDAC
### Upload a file to HARDAC using the secure copy (scp) command
	scp newDoc.txt NetID@hardac-login.genome.duke.edu:/home/NetID

### Upload an entire directory to HARDAC
	cd ..
	scp -r TestDir NetID@hardac-login.genome.duke.edu:/home/NetID

### Connect to HARDAC and start an interactive session
	ssh NetID@hardac-login.genome.duke.edu
	pwd
	ls
	cd TestDir
	cat newDoc.txt

### Copying files with cp
	cp newDoc.txt newDoc_copy.txt
	
### Exit interactive session and log out of HARDAC
	exit #close interactive session
	exit #log off from login node
	
