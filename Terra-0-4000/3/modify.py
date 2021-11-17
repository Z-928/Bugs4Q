#change

qc.cx(0, 1, label='Label', ctrl_state=0)
qc.ccx(0, 1, 2, label='Label', ctrl_state=1)

#to

qc.cx(0, 1, ctrl_state='0')
qc.ccx(0, 1, 2, ctrl_state='00')
