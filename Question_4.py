'''Max is planning to take part in a Diwali contest at a Diwali Party that will begin at 8
PM and will run until midnight (12 AM) i.e., for 4 hours. He also needs to travel to the
party venue within this time which takes him P minutes. The contest comprises
of N problems that are arranged in order of difficulty, with problem 1 being the
simplest and problem N being the most difficult. Max is aware that he will require 5*i
minutes to solve the ith problem.
Your task is help Max find and return an integer value, representing the number of
problems Max can solve and reach the party venue within the given time frame of 4
hours.
Note: Max will leave his home at exactly 8 PM to reach the party venue.
Input Format:
input1: An integer value N, representing the total number of problems.
input2: An integer value P, Representing the time to travel in minutes from his home
to the party venue.'''

def problem(n, p):
    total_t = 240  # Total time available in minutes (4 hours)
    travel_t = p  # Time to travel to the party venue
    solving_t = 0  # Time spent solving problems
    problem_s = 0  # Number of problems solved

    avl_time = total_t - travel_t  # Available time for solving problems

    for i in range(1, n + 1):
        time_to_solve_i = 5 * i  # Time to solve the i-th problem
        if solving_t + time_to_solve_i > avl_time:
            break
        solving_t += time_to_solve_i
        problem_s += 1

    return problem_s

n = 10
p = 60
print(problem(n, p))
