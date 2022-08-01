# EI connectivity increase
# for rotation report
# run
from brian2 import mV, ms
from pypet import cartesian_product

input_dict = {'p_ei': [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1],
              'ext_drive': [1.],
              'sigma_noise': [5.0] * mV,
              'dt': [0.1] * ms
              }

name = 'hdf5_data'
explore_dict = cartesian_product(input_dict)
