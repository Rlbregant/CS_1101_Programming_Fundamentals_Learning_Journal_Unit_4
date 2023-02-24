import random


# Step 1: Initial version In the initial version of the function, we define the function name and the function
# arguments, and return a simple success probability based on the number of crew members:
# def calculate_success_probability(num_crew_members): success_probability = num_crew_members * 10 # Each crew member
# increases the success probability by 10% return success_probability
#
# Step 2: Improved success probability calculation In the second version of the function, we improve the success
# probability calculation to take into account the skill levels of each crew member, which are represented as a list
# of integers between 1 and 10: def calculate_success_probability(num_crew_members, crew_member_skill_levels):
# total_skill_level = sum(crew_skills) avg_skill_level = total_skill_level / num_crew_members success_probability =
# avg_skill_level * 10 # Each crew member increases the success probability by 10% return success_probability
#
# Step 3: Random factor added to simulate unpredictable events In the third version of the function, we add a random
# factor to the success probability calculation to simulate unpredictable events that may occur during the mission:
# def calculate_success_probability(num_crew_members, crew_skills): total_skill_level = sum(crew_skills)
# avg_skill_level = total_skill_level / num_crew_members random_factor = random.randint(-20, 20) / 100  # Simulate
# randomness by adding or subtracting up to 20%. success_probability = max(0, min(100, (avg_skill_level +
# random_factor) * 10))  # Clamp result between 0 and 100. return success_probability
#
# Step 4: Error handling for invalid arguments
# In the fourth version of the function, we add error handling to ensure that the function arguments are valid:
# def calculate_success_probability(num_crew_members, crew_skills):
#     if not isinstance(num_crew_members, int) or num_crew_members <= 0:
#         raise ValueError("num_crew_members must be a positive integer")
#     if not isinstance(crew_skills, list) or len(crew_skills) != num_crew_members:
#         raise ValueError("crew_skills must be a list of integers with length equal to num_crew_members")
#     for skill in crew_skills:
#         if not isinstance(skill, int) or skill < 1 or skill > 10:
#             raise ValueError("crew_skills must be a list of integers between 1 and 10")
#     total_skill_level = sum(crew_skills)
#     avg_skill_level = total_skill_level / num_crew_members
#     random_factor = random.randint(-20, 20) / 100  # Simulate randomness by adding or subtracting up to 20%.
#     success_probability = max(0, min(100, (avg_skill_level + random_factor) * 10))  # Clamp result between 0 and 100.
#     return success_probability

# Step 5: Mash it together
# In the final version of the function, we combine all the above steps into a single function:
def calculate_success_probability(num_crew_members, crew_skills):
    if not isinstance(num_crew_members, int) or num_crew_members <= 0:
        raise ValueError("num_crew_members must be a positive integer")
    if not isinstance(crew_skills, list) or len(crew_skills) != num_crew_members:
        raise ValueError("crew_skills must be a list of integers with length equal to num_crew_members")
    for skill in crew_skills:
        if not isinstance(skill, int) or skill < 1 or skill > 10:
            raise ValueError("crew_skills must be a list of integers between 1 and 10")
    total_skill_level = sum(crew_skills)
    avg_skill_level = total_skill_level / num_crew_members
    random_factor = random.randint(-20, 20) / 100  # Simulate randomness by adding or subtracting up to 20%.
    success_probability = max(0, min(100, (avg_skill_level + random_factor) * 10))  # Clamp result between 0 and 100.
    return success_probability


# Step 6: Test the function Now that we have a function that calculates the success probability of a mission,
# we can test it by calling the function with different arguments:
def main():
    print("Success Probability: {:.2f}%".format(calculate_success_probability(1, [10])))  # Success Probability: 100.00%
    print(
        "Success Probability: {:.2f}%".format(calculate_success_probability(2, [5, 8])))  # Success Probability: 63.20%
    print("Success Probability: {:.2f}%".format(
        calculate_success_probability(3, [1, 2, 3])))  # Success Probability: 18.10%


if __name__ == "__main__":
    main()
