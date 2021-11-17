#change
for _ in range(2):

    # Encode S1 * !S2 * S3
    circuit.x( search_register[2] )
    circuit.ccx( search_register[1], search_register[2], ancillaries[0] )
    circuit.ccx( search_register[3], ancillaries[0], ancillaries[1] )
    circuit.x( search_register[2] )

    # Encode S0 * S1
    circuit.ccx( search_register[0], search_register[1], ancillaries[2] )

    # Encode oracle ((S0 * S1) + (S1 * !S2 * S3))
    circuit.x(ancillaries)
    circuit.ccx( ancillaries[1], ancillaries[2], m_qubit[0] )
    circuit.x(ancillaries)
    circuit.x(m_qubit)

    # Reset ancillaries to be used later
    circuit.reset(ancillaries)

    # Do rotation about the average
    circuit.h(search_register)
    circuit.x(search_register)
    circuit.ccx( search_register[0], search_register[1], ancillaries[0] )
    circuit.ccx( search_register[2], ancillaries[0], ancillaries[1] )
    circuit.ccx( search_register[3], ancillaries[1], m_qubit[0] )
    circuit.x(search_register)
    circuit.x(m_qubit)
    circuit.h(search_register)

    # Reset ancillaries for use later
    circuit.reset(ancillaries)



#to
for _ in range(2):

    # Encode S1 * !S2 * S3
    circuit.x( search_register[2] )
    circuit.ccx( search_register[1], search_register[2], ancillaries[0] )
    circuit.ccx( search_register[3], ancillaries[0], ancillaries[1] )

    # Encode S0 * S1
    circuit.ccx( search_register[0], search_register[1], ancillaries[2] )

    # Encode oracle ((S0 * S1) + (S1 * !S2 * S3))
    circuit.x(ancillaries)
    circuit.ccx( ancillaries[1], ancillaries[2], m_qubit[0] )
    circuit.x(m_qubit)

    # Return ancillaries to 0s so they can be used later
    circuit.x(ancillaries)
    circuit.ccx( search_register[0], search_register[1], ancillaries[2] )
    circuit.ccx( search_register[3], ancillaries[0], ancillaries[1] )
    circuit.ccx( search_register[1], search_register[2], ancillaries[0] )
    circuit.x( search_register[2] )

    # Do rotation about the average
    circuit.h(search_register)
    circuit.x(search_register)
    circuit.ccx( search_register[0], search_register[1], ancillaries[0] )
    circuit.ccx( search_register[2], ancillaries[0], ancillaries[1] )
    circuit.ccx( search_register[3], ancillaries[1], m_qubit[0] )
    circuit.x(search_register)
    circuit.x(m_qubit)

    # Return ancillaries to 0s for use later
    circuit.ccx( search_register[2], ancillaries[0], ancillaries[1] )
    circuit.ccx( search_register[0], search_register[1], ancillaries[0] )
    circuit.h(search_register)

    # Reset ancillaries for use later
    circuit.reset(ancillaries)

