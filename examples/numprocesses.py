#!/usr/bin/python

# Count number of running processes.
import os
from metriccounter import MetricCounter, autodump, run_every_n_seconds

def count_procs():
    return len([pid for pid in os.listdir('/proc') if pid.isdigit()])

if __name__ == "__main__":
    process_counter = MetricCounter(
        'proc.num_processes',
        timespan=5,    # Hold a total of 5 seconds.
        granularity=1, # Report data at a single-second granularity.
    )
    with autodump(process_counter) as numproc_counter:
        run_every_n_seconds(1, numproc_counter, count_procs)