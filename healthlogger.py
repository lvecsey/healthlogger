#!/usr/bin/python3

import subprocess

from time import sleep

from datetime import datetime

import sys

def main():

    dat_fn = '/var/log/ceph/ceph_health.dat'
    
    counter = 0
    
    outf = open(dat_fn, "a")

    while True:
    
        result = subprocess.run(["ceph", "health", "detail"], capture_output=True, text=True)

        ceph_result = 0.0
        
        if result.stdout.startswith('HEALTH_OK'):
            ceph_result = 1.0

        if result.stdout.startswith('HEALTH_WARN'):
            ceph_result = 0.75

        if result.stdout.startswith('HEALTH_ERR'):
            ceph_result = 0.5
            
        dt = datetime.now()
        
        ts = dt.timestamp()
        
        outf.write(str(ts) + ' ' + str(ceph_result) + '\n')

        if not (counter % 5):
            outf.flush()
        
        sleep(60)
        
        counter += 1
    
    outf.close()
    
    return 0


if __name__ == '__main__':

    main()
    
