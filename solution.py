print(''.join(map(chr, [int(''.join(__import__('re').findall(r'\d+',j))) for j in open("esd-aoc/problem.txt", "r").read().split('\n')])))