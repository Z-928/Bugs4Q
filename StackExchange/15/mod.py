#change
def qft_dagger(circ, q, n):
    """n-qubit inverse QFT on q in circ."""
    # SWAP gates
    for i in range(n//2):
        circ.swap(q[i], q[n - i - 1])

    for i in reversed(range(n)):
        circ.h(q[i])
        for m in reversed(range(i)):
            circ.cu1(-2*np.pi/2**(i - m + 1), q[i], q[m])
        circ.barrier()
        
#to
def qft_dagger(circ, q, n):
    """n-qubit inverse QFT on q in circ."""
    for i in range(n-1,-1,-1):
        for m in range(n-i,1,-1):
            circ.cu1(-2*math.pi/2**m, q[i+m-1], q[i])
        circ.h(q[i])
        circ.barrier()
