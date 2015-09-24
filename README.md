# subprocess-manager

### Description
A wrapper around python's subprocess module which handles new process spawning (optionally as a dameon), specifiying a timeout period, and printing/logging/accessing the process' output in a non-blocking fashion.

### Installation
`pip install git+git://github.com/agramian/subprocess-manager.git`

### Usage
```
from subprocess_manager.run_subprocess import run_subprocess

process, execution_time = run_subprocess('/bin/bash', ['-l', '-c', 'echo "Hello World!"')
tail_process, command_starttime, command_process_stdout, command_process_stderr = run_subprocess('/bin/bash', ['-l', '-c', 'tail process.log', daemon=True, return_std=True)
```

*See subprocess_manager/run_subprocess.py for additional arguments and details.*
