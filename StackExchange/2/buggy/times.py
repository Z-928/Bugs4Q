def multiply(first, second, product, n, m):

    a = QuantumRegister(m+n, "a") #accumulator
    b = QuantumRegister(m+n, "b") #holds multiplicand
    c = QuantumRegister(m, "c") #hold multiplier
    d = QuantumRegister(m, "d") #register with value 1
    cl = ClassicalRegister(m+n, "cl") #used for final output
    cl2 = ClassicalRegister(m, "cl2")
    qc = QuantumCircuit(a, b, c, d, cl, cl2, name="qc")

    for i in range(0, m+n):
        if product[i] == "1":  
            qc.x(a[m+n-(i+1)])

    for i in range(0, n):
        if first[i] == "1":
            qc.x(b[n-(i+1)])

    for i in range(0, m):
        if second[i] == "1":
            qc.x(c[m-(i+1)])

    qc.x(d[0])

    for i in range(0, m+n):
        createInputState(qc, a, m+n-(i+1), pie)

    for i in range(m):
        createInputState(qc, c, m-(i+1), pie)

    for i in range(0, m+n):
        evolveQFTState(qc, a, b, m+n-(i+1), pie) 

    for i in range(0, m):
        decrement(qc, c, d, m-(i+1), pie)

    for i in range(0, m):
        inverseQFT(qc, c, i, pie)

    for i in range(0, m+n):
        inverseQFT(qc, a, i, pie)

    for i in range(0, m+n):
        qc.measure(a[i], cl[i])

    for i in range(0, m):
        qc.measure(c[i], cl2[i])

    print(qc.qasm())

    register(Qconfig['APItoken'], Qconfig['url'])
    result = execute(qc, backend='ibmq_qasm_simulator', 
                  shots=1024).result()
    counts = result.get_counts("qc")
    print(counts)
    output = max(counts.items(), key=operator.itemgetter(1))[0]
    multiplier, accumulator = str(output).split(" ")

    print(multiplier)
    print(accumulator)

    return multiplier, accumulator
