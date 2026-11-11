def calculate_energy_charge(units):
    """Calculates the energy charge based on slab-wise rates."""
    if units <= 100:
        return units * 3
    elif units <= 200:
        return (100 * 3) + ((units - 100) * 5)
    else:
        return (100 * 3) + (100 * 5) + ((units - 200) * 8)

def generate_bill(name, units):
    """Generates and prints the formatted electricity bill."""
    fixed_charge = 50.00
    energy_charge = calculate_energy_charge(units)
    tax = 0.05 * (energy_charge + fixed_charge)
    total_bill = energy_charge + fixed_charge + tax
    
    print("\n--- Electricity Bill ---")
    print(f"Consumer Name: {name}")
    print(f"Units Consumed: {units}")
    print("-" * 24)
    print(f"Energy: {energy_charge:.2f} | Fixed: {fixed_charge:.2f} | Tax: {tax:.2f}")
    print(f"Total Bill: {total_bill:.2f}")
    print("------------------------\n")

def main():
    name = input("Enter consumer name: ")
    
    user_input = input("Enter units consumed: ")
    try:
        units = float(user_input)
        if units < 0:
            print("Invalid units. Enter a non-negative number.")
        else:
            generate_bill(name, units)
    except ValueError:
        print("Invalid units. Enter a non-negative number.")

if __name__ == "__main__":
    main()