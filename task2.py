import numpy as np

income = np.array([
    [100000, 110000, 120000, 130000, 140000, 150000, 160000, 170000, 180000, 190000],
    [80000, 85000, 90000, 95000, 100000, 105000, 110000, 115000, 120000, 125000],
    [120000, 125000, 130000, 135000, 140000, 145000, 150000, 155000, 160000, 165000]
])

print(income)

net_income = income * 0.70

print(net_income)

tax_rates = np.array([
    0.30, 0.30, 0.30, 0.30, 0.40,
    0.40, 0.40, 0.30, 0.30, 0.30
])

corrected_net_income = income * (1 - tax_rates)

print(corrected_net_income)

second_quarter = corrected_net_income[:, 3:6]

print(second_quarter)

# Calculate total net income for Q2 by department

q2_totals = second_quarter.sum(axis=1)

print("\n--- Total Net Income for Q2 ---")

for department, total in enumerate(q2_totals, start=1):
    print(f"Department {department}: {total:.2f} EUR")
