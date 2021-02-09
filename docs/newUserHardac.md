# New user set up the HARDAC cluster

## Log in to HARDAC

1) Get on the hospital network

    - Either through VPN or by being on campus

- Open the Terminal app on a macOS

Type the following:
    
    ssh yourNetID@hardac-login.genome.duke.edu

4) Enter your Duke password

## Start an interactive session to get off the login node

Type the following:

    srun -p interactive --pty --mem 500 /bin/bash
    
### Let's break down what that command does:

srun: Tell Slurm (the software on the cluster that manages job submission) to run a command

-p: indicates the partition of the cluster. In this case, we want to start an interactive session

--pty: open a pseudo terminal mode

--mem: How much memory (in Mb) to allocate for the interactive session

/bin/bash: Open the interactive session in the bash shell

### You're on the cluster!
You can start running jobs!

### Make a directory with your NetID in the data drive
Type the following:
    
    cd /data/taylorlab/
    
    mkdir NetID