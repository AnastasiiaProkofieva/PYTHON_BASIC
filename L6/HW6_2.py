n = int(input('Please type your number: '))
if 0 <= n < 8640000:
    all_mins, sec = divmod(n, 60)
    all_hours, mins = divmod(all_mins, 60)
    days, hours = divmod(all_hours, 24)
    data = f'{days} days, {str(hours).zfill(2)}:{str(mins).zfill(2)}:{str(sec).zfill(2)}'
    print(data)
else:
    print('out of range')
