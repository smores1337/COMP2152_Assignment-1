"""
Author: Benz Stephen Farinas 
Assignment: #1
"""

# Step b: Create 4 variables
gym_member = "Benz Farinas"  # str
preferred_weight_kg = 60.5  # float
highest_reps = 30  # int
membership_active = True  # bool

# Step c: Create a dictionary named workout_stats
# dictionary: Keys are friend names (str), Values are tuples of workout minutes (int)
workout_stats = {
    "Benz": (30, 45, 20),
    "Jaylyn": (40, 50, 30),
    "Bella": (25, 35, 15)
}

# Step d: Calculate total workout minutes using a loop and add to dictionary
for friend, minutes in workout_stats.copy().items():
    total = sum(minutes)
    workout_stats[friend + "_Total"] = total

# Step e: Create a 2D nested list called workout_list
# workoutlist: 2D nested list where each row is a friend's workout minutes for each activity
workout_list = [
    list(workout_stats["Benz"]),
    list(workout_stats["Jaylyn"]),
    list(workout_stats["Bella"])
]

# Step f: Slice the workout_list
print("Yoga and Running minutes for all friends:")
for i, friend_workouts in enumerate(workout_list):
    print(f"Friend {i+1}: {friend_workouts[:2]}")

print("\nWeightlifting minutes for the last two friends:")
for i, friend_workouts in enumerate(workout_list[-2:]):
    print(f"Friend {i+2}: {friend_workouts[2]}")

# Step g: Check if any friend's total >= 120
print("\n--- Active Friends ---")
for friend in ["Benz", "Jaylyn", "Bella"]:
    total_key = friend + "_Total"
    if workout_stats[total_key] >= 120:
        print(f"Great job staying active, {friend}!")

# Step h: User input to look up a friend
print("\n--- Friend Lookup ---")
friend_name = input("Enter a friend's name to look up: ")

if friend_name in workout_stats and not friend_name.endswith("_Total"):
    yoga, running, weightlifting = workout_stats[friend_name]
    total = workout_stats[friend_name + "_Total"]
    print(f"{friend_name}'s workout minutes:")
    print(f"  Yoga: {yoga} minutes")
    print(f"  Running: {running} minutes")
    print(f"  Weightlifting: {weightlifting} minutes")
    print(f"  Total: {total} minutes")
else:
    print(f"Friend {friend_name} not found in the records.")

# Step i: Friend with highest and lowest total workout minutes
print("\n--- Workout Statistics ---")
friends = ["Benz", "Jaylyn", "Bella"]
totals = {friend: workout_stats[friend + "_Total"] for friend in friends}

max_friend = max(totals, key=totals.get)
min_friend = min(totals, key=totals.get)

print(f"Friend with highest total workout minutes: {max_friend} ({totals[max_friend]} minutes)")
print(f"Friend with lowest total workout minutes: {min_friend} ({totals[min_friend]} minutes)")
