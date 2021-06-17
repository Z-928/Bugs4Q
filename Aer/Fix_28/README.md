Summary

Resolves issue #204, where Qiskit-Aer wouldn't catch circuits that were too large for the system memory.

Details and comments

The issue was caused by a size_t returned from Aer::Base::State::required_memory_mb being cast to int with value 0, causing the memory check to pass erroneously.
