# [(1000, 1030),
# (1100, 1200),
# (1400, 1500)]

# [(900, 1045),
# (1130, 1145),
# (1430, 1700)]



# 0000 2400


#QUESTION:
A, A_bound = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']], #['9:00', '20:00']
B, B_bound = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']], #['10:00', '18:30']
# t = 30

# [] A or B

# very large A or B

# #Solution
# def avail(A, B, A_bound, B_bound, t):
#     avail, bounds = [], [max(A_bound[0], B_bound[0]), min(A_bound[1], B_bound[1])]
#     m = [['00:00', bounds[0].zfill(5)]] + sorted([[j.zfill(5) for j in i] for i in A+B]) + [[bounds[1].zfill(5), '24:00']]
#     for i in range(len(m)-1):
#         a, b = m[i][1], m[i+1][0]
#         if a < b and helper(a,b, 30): avail.append([a,b])
#     return avail

# def helper(a, b, t):
#     if a[-2:] >= '30': a = '{:02}:{:02}'.format((int(a[:-3])+1), (int(a[-2:]) + t)%60)
#     else: a = '{}:{:02}'.format(a[:-3], int(a[-2:]) + t).zfill(5)
#     return a <= b


# if '__main__' == __name__:
#     print('Common time available:', avail(A, B, A_bound, B_bound, t))

class Solution:
    def freeSlots(self, p1s, p2s, time):
        booked_times = []
        output = []
        p1 = 0
        p2 = 0

        while p1 < len(p1s) or p2 < len(p2s):

            if compareTimes(p1s[p1][0], p2s[p2][0]) == -1: # P1 less than p2
                booked_times.append(p1s[p1])
                p1 += 1
            else:
                booked_times.append(p2s[p2])
                p2 += 1

        i = 0
        while i < len(booked_times) - 1:

            end1 = booked_times[i][1]
            start2 = booked_times[i+1][0]

            if compareTimes(end1, start2) == 1: # end1 greater than start2
                end2 = booked_times[i+1][1]

                if compareTimes(end1, end2) == 1: # delete intervval
                    booked_times.pop(i+1) 
                    i -= 1
                else:
                    booked_times[i][1] = end2 # Change end to largest

                continue

            i += 1

        
        for i in range(len(booked_times) - 1):
            end1 = booked_times[i][1]
            start2 = booked_times[i+1][0]
            if diffBetween(end1, start2) >= time: # only necessary if time is given
                output.append([end1, start2])

        return output


def compareTimes(time1, time2):
    h1, m1 = time1.split(':')
    h2, m2 = time2.split(':')

    time1 = int(h1) * 60 + int(m1)
    time2 = int(h2) * 60 + int(m2)

    if time1 > time2:
        return 1 # Greater than

    if time2 > time1:
        return -1 # Lesser than

    else:
        return 0 # Equal

def diffBetween(t1, t2):
    pass

if '__main__' == __name__:
    ans = Solution()
    res = ans.freeSlots([()])
    print(res)