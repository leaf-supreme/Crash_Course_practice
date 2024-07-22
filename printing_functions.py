def print_models(unprinted_1, printed_1):
    """Simulate Printing each model until none are left """
    while unprinted_1:
        current_print = unprinted_1.pop()
        print(f'Now Printing: {current_print}')
        printed_1.append(current_print)
def show_printed (printed_1):
    """Shows Models that have been printed"""
    print(f'\nThe Following models have been printed')
    for pront in printed_1:
        print(f'{pront} has completed printing')