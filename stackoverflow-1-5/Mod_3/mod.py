# The snipplet above ==== is buggy version; the code below ==== is fixed version.
print ('This is the initial state')
print(Qc.draw(output = 'mpl'))
print ('')
#============
print ('This is the initial state')
Qc.draw('mpl').show()