"""
Task
Read an integer N. For all non-negative integers i < N, print i[sqr]. See the sample for details.
"""

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i)
