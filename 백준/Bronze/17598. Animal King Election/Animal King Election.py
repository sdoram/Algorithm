vote_list = [input() for _ in range(9)]
print('Tiger' if vote_list.count('Tiger') > vote_list.count('Lion') else 'Lion')