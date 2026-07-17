class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_lst = [i.start for i in intervals]
        end_lst = [i.end for i in intervals]
        start_lst.sort()
        end_lst.sort()
        max_rooms = 0
        num_rooms = 0

        start_i = 0
        end_i = 0

        while start_i < len(start_lst):
            if start_lst[start_i] < end_lst[end_i]:
                num_rooms += 1
                start_i += 1
                max_rooms = max(num_rooms, max_rooms)
            else:
                num_rooms -= 1
                end_i += 1

        return max_rooms