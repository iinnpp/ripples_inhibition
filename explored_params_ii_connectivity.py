# II connectivity probability
from pypet import cartesian_product

input_dict = {'p_ii': [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11,
                       0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2]}

name = 'hdf5_data'
# explore_dict = n_list(input_dict) # check later if I need that
explore_dict = cartesian_product(input_dict)
