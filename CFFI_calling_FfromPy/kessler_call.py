""" simple example of kessler-python function usage"""

import sys
sys.path.append(".")
import numpy as np
from cffi_kessler import kessler

nx = 2
ny = 4
nz = 3
dt_in = 1.

variable_nparr = {}
variable_nparr["t"] = np.asfortranarray(np.ones((nx,nz,ny))) * 291.8
variable_nparr["qv"] = np.ones((nx,nz,ny), order="F") * 10.e-3
variable_nparr["qv"][:,0,:] *= 0.9
variable_nparr["qv"][:,2,:] *= 1.1
variable_nparr["qv"][1] += 0.0005
variable_nparr["qc"] = np.ones((nx,nz,ny), order='F') * 0.e-3
variable_nparr["rho"] = np.ones((nx,nz,ny), order='F')
variable_nparr["pii"] = np.ones((nx,nz,ny), order='F') * .97
variable_nparr["dz8w"] = np.ones((nx,nz,ny), order='F') * 20.
variable_nparr["z"] = np.ones((nx,nz,ny), order='F') * 700.
variable_nparr["qr"] = np.zeros((nx,nz,ny), order='F')
for var_nm in ["RAINNC", "RAINNCV"]:
    variable_nparr[var_nm] = np.zeros((nx,ny), order="F")
    variable_nparr[var_nm][:,3] = 3
    variable_nparr[var_nm][1,:] +=1

#print "before calling the microphysical scheme: temperature, T = %2.2f; water vapour mixing ratio, qv =  %2.4f; and cloud water mixing ratio, qc =  %2.4f" % (variable_nparr["t"][0], variable_nparr["qv"][0], variable_nparr["qc"][0])

np.set_printoptions(precision=6)
print "water vapour before microphysics \n",  variable_nparr["qv"][:,:,0], "\n", "liquid water  before microphysics \n", variable_nparr["qc"][:,:,0], "\n",variable_nparr["qv"][1,1,0], variable_nparr["qv"][0,2,3], variable_nparr["RAINNC"][1,3]

kessler(nx, ny, nz, dt_in, variable_nparr)

#print "after calling the microphysical scheme: temperature, T = %2.2f; water vapour mixing ratio, qv =  %2.4f; and cloud water mixing ratio, qc =  %2.4f" % (variable_nparr["t"], variable_nparr["qv"], variable_nparr["qc"])

print "water vapour after microphysics \n",  variable_nparr["qv"][:,:,0], "\n", "liquid water after microphysics \n", variable_nparr["qc"][:,:,0], "\n", variable_nparr["qv"][1,1,0], variable_nparr["qv"][0,2,3]

