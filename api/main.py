email = 'example@example.com'
domain = email.split('@').pop()
extension = domain.split('.')[-1]
print(extension)



email = 'example@example.com'
username = email.split('@')[0]
print(username)