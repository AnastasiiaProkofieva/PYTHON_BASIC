# 224930 -> 2 дні, 14:28:50
# 950400 -> 11 днів, 00:00:00
# 7948799 -> 91 день, 23:59:59

n = int(input('Please type your number: '))
if 0 <= n < 8640000:
    all_mins, sec = divmod(n, 60)
    all_hours, mins = divmod(all_mins, 60)
    days, hours = divmod(all_hours, 24)
    days = str(days)

    if len(days) == 2 and days[1] == '1' and days != '11':
        data = f'{days} день, {str(hours).zfill(2)}:{str(mins).zfill(2)}:{str(sec).zfill(2)}'
    elif days == '1':
        data = f'{days} день, {str(hours).zfill(2)}:{str(mins).zfill(2)}:{str(sec).zfill(2)}'
    elif len(days) == 2 and days[1] == '2' and days != '12':
        data = f'{days} дні, {str(hours).zfill(2)}:{str(mins).zfill(2)}:{str(sec).zfill(2)}'
    elif days == '2':
        data = f'{days} дні, {str(hours).zfill(2)}:{str(mins).zfill(2)}:{str(sec).zfill(2)}'
    else:
        data = f'{days} днів, {str(hours).zfill(2)}:{str(mins).zfill(2)}:{str(sec).zfill(2)}'
    print(data)

else:
    print('out of range')
