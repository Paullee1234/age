driving = input('have you driven a car?')
if driving != 'yes' and driving != 'no':
    print('type yes or no only')
    raise SystemExit

age = input('how old are you?')
age = int(age)
if driving == 'yes':
    if age >= 18:
        print('pass')
    else:
        print('how dare you?')
elif driving == 'no':
    if age >= 18:
        print('you can go have a dirvers license')
    else:
        print('you have to wait for', 18 - age, 'years')
