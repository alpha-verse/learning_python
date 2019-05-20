from collections import deque


def fib(n):
    """ Print fibonacci numbers less than n  """
    a, b = 0, 1
    s = 1
    print(s)
    while (a <= n):
        print(a, end=',')
        a, b = b, a + b


def list_ops():
    list = [2, 45, 34, 43, 23, 89]
    queue = deque(list)

    queue.append(99)
    print(queue)
    print(queue.popleft())
    return queue


def b_map0(Fn, list):
    return [Fn(x) for x in list]


def list_comprehensions(n, m):
    for s, t in [(i, j) for i in range(1, n + 1)
                 for j in range(1, m + 1) if i != j]:
        print(s, t, end=' | ')


def chunk_lists(k, list):
    return [list[x: x + k] for x in range(0, len(list), k)]


print(chunk_lists(3, [1, 2, 3, 4, 5, 6, 7, 8]))
