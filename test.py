''"""""""""""
This problem was asked by Snapchat.
     
      Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
     
      For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

"""""


sample = [(30, 75), (0, 50), (60, 150), (22,65), (120,150)]

def number_of_lectures(lectures):
    rooms = 1
    total_rooms = 0
    if (len(lectures) == 1):
        return 1
    elif(len(lectures) == 0):
        return 0
    else:
        cl = 0
        lec_list = lectures
        while cl < len(lec_list):
            for lec in lec_list:
                if lec[0] < lec_list[cl][-1] and lec[0] > lec_list[cl][0]:
                    rooms += 1
            cl += 1
            if rooms > total_rooms:
                total_rooms = rooms
        return total_rooms


print(number_of_lectures(sample))