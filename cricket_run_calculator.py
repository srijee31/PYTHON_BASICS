# Cricket Run Calculator

runs = input("Enter runs scored in each ball (separated by space): ")

run_list = [int(r) for r in runs.split()]

total_runs = sum(run_list)

print("Total runs scored:", total_runs)