from qiskit.opflow import Zero, One, Z, I, StateFn

phi = 0.5*((One + Zero)^2)
ZeroOp = ((Z + I)/2)
OneOp = ((I - Z)/2)
h1 = OneOp ^ I
h2 = OneOp^(OneOp+ZeroOp)  # OneOp + ZeroOp == I
h2a = OneOp^OneOp
h2b = OneOp^ZeroOp
print((~StateFn(h1)@phi).eval())
print((~StateFn(h2)@phi).eval())
print((~StateFn(h2a)@phi).eval())
print((~StateFn(h2b)@phi).eval())
print((~StateFn(h2a + h2b)@phi).eval())
print((~StateFn(h2a)@phi).eval() + (~StateFn(h2b)@phi).eval())
print('---')
print(h1.to_matrix() @ phi.to_matrix() @ phi.to_matrix())
print(h2.to_matrix() @ phi.to_matrix() @ phi.to_matrix())
print(h2a.to_matrix() @ phi.to_matrix() @ phi.to_matrix())
print(h2b.to_matrix() @ phi.to_matrix() @ phi.to_matrix())

(0.5+0j)    # correct
(-0.25+0j)  # wrong
(0.25+0j)   # correct
0j          # wrong
(-0.25+0j)  # wrong 
(0.25+0j)   # wrong
---
(0.5+0j)    # correct
(0.5+0j)    # correct
(0.25+0j)   # correct
(0.25+0j)   # correct