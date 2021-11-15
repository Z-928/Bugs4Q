import qiskit as qk
qreg = qk.QuantumRegister(7)
layout = {qreg[0]: 12, 
          qreg[1]: 11,
          qreg[2]: 13, 
          qreg[3]: 17, 
          qreg[4]: 14, 
          qreg[5]: 12, 
          qreg[6]: 6}


    ########## error mitigation ##########

meas_calibs, state_labels = complete_meas_cal(
    qubit_list=[0, 1, 2], qr=qreg, circlabel='mcal') 
print(meas_calibs[0])

    # This line below is causing error if I add "initial_layout" in both qk.compiler.transpile and qk.execute
qk.compiler.transpile(meas_calibs, initial_layout=layout)
