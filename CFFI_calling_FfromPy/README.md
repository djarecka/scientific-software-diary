To make a share library - libkessler.so, the C wrapper - kessler_wrap.f90 has to be also compiled. Example of compilation using gfortran 4.8.2 (-fdefault-real-8 for double precision):

    $ gfortran -fdefault-real-8 -c -fPIC module_mp_kessler.f90 -o module_mp_kessler.o
    $ gfortran -fdefault-real-8 -shared -fPIC module_mp_kessler.o kessler_wrap.f90 -o libkessler.so

The python binding of the Fortran kessler scheme, using a foreign function interface provided by CFFI, is define in `cffi_kessler.py`.
The simplest example of the python function call is in `kessler_call.py` (tested with python 2.7 and cffi 0.8.2):

     $ python kessler_call.py

possible problems and solutions:
* If can not find the libkessler.so try:

    $ export LD_LIBRARY_PATH=.