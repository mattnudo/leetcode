class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
            return merged intervals without overlaps between results

            Parameters:
            intervals(List[List[int]]): list of ranges
            newInterval(List[int]): interval to merge into intervals

            Returns:
            List(List[int]): merged intervals
        """
        # This function merges overlapping intervals.
        def merge(intervals: List[List[int]]) -> List[List[int]]:
            # First we sort the intervals based on the starting times.
            intervals.sort(key=lambda x: x[0])
            merged_intervals = [intervals[0]]  # Initialize with the first interval.
          
            # Iterate through the rest of the intervals to merge overlapping ones.
            for start, end in intervals[1:]:
                # If the current interval does not overlap with the last merged interval.
                if merged_intervals[-1][1] < start:
                    merged_intervals.append([start, end])  # Keep it separate.
                else:
                    # They overlap, so we merge them by updating the end time of
                    # the last interval in the merged list if needed.
                    merged_intervals[-1][1] = max(merged_intervals[-1][1], end)
          
            # Return the merged list of intervals.
            return merged_intervals

        # Add the new interval to the existing list of intervals.
        intervals.append(newInterval)

        # Call the merge function to merge any overlapping intervals including the new one.
        return merge(intervals)