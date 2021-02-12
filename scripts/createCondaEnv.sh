#!/bin/bash

LAB_DIR=/data/${SLURM_JOB_ACCOUNT}
CONDA_ROOT=${LAB_DIR}/${USER}/conda
mkdir -p ${CONDA_ROOT}
export CONDA_PKGS_DIRS=${CONDA_ROOT}/pkgs 
export CONDA_ENVS_DIRS=${CONDA_ROOT}/envs
mkdir -p ${CONDA_PKGS_DIRS} ${CONDA_ENVS_DIRS}


