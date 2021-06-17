class LocalJob(BaseJob):
    if sys.platform in ['darwin', 'win32']:
        _executor = futures.ThreadPoolExecutor()
    else:
        _executor = futures.ProcessPoolExecutor()
    def __init__(self, fn, qobj):
        super().__init__()
        self._qobj = qobj
        self._backend_name = qobj.header.backend_name
        self._future = self._executor.submit(fn, qobj)
        
        
#######################################################################

import os
class LocalJob(BaseJob):
    processes2executors = {}
    def __init__(self, fn, qobj):
        super().__init__()
        self._qobj = qobj
        self._backend_name = qobj.header.backend_name
        pid = os.getpid()
        if pid not in LocalJob.processes2executors:
            print(pid, "first time to create the executor")
            if sys.platform in ['darwin', 'win32']:
                _executor = futures.ThreadPoolExecutor()
            else:
                _executor = futures.ProcessPoolExecutor()
            LocalJob.processes2executors[pid] = _executor
        else:
            print(pid, "reuse my executor")
            _executor = LocalJob.processes2executors[pid]
        self._future = _executor.submit(fn, qobj)
