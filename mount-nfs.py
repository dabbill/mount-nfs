#! /usr/bin/env python3

import os.path
import sys
import subprocess

def server_status(nfs_host):
    with open('/dev/null', 'a') as out:
        response = subprocess.call(['ping', '-c1', nfs_host], stdout=out, stderr=out)
        return not response


user_input1 = str(sys.argv[1])

host = '192.168.1.10'
mnt = '/mnt/NFS/'
mount = 'sudo mount -t nfs'
unmount = 'sudo umount'

ping_status = server_status(host)

is_mounted = os.path.ismount('/mnt/NFS/plex')

if user_input1 == 'mount':
    if is_mounted:
        print('Already mounted silly Master!')
    else:
        if ping_status:
            subprocess.call(['sudo', 'mount', '-t', 'nfs', '192.168.1.10:/mnt/tank/data', '/mnt/NFS/data'])
            subprocess.call(['sudo', 'mount', '-t', 'nfs', '192.168.1.10:/mnt/tank/backup', '/mnt/NFS/backup'])
            subprocess.call(['sudo', 'mount', '-t', 'nfs', '192.168.1.10:/mnt/tank/plex', '/mnt/NFS/plex'])
            subprocess.call(['sudo', 'mount', '-t', 'nfs', '192.168.1.10:/mnt/Torrents', '/mnt/NFS/torrents'])
            subprocess.call(['sudo', 'mount', '-t', 'nfs', '192.168.1.10:/mnt/tank/Zene', '/mnt/NFS/Zene'])
            print('NFS Mounts have been connected. Master!')
        else:
            print('No connection to NFS server. Master!')

if user_input1 == 'unmount':
    if is_mounted:
        if ping_status:
            subprocess.call(['sudo', 'umount', '/mnt/NFS/plex'])
            subprocess.call(['sudo', 'umount', '/mnt/NFS/data'])
            subprocess.call(['sudo', 'umount', '/mnt/NFS/backup'])
            subprocess.call(['sudo', 'umount', '/mnt/NFS/torrents'])
            subprocess.call(['sudo', 'umount', '/mnt/NFS/Zene'])
            print('NFS Mounts have been disconnected!')

        else:
            subprocess.call(['sudo', 'umount', '-l', '/mnt/NFS/plex'])
            subprocess.call(['sudo', 'umount', '-l', '/mnt/NFS/data'])
            subprocess.call(['sudo', 'umount', '-l', '/mnt/NFS/backup'])
            subprocess.call(['sudo', 'umount', '-l', '/mnt/NFS/torrents'])
            subprocess.call(['sudo', 'umount', '-l', '/mnt/NFS/Zene'])
            print('NFS Mounts have been forcefully disconnected!')
    else:
        print('NFS Mounts are already disconnected. Master!')
