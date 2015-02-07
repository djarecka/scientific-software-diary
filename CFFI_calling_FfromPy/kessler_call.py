""" simple example of kessler-python function usage"""

import sys
sys.path.append(".")
import numpy as np
from cffi_kessler import kessler

nx = 1
ny = 1
nz = 1
dt_in = 1.

variable_nparr = {}
variable_nparr["t"] = np.ones((nx,nz,ny)) * 291.8
variable_nparr["qv"] = np.ones((nx,nz,ny)) * 10.e-3
variable_nparr["qc"] = np.ones((nx,nz,ny)) * 0.e-3
variable_nparr["rho"] = np.ones((nx,nz,ny))
variable_nparr["pii"] = np.ones((nx,nz,ny)) * .97
variable_nparr["dz8w"] = np.ones((nx,nz,ny)) * 20.
variable_nparr["z"] = np.ones((nx,nz,ny)) * 700.
variable_nparr["qr"] = np.zeros((nx,nz,ny))
for var_nm in ["RAINNC", "RAINNCV"]:
    variable_nparr[var_nm] = np.zeros((nx,ny))

print "before calling the microphysical scheme: temperature, T = %2.2f; water vapour mixing ratio, qv =  %2.4f; and cloud water mixing ratio, qc =  %2.4f" % (variable_nparr["t"], variable_nparr["qv"], variable_nparr["qc"])

kessler(nx, ny, nz, dt_in, variable_nparr)

print "after calling the microphysical scheme: temperature, T = %2.2f; water vapour mixing ratio, qv =  %2.4f; and cloud water mixing ratio, qc =  %2.4f" % (variable_nparr["t"], variable_nparr["qv"], variable_nparr["qc"])

