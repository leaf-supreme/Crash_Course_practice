#Practice for importing modules and functions
import printing_functions
from printing_functions import show_printed
from printing_functions import print_models as pm
import printing_functions as pf
from printing_functions import *

unprinted_1 = ['orange', 'you', 'glad', 'i didnt', 'say', 'bananna']
printed_1 = []

print_models(unprinted_1, printed_1)
show_printed(printed_1)