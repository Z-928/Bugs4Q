from pyscf import gto, scf
atom = 'H 0 0 0; H 0 0 1; H 0 0 2'
mol = gto.M(atom=atom, basis='sto3g',spin=1)
mf = scf.RHF(mol)
mf.kernel()
