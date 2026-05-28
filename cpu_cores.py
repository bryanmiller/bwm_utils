#!/usr/bin/env python

# Determine the number of CPU cores, including power vs efficiency on a Mac
# Bryan Miller
# 2025-03-13

import os
import psutil


def execute(command):
    exe = os.popen(command)
    output = exe.readlines()
    exe.close()
    return output


def get_cores():
    """Get CPU and system information"""
    core_info = {'threads': psutil.cpu_count(logical=True), 'cores': psutil.cpu_count(logical=False), 'performance': 0,
                 'efficiency': 0, 'sys': os.uname().sysname, 'arch': execute('uname -m')[0].strip()}

    if 'arm' in core_info['arch'] and 'Darwin' in core_info['sys']:
        # Performance cores
        command = '/usr/sbin/sysctl -n hw.perflevel0.logicalcpu_max'
        core_info['performance'] = int(execute(command)[0].strip())

        # Efficiency cores
        command = '/usr/sbin/sysctl -n hw.perflevel1.logicalcpu_max'
        core_info['efficiency'] = int(execute(command)[0].strip())

    return core_info


if __name__ == '__main__':
    print(get_cores())
    # print(os.uname())
    print('Done')