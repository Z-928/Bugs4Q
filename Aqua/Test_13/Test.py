from qiskit.chemistry.drivers import PySCFDriver, UnitsType
atom = 'H 0 0 0; H 0 0 1; H 0 0 2'
driver = PySCFDriver(atom=atom, unit=UnitsType.ANGSTROM, charge=0, spin=1, basis='sto3g')
molecule = driver.run()