#recquired run rate calculatior

runs= int(input("Enter the total runs scored by the opposition team: "))
chasing_runs = int(input("Enter the total runs scored by chasing team: "))
overs_input = float(input("Enter overs played by chasing team (example: 10.3):  "))

# Separate overs and balls
overs = int(overs_input)
balls = int((overs_input - overs) * 10)
# Convert overs to balls
total_balls = (overs * 6) + balls
# Convert balls back to overs
actual_overs = total_balls / 6  
# Calculate required run rate
required_runs = runs - chasing_runs
remaining_overs = 20 - actual_overs
required_run_rate = required_runs / remaining_overs
print(f"\nRequired Run Rate: {required_run_rate:.2f} runs per over")    
