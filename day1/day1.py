

def determine_fuel(mass):
    fuel_needed = (int(mass) // 3) - 2
    return 0 if fuel_needed <= 0 else fuel_needed + determine_fuel(fuel_needed)

with open('input.txt','r') as f:
    total_fuel = 0
    for module_mass in f.readlines():
        total_fuel += determine_fuel(module_mass)
    print('total fuel needed:', total_fuel)


