message = input()
print('none' if ':-)' not in message and ':-(' not in message else 'unsure'
      if message.count(':-)') == message.count(':-(') else 'happy'
      if message.count(':-)') > message.count(':-(') else 'sad')