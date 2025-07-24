# Calculates the total points for a team.
# Each win is worth 2 points, and each draw is worth 1 point.
def calculate_points(team):
    return team.wins * 2 + team.draws


# Sorts a list of team statistics using the Quick Sort algorithm.
# Teams are sorted based on their calculated points.
# If reverse is True, the list is sorted in descending order.
# Otherwise, the list is sorted in ascending order.
def quick_sort_teams(stats, reverse=True):
    # Base case: return the list if it has one or no elements.
    if len(stats) <= 1:
        return stats

    # Select the first element as the pivot.
    pivot = stats[0]
    pivot_points = calculate_points(pivot)

    # Partition the list into two sublists: 
    # 'left' contains teams with more (or fewer) points than the pivot depending on sort order.
    if reverse:
        left = [s for s in stats[1:] if calculate_points(s) > pivot_points]
        right = [s for s in stats[1:] if calculate_points(s) <= pivot_points]
    else:
        left = [s for s in stats[1:] if calculate_points(s) < pivot_points]
        right = [s for s in stats[1:] if calculate_points(s) >= pivot_points]

    # Recursively apply quick sort to the partitions and return the combined result.
    return quick_sort_teams(left, reverse) + [pivot] + quick_sort_teams(right, reverse)


# Performs binary search to find a team in the statistics list by its name.
# The input list must be sorted by team name in ascending order.
# Returns the Statistic object if a match is found, otherwise returns None.
def binary_search_by_team_name(stats, target_name):
    left = 0
    right = len(stats) - 1
    target_name = target_name.lower()

    while left <= right:
        mid = (left + right) // 2
        team_name = str(stats[mid].team).lower()

        if team_name == target_name:
            return stats[mid]  # Exact match found
        elif team_name < target_name:
            left = mid + 1     # Search in the right half
        else:
            right = mid - 1    # Search in the left half

    return None  # No match found