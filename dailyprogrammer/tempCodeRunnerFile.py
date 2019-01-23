
def balanced(s):
    answer = s.count('x') == s.count('y')
    print(answer)

def balanced_bonus(s):
    answer = len(set([s.count(i) for i in s])) <= 1

balanced('xxxxxyyy')