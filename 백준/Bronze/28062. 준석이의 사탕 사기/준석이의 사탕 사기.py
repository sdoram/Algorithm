input()

candy = sorted(map(int, input().split()), reverse=True)
even_candy = sum([c for c in candy if c % 2 == 0])
odd_candy = [c for c in candy if c % 2 != 0]

print(even_candy + sum(odd_candy) if sum(odd_candy) % 2 == 0 else even_candy + sum(odd_candy)-odd_candy[-1])