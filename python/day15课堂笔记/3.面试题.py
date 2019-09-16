# def demo():
#     for i in range(4):
#         yield i
#
# g=demo()
#
# g1=(i for i in g)
# g2=(i for i in g1)
#
# print(list(g))
# print(list(g1))
# print(list(g2))

def add(n,i):
    return n+i

def test():
    for i in range(4):
        yield i

g=test()
# for n in [1,10,5]:
#     g=(add(n,i) for i in g)
n = 1
g=(add(n,i) for i in test())
n = 10
g=(add(n,i) for i in (add(n,i) for i in test()))
n = 5
g=(15,16,17,18)


print(list(g))