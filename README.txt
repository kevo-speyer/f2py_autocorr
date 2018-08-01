F2PY INSCTRUCTIONS:
==== =============
1) Create dynamic library from a fortran file:

    $ f2py -c for_fl.f90 --fcompiler=intelem -m test_f2py

or if intel fortran compiler is not installed or does not work:

    $ f2py -c for_fl.f90 -m test_f2py

This will create a new file test_f2py.so wich is callable in any python script

2) Inside the python script import routines from the library:
    
    >>> from test_f2py import f_routine as corr_f
    >>> y = corr_f(x)
