from collections import deque as queue


CACHE_DATA = {}
q = queue()
FULL_QUEUE = 10


def get_val(k):
    if k in CACHE_DATA:
        # q.append(k)
        # check_queue()
        return CACHE_DATA[k]

    else:
        sql = ''
        # Execcute sql
        data = ''
        CACHE_DATA[k] = data
        q.append(k)
        check_queue()
        return data

def check_queue():
    if len(q) >= FULL_QUEUE:
        while len(q) <= FULL_QUEUE:
            q.popleft()



if __name__ == '__main__':
    res = Solution()
    print(res.maxArea([1,1]))