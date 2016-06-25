#! /usr/bin/env python3

from os.path import ismount
from sys import argv
from subprocess import call


def server_status(nfs_host):
    with open('/dev/null', 'a') as out:
        response = call(['ping', '-c1', nfs_host], stdout=out, stderr=out)
        return not response


user_input = str(argv[1])

host = '192.168.1.10'
mnt = '/mnt/NFS/'
mount = 'sudo mount -t nfs4'
unmount = 'sudo umount'

ping_status = server_status(host)

is_mounted = ismount('/mnt/NFS/plex')

if user_input == 'mount':
    if is_mounted:
        print('Already mounted silly Master!')
    else:
        if ping_status:
            call(['sudo', 'mount', '-t', 'nfs4', '192.168.1.10:/mnt/tank/data', '/mnt/NFS/data'])
            call(['sudo', 'mount', '-t', 'nfs4', '192.168.1.10:/mnt/tank/backup', '/mnt/NFS/backup'])
            call(['sudo', 'mount', '-t', 'nfs4', '192.168.1.10:/mnt/tank/plex', '/mnt/NFS/plex'])
            call(['sudo', 'mount', '-t', 'nfs4', '192.168.1.10:/mnt/Torrents', '/mnt/NFS/torrents'])
            call(['sudo', 'mount', '-t', 'nfs4', '192.168.1.10:/mnt/tank/Zene', '/mnt/NFS/Zene'])
            print('NFS Mounts have been connected. Master!')
        else:
            print('No connection to NFS server. Master!')

if user_input == 'unmount':
    if is_mounted:
        if ping_status:
            call(['sudo', 'umount', '/mnt/NFS/plex'])
            call(['sudo', 'umount', '/mnt/NFS/data'])
            call(['sudo', 'umount', '/mnt/NFS/backup'])
            call(['sudo', 'umount', '/mnt/NFS/torrents'])
            call(['sudo', 'umount', '/mnt/NFS/Zene'])
            print('NFS Mounts have been disconnected!')

        else:
            call(['sudo', 'umount', '-l', '/mnt/NFS/plex'])
            call(['sudo', 'umount', '-l', '/mnt/NFS/data'])
            call(['sudo', 'umount', '-l', '/mnt/NFS/backup'])
            call(['sudo', 'umount', '-l', '/mnt/NFS/torrents'])
            call(['sudo', 'umount', '-l', '/mnt/NFS/Zene'])
            print('NFS Mounts have been forcefully disconnected!')
    else:
        print('NFS Mounts are already disconnected. Master!')
