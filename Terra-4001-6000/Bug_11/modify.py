#change

print(qc.decompose())

#to

transpile(qc, basis_gates=['u1', 'u2', 'u3', 'cx'])
print(qc)
