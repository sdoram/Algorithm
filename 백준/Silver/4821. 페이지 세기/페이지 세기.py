def document_output(N):
    page = [False for _ in range(int(N))]
    output_page = list(input().split(','))
    for output in output_page:
        out = list(map(int, output.split('-')))
        for o in range(out[0]-1, min(out[-1], len(page))):
            page[o] = True
            
    return sum(page)

while True:
    N = int(input())
    if N == 0:
        break
    print(document_output(N))