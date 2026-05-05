# Sports Tournament Points Table
points = [45, 60, -10, 38, 52, -5, 60]
# 1. Replace negative points with 0
for i in range(len(points)):
    if points[i] < 0:
        points[i] = 0
print("Updated Points:", points)
# 2. Sort leaderboard in descending order
points.sort(reverse=True)
print("Sorted Leaderboard:", points)
# 3. Find winner and runner-up
winner = points[0]
runner_up = points[1]
print("Winner Points:", winner)
print("Runner-up Points:", runner_up)


