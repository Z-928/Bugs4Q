# Bugs4Q
A Benchmark Suite of Real-World Qiskit Bugs
## Label
**Bug Id**: Our own defined number  

**Issue No**：Number of bug we found :#XXXX  

**Buggy**: Wrong program

**Fixed**: Repaired program

**Modify**: For specific modifications

**Status**: New, unconfirmed, resolved.   

**Version**: Current Version

**Type**: Type of error

**Registered**: Time the bug was raised  

**Resolved**: Time the bug was resovled 
 
## Qiskit Reproduceable Bugs from GitHub
Qiskit is an open-source framework for working with noisy quantum computers at the level of pulses, circuits, and algorithms.

### Terra
This element is Terra and is the foundation on which the rest of Qiskit is built.
| Bug Id | Issue No | Buggy | Fixed | Modify | Status | Version | Type | Registered | Resolved |
| --- | --- | ---| ---| ---| ---| --- | ---| ------ | --- |
| 1 | [#5098](https://github.com/Qiskit/qiskit-terra/issues/5098) | [Buggy](./Terra-0-4000/3/buggy.py) | [Fixed](./Terra-0-4000/3/Fixed.py) | ---| Open | master| parameter | Sep 7, 2020 | ---|
| 2 | [#356](https://github.com/Qiskit/qiskit-terra/issues/356) | [Buggy](./Terra-0-4000/6/buggy.py) | [Fixed](./Terra-0-4000/6/Fixed.py) | ---|Close | ---| qr,qc | Mar 22, 2018 | ---|
| 3 | [#537](https://github.com/Qiskit/qiskit-terra/issues/537);[#783](https://github.com/Qiskit/qiskit-terra/issues/783) | [Buggy](./Terra-0-4000/7/buggy.py) | [Fixed](./Terra-0-4000/7/Fix.py) | ---| Close | 0.5.3 | ! U | Jun 6, 2018 | Jun 8,2018|
| 4 | [#596](https://github.com/Qiskit/qiskit-terra/issues/596) | [Buggy](./Terra-0-4000/8/buggy.py) | [Fixed](./Terra-0-4000/8/fixed.py) | ---| Close | 0.5.4 | empty circuit | Jun 27, 2018 | Jun 27,2018|
| 5 | [#1446](https://github.com/Qiskit/qiskit-terra/issues/1446) | [Buggy](./Terra-0-4000/11/buggy.py) | [Fixed](./Terra-0-4000/11/fix.py) | ---| Close | --- | qasm | Dec 7, 2018 | Dec 8, 2018|
| 6 | [#1985](https://github.com/Qiskit/qiskit-terra/issues/1985) | [Buggy](./Terra-0-4000/13/buggy.py) | [Fixed](./Terra-0-4000/12/fix.py) | ---| Close | ---|lack   | Mar 20, 2018 | Apr 13, 2018|
| 7 | [#3799](https://github.com/Qiskit/qiskit-terra/issues/3799) | [Buggy](./Terra-0-4000/22/buggy.py) | [Fixed](./Terra-0-4000/22/fix.py)| [mod](./Terra-0-4000/22/mod.py)| Close |master| output wrong| Feb 6, 2020|Feb 6, 2020|
| 8 | [#5580](https://github.com/Qiskit/qiskit-terra/issues/5580) | [Buggy](./Terra-4001-6000/Bug_5/buggy.py) |  [Fixed](./Terra-4001-6000/Bug_5/fixed.py)  | --- | Close | --- | Wrong circuit design | Dec 30, 2020 | --- |
| 9 | [#5249](https://github.com/Qiskit/qiskit-terra/issues/5249) | [Buggy](./Terra-4001-6000/Bug_8/buggy.py) |  [Fixed](./Terra-4001-6000/Bug_8/fixed.py)  | --- | Close | --- | Wrong command | Oct 17, 2020 | --- |
| 10 | [#4144](https://github.com/Qiskit/qiskit-terra/issues/4144) | [Buggy](./Terra-4001-6000/Bug_11/buggy.py) |  [Fixed](./Terra-4001-6000/Bug_11/fixed.py)  | --- | Close | --- | Wrong command | Apr 14, 2020 | --- |
| 11 | [#6892](https://github.com/Qiskit/qiskit-terra/issues/6892) | [Buggy](./Terra-6000-7100/6892_Bug/bug_version.py) | [Fixed](./Terra-6000-7100/6892_fixed/fixed_version.py) | --- | Close | 0.19.0 | `QuantumCircuit.parameters` only tracks unbound parameters. | August 11, 2021 | --- |
| 12 | [#6571](https://github.com/Qiskit/qiskit-terra/issues/6571) | [Buggy](./Terra-6000-7100/6571_Bug/bug_version.py) | [Fixed](./Terra-6000-7100/6571_fixed/fixed_version.py) | --- | Close | --- | Being not familiar with the usage of measuring all bit using existing registers. | June 15, 2021 | --- |
| 13 | [#6540](https://github.com/Qiskit/qiskit-terra/issues/6540) | [Buggy](./Terra-6000-7100/6540_Bug/bug_version.py) | [Fixed](./Terra-6000-7100/6540_fixed/fixed_version.py) | --- | Close | 0.17.4 | Qiskit distinguishes operations in `Gate`s | June 9, 2021 | --- |
| 14 | [#6255](https://github.com/Qiskit/qiskit-terra/issues/6255) | [Buggy](./Terra-6000-7100/6255_Bug/bug_version.py) | [Fixed](./Terra-6000-7100/6255_fixed/fixed_version.py) | --- | Close | 0.17.0 | Not fully understanding QASM and statevector/eval computation. | April 19, 2021     | --- |

### Aer
This element is Aer, which provides high-performance quantum computing simulators with realistic noise models.
| Bug Id| Issue No | Buggy | Fixed | Modify| Status |Version|Type|Issue Registered | Issue Resolved |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| 1 | [#135](https://github.com/Qiskit/qiskit-aer/issues/135) | [Buggy](./Aer/bug_1/buggy.py) | [Fixed](./Aer/bug_1/fixed.py) | --- | Close | --- | Ignoring the impact of measurement | Apr 10, 2019 | --- |
| 2 | [#664](https://github.com/Qiskit/qiskit-aer/issues/664) | [Buggy](./Aer/bug_7/buggy.py) | [Fixed](./Aer/bug_7/fixed.py) | --- | Close | --- | Order during measurement | Mar 19, 2020 | --- |
| 3 | [#1192](https://github.com/Qiskit/qiskit-aer/issues/1192) | [Buggy](./Aer/bug_10/buggy.py) | [Fixed](./Aer/bug_10/fixed.py) | --- | Close| --- | Oversized resource consumption | Mar 24, 2021 | --- |
|4 | [#1107;#1108](https://github.com/Qiskit/qiskit-aer/issues/1107) | [Buggy](./Aer/Bug_2) | [Fixed](./Aer/Fix_2) | [Mod](https://github.com/Qiskit/qiskit-aer/pull/1108/files) | Close | 0.7.3 | Bug |  Jan 23, 2021 | Jan 26, 2021 |
|5 | [#1011](https://github.com/Qiskit/qiskit-aer/pull/1011) | [Buggy](./Aer/Bug_4) | [Fixed](./Aer/Fix_4) | [Mod](https://github.com/Qiskit/qiskit-aer/pull/1011/files) | Close | 0.7.1 | Bug | Oct 29, 2020 | Nov 3, 2020 |
|6 | [#580;#605](https://github.com/Qiskit/qiskit-aer/issues/580) | [Buggy](./Aer/Bug_18) | [Fixed](./Aer/Fix_18) | [Mod](https://github.com/Qiskit/qiskit-aer/pull/605/files) | Close | 0.4.1 | Bug |  Feb 11, 2020 | Feb 21, 2020 |
| 7 | [#640](https://github.com/Qiskit/qiskit-aer/pull/640) | [Buggy](./Aer/Bug_19) | [Fixed](./Aer/Fix_19) | [Mod](https://github.com/Qiskit/qiskit-aer/pull/640/files) | Close | 0.4.1→master | Bug |  Feb 27, 2020 | Feb 29, 2020 |
| 8 | [#244](https://github.com/Qiskit/qiskit-aer/issues/244) | [Buggy](./Aer/Bug_26) | [Fixed](./Aer/Fix_26) | [Mod](https://github.com/Qiskit/qiskit-aer/pull/259/files) | Close | 0.2.2→master | Bug |  Jul 2, 2019 | Jul 2, 2019 |

### Ignis
This element is Ignis, which provides tools for quantum hardware verification, noise characterization, and error correction.

| Bug Id | Issue No                                                     | Buggy                   | Fixed                     | Modify                                                       | Status      | Version            | Type            | Test                                                      | Issue Registered | Issue Resolved |
| ------ | ------------------------------------------------------------ | ----------------------- | ------------------------- | ------------------------------------------------------------ | ----------- | ------------------ | --------------- | --------------------------------------------------------- | ---------------- | -------------- |
|1     | [#443](https://github.com/Qiskit/qiskit-ignis/issues/443);[#429](https://github.com/Qiskit/qiskit-ignis/issues/429) | [Buggy](./Ignis/Bug_11) | [Fixed](./Ignis/Fixed_11) | [Mod](https://github.com/Qiskit/qiskit-ignis/pull/435/files) | Close   | 0.3.2              | bug             | [Test](https://github.com/Qiskit/qiskit-ignis/issues/429) | 25 Jun 2020      | 25 Jun 2020    |

### Aqua
 Aqua includes domain application support for:Chemistry，Finance，Machine Learning，Optimization

| Bug Id| Issue No | Buggy | Fixed | Modify| Status |Version|Type|Test|Issue Registered | Issue Resolved |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [#1292](https://github.com/Qiskit/qiskit-aqua/issues/1292) | [Buggy](./Terra-0-4000/1/buggy.py) | [Fixed](./Terra-0-4000/1/Fixed.py) | --- | Close| --- | bug|--- | Sep 30, 2020 | Oct 1, 2020|
| 2| [#1392](https://github.com/Qiskit/qiskit-aqua/issues/1392)|[Buggy](./Aqua/Bug_4/admm_optimizer.py) | [Fixed](./Aqua/Fix_4/admm_optimizer.py) | [Mod](https://github.com/Qiskit/qiskit-aqua/pull/1393/files)|Close|0.8.0|Bug|[Test](./Aqua/Test_4/test4.py)|  Oct 27, 2020| Oct 28, 2020|
|3|[#1324](https://github.com/Qiskit/qiskit-aqua/issues/1324)|[Buggy](./Aqua/Bug_7/vector_state_fn.py) | [Fixed](./Aqua/Fix_7/vector_state_fn.py) | [Mod](https://github.com/Qiskit/qiskit-aqua/commit/750d6c225320fdac07ba14f5dff71031f441e4b8)|Close|---|Bug|[Test](./Aqua/Test_7/Test7.py)| Oct 9 , 2020| Oct 14, 2020|
|4|[#1279](https://github.com/Qiskit/qiskit-aqua/issues/1279)|[Buggy](./Aqua/Bug_8%2C9/grover_optimizer.py) | [Fixed](./Aqua/Fix_8,9/grover_optimizer.py) | [Mod](https://github.com/Qiskit/qiskit-optimization/commit/21969d728e4f47d870916ca2bdb0d3bb152cb373)|Close|0.7.5|Bug|[Test](./Aqua/Test_8/Test8.py)|Sep 29 ,2020| Oct 10, 2020|

## Qiskit Reproduceable Bugs from Stackflow

| Bug Id | Buggy | Fixed | Modify| Status |Version|Type| Registered | Resolved |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [1](https://stackoverflow.com/questions/60918011/implement-quantum-teleportation-in-qiskit) |  [Buggy](./Stackflow-1-5/1/buggy.py) | [Fixed](/Stackflow-1-5/1/Fixed.py) | --- | --- | --- | Output Wrong | Mar 19, 2020| --- |
| [2](https://stackoverflow.com/questions/69598995/qiskits-draw-only-shows-the-circuits-name-and-not-the-architecture) | [Buggy](./stackoverflow-1-5/Bug_2)  | [Fixed](./stackoverflow-1-5/Fixed_2)  | ---    | ---    | ---     | unfamiliar with API                                          | Oct 17, 2021 | ---      |
| [3](https://stackoverflow.com/questions/69245836/getting-figure-x-when-drawing-quantum-circuit-with-qiskit-mpl-output-mo) | [Buggy](./stackoverflow-1-5/Bug_3)  | [Fixed](./stackoverflow-1-5/Fixed_3)  | ---    | ---    | ---     | Mixing the usage of draw method and print method             | ---          | ---      |
| [4](https://stackoverflow.com/questions/64707625/visualizing-circuits-in-qiskit-with-matplotlib) | [Buggy](./stackoverflow-1-5/Bug_11) | [Fixed](./stackoverflow-1-5/Fixed_11) | ---    | ---    | ---     | name conflict.                                               | ---          | ---      |
| [5](https://stackoverflow.com/questions/63283443/my-qiskit-codes-output-differ-from-the-lecturer-ryan-o-donnell)| [Buggy](./stackoverflow-6-10/bug_1/buggy.py) | [Fixed](./stackoverflow-6-10/bug_1/fixed.py) | | | | Label convention is reversed(\|011>&\|110>)  | | |
| [6](https://stackoverflow.com/questions/62661255/2-entangle-qubit-gives-all-states-with-25)| [Buggy](./stackoverflow-6-10/bug_2/buggy.py) | [Fixed](./stackoverflow-6-10/bug_2/fixed.py) | | | | Wrong operation with GATE  |  | |
| [7](https://stackoverflow.com/questions/63342432/python-quantum-fourier-transform)| [Buggy](./stackoverflow-6-10/bug_3/buggy.py) | [Fixed](./stackoverflow-6-10/bug_3/fixed.py) | | | | QFT operation*  | | |

## Qiskit Reproduceable Bugs from StackExchange
| Bug Id                                                       | ID | Buggy | Fixed | Modify | Status | Version | Type                                                         | Registered   | Resolved |
| ------------------------------------------------------------ | -- | ----- | ----- | ------ | ------ | ------- | ------------------------------------------------------------ | ------------ | -------- |
| 1|[#20894](https://quantumcomputing.stackexchange.com/questions/20894/saving-statevector-on-more-than-one-location-in-a-quantum-circuit-in-qiskit) | [Buggy](./StackExchange-page-1-25/Bug_5)  | [Fixed](./StackExchange-page-1-25/Fixed_5)  | ---    | ---    | ---                   | statevector                                  | ---        | ---      |
| 2|[#18448](https://quantumcomputing.stackexchange.com/questions/18448/how-to-perform-a-plot-histogram-for-a-circuit) | [Buggy](./StackExchange-page-1-25/Bug_9)  | [Fixed](./StackExchange-page-1-25/Fixed_9)  | ---    | ---    | ---                   | Unfamiliar with quantum computing            | ---        | ---      |
| 3|[#17651](https://quantumcomputing.stackexchange.com/questions/17651/setting-initial-state-in-qiskit-unitary-simulator) | [Buggy](./StackExchange-page-1-25/Bug_19) | [Fixed](./StackExchange-page-1-25/Fixed_19) | ---    | ---    | ---                   | `transpile` required                         | ---        | ---      |
| 4 | [#15966](https://quantumcomputing.stackexchange.com/questions/15966/was-the-quantum-circuit-attribute-iden-renamed) | [Buggy](./StackExchange/bug_1/buggy.py) | [Fixed](./StackExchange/bug_1/fixed.py) | | | | Outdated grammar | | |
| 5 | [#15925](https://quantumcomputing.stackexchange.com/questions/15925/q-sphere-representation-of-bell-states) | [Buggy](./StackExchange/bug_2/buggy.py) | [Fixed](./StackExchange/bug_2/fixed.py) | | | | Start state is reversed | | |
|6| [#4260](https://quantumcomputing.stackexchange.com/questions/4260/how-to-create-a-condition-on-only-one-classical-bit-when-we-have-a-total-of-2-cl) | [Buggy](./StackExchange/1/buggy.py) | [Fixed](./StackExchange/1/fix.py) | --- | Close| --- | output wrong | --- | ---|
| 7| [#5557](https://quantumcomputing.stackexchange.com/questions/5557/wait-gate-throws-an-error-notimplementederror-no-decomposition-rules-defin) | [Buggy](./StackExchange/3/buggy.py) | [Fixed](StackExchange/3/fix.py) | --- | Close| --- | wait() | --- | ---|
| 8 | [#5959](https://quantumcomputing.stackexchange.com/questions/5959/grovers-algorithm-returns-skewed-probability-distribution) | [Buggy](./StackExchange/4/buggy.py) | [Fixed](StackExchange/4/fix.py) | --- | Close| --- | grover algrithm| --- | ---|
| 9| [#6692](https://quantumcomputing.stackexchange.com/questions/6692/how-do-i-get-out-2-measurements-from-the-same-execution-on-qiskit) | [Buggy](./StackExchange/5/buggy.py) | [Fixed](StackExchange/5/fix.py) | --- | Close| --- | only for simulator| --- | ---|
| 10 | [#6697](https://quantumcomputing.stackexchange.com/questions/6697/creating-and-running-parallel-circuits-in-qiskit) | [Buggy](./StackExchange/6/buggy.py) | [Fixed](StackExchange/6/fix.py) | --- | Close| 0.9 | compiler() removerd | --- | ---|
| 11 | [#7129](https://quantumcomputing.stackexchange.com/questions/7129/how-to-obtain-qubits-amplitude-in-qiskit) | [Buggy](./StackExchange/7/buggy.py) | [Fixed](StackExchange/7/fix.py) | --- | Close| --- |obtain qubit's amplitude  | --- | ---|
| 12 | [#8893](https://quantumcomputing.stackexchange.com/questions/8893/why-is-the-order-reversed-on-measurement) | [Buggy](./StackExchange/9/buggy.py) | [Fixed](StackExchange/9/fix.py) | --- | Close| --- |output   | --- | ---|
| 13 | [#9209](https://quantumcomputing.stackexchange.com/questions/9209/how-to-use-parallel-executions-of-circuits) | [Buggy](./StackExchange/12/buggy.py) | [Fixed](StackExchange/12/fix.py) | --- | Close| --- |threads   | --- | ---|
| 14 | [#9224](https://quantumcomputing.stackexchange.com/questions/9224/how-to-plot-histogram-or-bloch-sphere-for-multiple-circuits) | [Buggy](./StackExchange/14/buggy.py) | [Fixed](StackExchange/14/fix.py) | --- | Close| --- |output wrong   | --- | ---|
| 15 | [#9246](https://quantumcomputing.stackexchange.com/questions/9246/quantum-phase-estimation-implementation) | [Buggy](./StackExchange/15/buggy.py) | [Fixed](StackExchange/15/fix.py) | --- | Close| --- |QFE output wrong  | --- | ---|
| 16 | [#9871](https://quantumcomputing.stackexchange.com/questions/9871/achieve-a-control-gate-with-2-hadamard-coins) | [Buggy](./StackExchange/16/buggy.py) | [Fixed](StackExchange/16/fix.py) | --- | Close| --- | ccx | Feb 16, 2020| ---|
| 17 | [#9943](https://quantumcomputing.stackexchange.com/questions/9943/how-to-make-circuit-for-randomly-selected-gate) | [Buggy](./StackExchange/17/buggy.py) | [Fixed](StackExchange/17/fix.py) | --- | Close| --- | Random gates | Feb 22, 2020| ---|
| 18 | [#12076](https://quantumcomputing.stackexchange.com/questions/12076/real-device-error-mitigation-with-qiskit) | [Buggy](./StackExchange/20/buggy.py) | [Fixed](StackExchange/20/fix.py) | --- | Close| --- | Not a DAG| may 19, 2020| ---|


