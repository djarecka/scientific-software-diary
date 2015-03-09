import numpy as np
from constants_kessler import xlv, cp, EP2, SVP1, SVP2, SVP3, SVPT0, rhowater
# use cffi library - a C Foreign Function Interface for Python
from cffi import FFI
ffi = FFI()

def as_pointer(numpy_array):
    assert numpy_array.flags['F_CONTIGUOUS'], \
        "array is not contiguous in memory (Fortran order)"
    return ffi.cast("double*", numpy_array.__array_interface__['data'][0])


# define a python function - binding a C function
def kessler(nx, ny, nz, dt_in, variable_nparr):
    # provide a signature for the C function
    ffi.cdef("void c_kessler(double t[], double qv[], double qc[], double qr[], double rho[], double pii[], double dt_in, double z[], double xlv, double cp, double EP2, double SVP1, double SVP2, double SVP3, double SVPT0, double rhowater, double dz8w[], double RAINNC[], double RAINNCV[], int ids, int ide, int jds, int jde, int kds, int kde, int ims, int ime, int jms, int jme, int kms, int kme, int its, int ite, int jts, int jte, int kts, int kt);", override=True)

    # load a library with the C function
    lib = ffi.dlopen('libkessler.so')

    # create cdata variables of a type "double *" for each numpy array 
    # the cdata variables will be passed to the C function and can be changed 
    variable_CFFI = {}
    for item in ["t", "qv", "qc", "qr", "rho", "pii", "z", "dz8w", "RAINNC", "RAINNCV"]:
        variable_CFFI[item] = as_pointer(variable_nparr[item]) 

    # create additional variables that will be passed to the C function as values
    [ims, ime, ids, ide, its, ite] = [1, nx] * 3
    [jms, jme, jds, jde, jts, jte] = [1, ny] * 3
    [kms, kme, kds, kde, kts, kte] = [1, nz] * 3

    # call the C function 
    lib.c_kessler(variable_CFFI["t"], variable_CFFI["qv"], variable_CFFI["qc"], 
                  variable_CFFI["qr"], variable_CFFI["rho"], variable_CFFI["pii"], 
                  dt_in, variable_CFFI["z"], xlv, cp, EP2, SVP1, SVP2, SVP3, SVPT0, 
                  rhowater, variable_CFFI["dz8w"], variable_CFFI["RAINNC"], 
                  variable_CFFI["RAINNCV"], ids, ide, jds, jde, kds, kde, 
                  ims, ime, jms, jme, kms, kme, its, ite, jts, jte, kts, kte)
