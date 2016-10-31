def outed(meet, boss):
    a = len([i for i in meet if meet[i] <= 5])
    if meet[boss] <= 5:
        a += 1
    return 'Nice Work Champ!' if len(meet)/2 > a else 'Get Out Now!'
    # if len(meet)/2 > a:
    #     return 'Nice Work Champ!'
    # return 'Get Out Now!'

print(outed({'tim':0, 'jim':2, 'randy':0, 'sandy':7, 'andy':0, 'katie':5, 'laura':1, 'saajid':2, 'alex':3, 'john':2, 'mr':0}, 'laura'))
