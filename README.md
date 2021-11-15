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
 
## Qiskit Reproduceable Bugs
Qiskit is an open-source framework for working with noisy quantum computers at the level of pulses, circuits, and algorithms.

### Terra
This element is Terra and is the foundation on which the rest of Qiskit is built.
| Bug Id | Issue No | Buggy | Fixed | Modify | Status | Version | Type | Registered | Resolved |
| --- | --- | ---| ---| ---| ---| --- | ---| ------ | --- |
| 3 | [#5098](https://github.com/Qiskit/qiskit-terra/issues/5098) | [Buggy](./Terra-0-4000/3/buggy.py) | [Fixed](./Terra-0-4000/3/Fixed.py) | ---| Open | master| parameter | Sep 7, 2020 | ---|
| 6 | [#356](https://github.com/Qiskit/qiskit-terra/issues/356) | [Buggy](./Terra-0-4000/4/buggy.py) | [Fixed](./Terra-0-4000/6/Fixed.py) | ---|Close | qr,qc| --- | Mar 22, 2018 | ---|
| 7 | [#537](https://github.com/Qiskit/qiskit-terra/issues/537);[#783](https://github.com/Qiskit/qiskit-terra/issues/783) | [Buggy](./Terra-0-4000/7/buggy.py) | [Fixed](./Terra-0-4000/7/Fix.py) | ---| Close | 0.5.3 | ! U | Jun 6, 2018 | Jun 8,2018|
| 8 | [#596](https://github.com/Qiskit/qiskit-terra/issues/596) | [Buggy](./Terra-0-4000/8/buggy.py) | [Fixed](./Terra-0-4000/8/fixed.py) | ---| Close | 0.5.4 | empty circuit | Jun 27, 2018 | Jun 27,2018|
| 11 | [#1446](https://github.com/Qiskit/qiskit-terra/issues/1446) | [Buggy](./Terra-0-4000/11/buggy.py) | [Fixed](./Terra-0-4000/11/fix.py) | ---| Close | --- | qasm | Dec 7, 2018 | Dec 8, 2018|
| 13 | [#1985](https://github.com/Qiskit/qiskit-terra/issues/1985) | [Buggy](./Terra-0-4000/13/buggy.py) | [Fixed](./Terra-0-4000/12/fix.py) | ---| Close | ---|lack   | Mar 20, 2018 | Apr 13, 2018|
| 22 | [#3799](https://github.com/Qiskit/qiskit-terra/issues/3799) | [Buggy](./Terra-0-4000/22/buggy.py) | [Fixed](./Terra-0-4000/22/fix.py)| [mod](./Terra-0-4000/22/mod.py)| Close |master| output wrong| Feb 6, 2020|Feb 6, 2020|
| 5* | [#5580](https://github.com/Qiskit/qiskit-terra/issues/5580) | [Buggy](./Terra-4001-6000/Bug_5/buggy.py) |  [Fixed](./Terra-4001-6000/Bug_5/fixed.py)  | --- | Closed | --- | Wrong circuit design | Dec 30, 2020 | --- |
| 8* | [#5249](https://github.com/Qiskit/qiskit-terra/issues/5249) | [Buggy](./Terra-4001-6000/Bug_8/buggy.py) |  [Fixed](./Terra-4001-6000/Bug_8/fixed.py)  | --- | Closed | --- | Wrong command | Oct 17, 2020 | --- |
| 11* | [#4144](https://github.com/Qiskit/qiskit-terra/issues/4144) | [Buggy](./Terra-4001-6000/Bug_11/buggy.py) |  [Fixed](./Terra-4001-6000/Bug_11/fixed.py)  | --- | Closed | --- | Wrong command | Apr 14, 2020 | --- |
| *5 | [6892](https://github.com/Qiskit/qiskit-terra/issues/6892) | [Buggy](./Terra-6000-7100/6892_Bug/bug_version.py) | [Fixed](./Terra-6000-7100/6892_fixed/fixed_version.py) | --- | resolved | 0.19.0 | `QuantumCircuit.parameters` only tracks unbound parameters. | August 11, 2021 | --- |
| *10 | [6571](https://github.com/Qiskit/qiskit-terra/issues/6571) | [Buggy](./Terra-6000-7100/6571_Bug/bug_version.py) | [Fixed](./Terra-6000-7100/6571_fixed/fixed_version.py) | --- | resolved | --- | Being not familiar with the usage of measuring all bit using existing registers. | June 15, 2021 | --- |
| *11 | [6540](https://github.com/Qiskit/qiskit-terra/issues/6540) | [Buggy](./Terra-6000-7100/6540_Bug/bug_version.py) | [Fixed](./Terra-6000-7100/6540_fixed/fixed_version.py) | --- | resolved | 0.17.4 | Qiskit distinguishes operations in `Gate`s | June 9, 2021 | --- |
| *15 | [6255](https://github.com/Qiskit/qiskit-terra/issues/6255) | [Buggy](./Terra-6000-7100/6255_Bug/bug_version.py) | [Fixed](./Terra-6000-7100/6255_fixed/fixed_version.py) | --- | resolved | 0.17.0 | Not fully understanding QASM and statevector/eval computation. | April 19, 2021     | --- |

### Aer
This element is Aer, which provides high-performance quantum computing simulators with realistic noise models.
| Bug Id| Issue No | Buggy | Fixed | Modify| Status |Version|Type|Test|Issue Registered | Issue Resolved |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1* | [#135](https://github.com/Qiskit/qiskit-aer/issues/135) | [Buggy](./Aer/bug_1/buggy.py) | [Fixed](./Aer/bug_1/fixed.py) | --- | Closed | --- |---| Ignoring the impact of measurement | Apr 10, 2019 | --- |
| 7* | [#664](https://github.com/Qiskit/qiskit-aer/issues/664) | [Buggy](./Aer/bug_7/buggy.py) | [Fixed](./Aer/bug_7/fixed.py) | --- | Closed | --- |---| Order during measurement | Mar 19, 2020 | --- |
| 10* | [#1192](https://github.com/Qiskit/qiskit-aer/issues/1192) | [Buggy](./Aer/bug_10/buggy.py) | [Fixed](./Aer/bug_10/fixed.py) | --- | Closed | --- | ---|Oversized resource consumption | Mar 24, 2021 | --- |

|* 2 | [#1107;#1108](https://github.com/Qiskit/qiskit-aer/issues/1107) | [Buggy](./Aer/Bug_2) | [Fixed](./Aer/Fix_2) | [Mod](https://github.com/Qiskit/qiskit-aer/pull/1108/files) | Resolved | 0.7.3 | Bug | [Test](./Aer/Test_2/Test_2.py) | Jan 23, 2021 | Jan 26, 2021 |
|* 4 | [#1011](https://github.com/Qiskit/qiskit-aer/pull/1011) | [Buggy](./Aer/Bug_4) | [Fixed](./Aer/Fix_4) | [Mod](https://github.com/Qiskit/qiskit-aer/pull/1011/files) | Resolved | 0.7.1 | Bug | [Test](https://github.com/Qiskit/qiskit-aer/issues/997) | Oct 29, 2020 | Nov 3, 2020 |
|* 18 | [#580;#605](https://github.com/Qiskit/qiskit-aer/issues/580) | [Buggy](./Aer/Bug_18) | [Fixed](./Aer/Fix_18) | [Mod](https://github.com/Qiskit/qiskit-aer/pull/605/files) | Resolved | 0.4.1 | Bug | [Test](./Aer/Test_18) | Feb 11, 2020 | Feb 21, 2020 |
| * 19 | [#640](https://github.com/Qiskit/qiskit-aer/pull/640) | [Buggy](./Aer/Bug_19) | [Fixed](./Aer/Fix_19) | [Mod](https://github.com/Qiskit/qiskit-aer/pull/640/files) | Resolved | 0.4.1→master | Bug | [Test](./Aer/Test_19) | Feb 27, 2020 | Feb 29, 2020 |
| * 26 | [#244](https://github.com/Qiskit/qiskit-aer/issues/244) | [Buggy](./Aer/Bug_26) | [Fixed](./Aer/Fix_26) | [Mod](https://github.com/Qiskit/qiskit-aer/pull/259/files) | Resolved | 0.2.2→master | Bug | [Test](./Aer/Test_26/Test_26.py) | Jul 2, 2019 | Jul 2, 2019 |

### Ignis
This element is Ignis, which provides tools for quantum hardware verification, noise characterization, and error correction.

| Bug Id | Issue No                                                     | Buggy                   | Fixed                     | Modify                                                       | Status      | Version            | Type            | Test                                                      | Issue Registered | Issue Resolved |
| ------ | ------------------------------------------------------------ | ----------------------- | ------------------------- | ------------------------------------------------------------ | ----------- | ------------------ | --------------- | --------------------------------------------------------- | ---------------- | -------------- |
|* 11     | [#443](https://github.com/Qiskit/qiskit-ignis/issues/443);[#429](https://github.com/Qiskit/qiskit-ignis/issues/429) | [Buggy](./Ignis/Bug_11) | [Fixed](./Ignis/Fixed_11) | [Mod](https://github.com/Qiskit/qiskit-ignis/pull/435/files) | Resolved    | 0.3.2              | bug             | [Test](https://github.com/Qiskit/qiskit-ignis/issues/429) | 25 Jun 2020      | 25 Jun 2020    |

### Aqua
 Aqua includes domain application support for:Chemistry，Finance，Machine Learning，Optimization

| Bug Id| Issue No | Buggy | Fixed | Modify| Status |Version|Type|Test|Issue Registered | Issue Resolved |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [#1292](https://github.com/Qiskit/qiskit-aqua/issues/1292) | [Buggy](./Terra-0-4000/1/buggy.py) | [Fixed](./Terra-0-4000/1/Fixed.py) | --- | Close| --- | bug|--- | Sep 30, 2020 | Oct 1, 2020|
| 2| [#1392](https://github.com/Qiskit/qiskit-aqua/issues/1392)|[Buggy](./Aqua/Bug_4/admm_optimizer.py) | [Fixed](./Aqua/Fix_4/admm_optimizer.py) | [Mod](https://github.com/Qiskit/qiskit-aqua/pull/1393/files)|Resloved|0.8.0|Bug|[Test](./Aqua/Test_4/test4.py)|  Oct 27, 2020| Oct 28, 2020|
|3|[#1324](https://github.com/Qiskit/qiskit-aqua/issues/1324)|[Buggy](./Aqua/Bug_7/vector_state_fn.py) | [Fixed](./Aqua/Fix_7/vector_state_fn.py) | [Mod](https://github.com/Qiskit/qiskit-aqua/commit/750d6c225320fdac07ba14f5dff71031f441e4b8)|Resloved|---|Bug|[Test](./Aqua/Test_7/Test7.py)| Oct 9 , 2020| Oct 14, 2020|
|4|[#1279](https://github.com/Qiskit/qiskit-aqua/issues/1279)|[Buggy](./Aqua/Bug_8%2C9/grover_optimizer.py) | [Fixed](./Aqua/Fix_8,9/grover_optimizer.py) | [Mod](https://github.com/Qiskit/qiskit-optimization/commit/21969d728e4f47d870916ca2bdb0d3bb152cb373)|Resloved|0.7.5|Bug|[Test](./Aqua/Test_8/Test8.py)|Sep 29 ,2020| Oct 10, 2020|

