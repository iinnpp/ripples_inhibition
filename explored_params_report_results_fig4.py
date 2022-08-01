# II inhibition increase
# for rotation report
# run 20220729_141016
from brian2 import mV, ms
from pypet import cartesian_product

input_dict = {'c_gii': [0.25, 0.3125, 0.375, 0.4375, 0.5, 0.5625, 0.625, 0.6875,
                        0.75, 0.8125, 0.875, 0.9375, 1., 1.0625, 1.125, 1.1875,
                        1.25, 1.3125, 1.375, 1.4375, 1.5, 1.5625, 1.625, 1.6875,
                        1.75, 1.8125, 1.875, 1.9375, 2., 2.0625, 2.125, 2.1875,
                        2.25, 2.3125, 2.375, 2.4375, 2.5, 2.5625, 2.625, 2.6875,
                        2.75, 2.8125, 2.875, 2.9375, 3.],
              'ext_drive': [1.],
              'sigma_noise': [5.0] * mV,
              'dt': [0.1] * ms
              }

name = 'hdf5_data'
explore_dict = cartesian_product(input_dict)
