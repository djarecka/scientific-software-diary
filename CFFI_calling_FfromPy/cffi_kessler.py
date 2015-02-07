import numpy as np
from constants_kessler import xlv, cp, EP2, SVP1, SVP2, SVP3, SVPT0, rhowater
# use cffi library - a C Foreign Function Interface for Python
from cffi import FFI
ffi = FFI()

def as_pointer(numpy_array):
    return ffi.cast("double*", numpy_array.__array_interface__['data'][0])


# define a python function - binding a C function
def kessler(nx, ny, nz, dt_in, variable_nparr):
    # provide a signature for the C function
    ffi.cdef("void c_kessler(double t[], double qv[], double qc[], double qr[], double rho[], double pii[], double dt_in, double z[], double xlv, double cp, double EP2, double SVP1, double SVP2, double SVP3, double SVPT0, double rhowater, double dz8w[], double RAINNC[], double RAINNCV[], int ids, int ide, int jds, int jde, int kds, int kde, int ims, int ime, int jms, int jme, int kms, int kme, int its, int ite, int jts, int jte, int kts, int kt);", override=True)

    # load a library with the C function
    lib = ffi.dlopen('libkessler.so')

    # create cdata variables of a type "double *" for each numpy array 
    # the cdata variables will be passed to the C function and can be changed 
    variable_Farr = {}
    for item in ["t", "qv", "qc", "qr", "rho", "pii", "z", "dz8w", "RAINNC", "RAINNCV"]:
        variable_Farr[item] = as_pointer(variable_nparr[item]) 

    # create additional variables that will be passed to the C function as values
    [ims, ime, ids, ide, its, ite] = [1, nx] * 3
    [jms, jme, jds, jde, jts, jte] = [1, ny] * 3
    [kms, kme, kds, kde, kts, kte] = [1, nz] * 3

    #import pdb
    #pdb.set_trace()

    # call the C function 
    lib.c_kessler(variable_Farr["t"], variable_Farr["qv"], variable_Farr["qc"], 
                  variable_Farr["qr"], variable_Farr["rho"], variable_Farr["pii"], 
                  dt_in, variable_Farr["z"], xlv, cp, EP2, SVP1, SVP2, SVP3, SVPT0, 
                  rhowater, variable_Farr["dz8w"], variable_Farr["RAINNC"], 
                  variable_Farr["RAINNCV"], ids, ide, jds, jde, kds, kde, 
                  ims, ime, jms, jme, kms, kme, its, ite, jts, jte, kts, kte)
