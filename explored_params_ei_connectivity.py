# EI connectivity probability
#  model at least 2fold increase
from pypet import cartesian_product

input_dict = {'p_ei': [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1]}

name = 'hdf5_data'
# explore_dict = n_list(input_dict) # check later if I need that
explore_dict = cartesian_product(input_dict)
