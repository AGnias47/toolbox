#!/bin/bash
#
#   backup.bash - Perform a system backup and package into tgz file
#
#   A. Gnias | 6/2/2019
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   GNU bash, version 4.4.19(1)-release
#   Vim 8.0 [tabstop=3]

Date=`date +%Y_%m_%d`
tar cvpzf backup_${Date}.tgz --exclude=/proc \
                     --exclude=/lost+found \
                     --exclude=$(pwd)/backup*.tgz \
                     --exclude=/mnt \
                     --exclude=/sys \
                     --exclude=/media/${USER}/EXT \
                     --exclude=/home/${USER}/.local/share/Trash \
                     --exclude=/home/${USER}/.cache \
							--exclude=/home/${USER}/.steam \
							--exclude=/home/${USER}/.config/Code/CachedData \
/home/${USER}/

apt list --installed
