namespace Qrng {

    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Diagnostics;

    @EntryPoint()
    operation GetProbabilityAmplitude() : Double[]
{
    body
    {
        mutable result = new Double[4];
        using (register = Qubit[2])
        {
            H(register[0]);
            CNOT(register[0], register[1]);
            // ...put the amplitude doubles in the result array
        }
        return result;
    }
}

}
