#!/usr/bin/env python3

import os
import logging
import subprocess
from argparse import ArgumentParser
import threading
import time


""" This project makes use of:
cputhrottle
http://www.willnolan.com/cputhrottle/cputhrottle.html
"""


def run_subproc(cmd):
    logging.debug(cmd)
    return subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)


def find_dropbox_procs():
    logging.info('Finding Dropbox procs')
    cmd = "ps -axc | grep -w Dropbox"
    p = run_subproc(cmd)
    lines = p.communicate()[0].decode('utf-8').strip().split('\n')
    procs = []
    for line in lines:
        args = [arg for arg in line.split(' ') if arg.replace('?', '')]
        num, ctime = args[0], args[1]
        name = ' '.join(args[2:])
        procs.append((num, ctime, name))
    return procs


def limit_cpu(pid, percent, name='Dropbox'):
    logging.info(f'Limiting {name} ({pid}) to {percent}%')
    pid = str(pid)
    percent = str(percent)

    cmd = f'./cputhrottle {pid} {percent}'
    return run_subproc(cmd)


def kill_old_procs():
    logging.info('Killing old Dropbox Tamer processes (if any)')
    cmd = 'pkill cputhrottle'
    return run_subproc(cmd)


def main(percent, verbosity='INFO', kill=False):
    logging.getLogger().setLevel(verbosity)

    kill_old_procs()
    if not kill:
        processes = find_dropbox_procs()
        for pid, ctime, name in processes:
            limit_cpu(pid, percent, name=name)


if __name__ == '__main__':
    parser = ArgumentParser('Dropbox Tamer', description='Limit the amount of CPU Dropbox is allowed to use')

    parser.add_argument('-p', '--percent', type=int, choices=range(1, 99), metavar="[1-99]",
                        help='Percent of CPU power that Dropbox will be allowed to use')

    parser.add_argument('--kill', action='store_true', help='Kill the process and let Dropbox use the full CPU power')
    parser.add_argument('-v', '--verbosity', default='INFO', type=str.upper,
                        choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'],
                        help='Verbosity level')

    args = parser.parse_args()

    if not any([args.kill, args.percent]):
        raise Exception('The following argument is required: -p/--percent')

    if os.geteuid() == 0:
        main(percent=args.percent, verbosity=args.verbosity, kill=args.kill)
    else:
        exit("You need to have root privileges to run this script.\nPlease try again using 'sudo'. Exiting.")
