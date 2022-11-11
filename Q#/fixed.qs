namespace Qrng {

    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Diagnostics;

    @EntryPoint()
    operation MultiQubitDumpMachineDemo() : Unit {
       using (register = Qubit[2]) {
            H(register[0]);
            CNOT(register[0], register[1]);
            DumpMachine("");
            // to avoid ReleasedQubitsAreNotInZeroState exception
            ResetAll(register);
        }
   }

}
    
   
