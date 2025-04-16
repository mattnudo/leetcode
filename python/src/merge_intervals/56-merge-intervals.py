class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals by their start time.
        intervals.sort(key = lambda x: x[0])
        # Create an empty list called merged to store the merged intervals.
        merged_intervals = [intervals[0]]
        # Iterate through the intervals and check if it overlaps with the last interval in the merged list.
        for interval in range(1,len(intervals)):
            if  merged_intervals[-1][1] >= intervals[interval][0]:
                # If it overlaps, merge the intervals by updating the end time of the last interval in merged.
                merged_intervals[-1] = [merged_intervals[-1][0], max(intervals[interval][1], merged_intervals[-1][1])]
                print(merged_intervals)
            # If it does not overlap, simply add the current interval to the merged list.
            else:
                merged_intervals.append(intervals[interval])

        return merged_intervals