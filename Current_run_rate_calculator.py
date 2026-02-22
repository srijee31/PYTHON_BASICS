runs = int(input("Enter total runs scored: "))
overs_input = float(input("Enter overs played (example: 10.3): "))

# Separate overs and balls
overs = int(overs_input)
balls = int((overs_input - overs) * 10)

# Convert overs to balls
total_balls = (overs * 6) + balls

# Convert balls back to overs
actual_overs = total_balls / 6

# Calculate run rate
run_rate = runs / actual_overs

print(f"\nRun Rate: {run_rate} runs per over")