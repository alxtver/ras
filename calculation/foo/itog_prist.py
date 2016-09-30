from ras.models import ComplektSK, ComplektSKCal



def createdickt():
    count = ComplektSK.objects.all().count()
    complekts = {}
    i = 1
    while i <= count:
        value = ComplektSK.objects.get(id=i)
        complekts[value.name] = dict(number=0, price=value.price, weight=value.weight)
        i += 1
    return complekts

def stoyki_dic(list_post, kol_total, complekts):
    base_polka = list_post['base_polka']
    kol_125 = int(list_post['kol_125'])
    kol_100 = int(list_post['kol_100'])
    kol_80 = int(list_post['kol_80'])
    kol_65 = int(list_post['kol_65'])
    kol_sku = int(list_post['kol_sku'])
    kol_skun = int(list_post['kol_skun'])
    height_stell = list_post['height_stell']
    dop_stoyka = int(list_post['dop_stoyka'])
    if base_polka == '500':
        base_polka_125 = complekts['Полка 500 СК125']
        base_polka_100 = complekts['Полка 500 СК100']
        base_polka_80 = complekts['Полка 500 СК80']
        base_polka_65 = complekts['Полка 500 СК65']
        base_polka_sku = complekts['Полка 500 СКУ']
        base_polka_skun = complekts['Полка 500 СКУН']

    elif base_polka == '400':
        base_polka_125 = complekts['Полка 400 СК125']
        base_polka_100 = complekts['Полка 400 СК100']
        base_polka_80 = complekts['Полка 400 СК80']
        base_polka_65 = complekts['Полка 400 СК65']
        base_polka_sku = complekts['Полка 400 СКУ']
        base_polka_skun = complekts['Полка 400 СКУН']
    else:
        base_polka_125 = complekts['Полка 600 СК125']
        base_polka_100 = complekts['Полка 600 СК100']
        base_polka_80 = complekts['Полка 600 СК80']
        base_polka_65 = complekts['Полка 600 СК65']
        base_polka_sku = complekts['Полка 600 СКУ']
        base_polka_skun = complekts['Полка 600 СКУН']

    base_polka_125_value = int(base_polka_125['number'])
    base_polka_125['number'] = base_polka_125_value + kol_125
    base_polka_100_value = int(base_polka_100['number'])
    base_polka_100['number'] = base_polka_100_value + kol_100
    base_polka_80_value = int(base_polka_80['number'])
    base_polka_80['number'] = base_polka_80_value + kol_80
    base_polka_65_value = int(base_polka_65['number'])
    base_polka_65['number'] = base_polka_65_value + kol_65
    base_polka_sku_value = int(base_polka_sku['number'])
    base_polka_sku['number'] = base_polka_sku_value + kol_sku
    base_polka_skun_value = int(base_polka_skun['number'])
    base_polka_skun['number'] = base_polka_skun_value + kol_skun


    if height_stell == '2200':
        stoika = complekts['Стойка 2200 с опорой']
        value = int(stoika['number'])
        stoika['number'] = value + kol_total+ dop_stoyka
    elif height_stell == '1600':
        stoika = complekts['Стойка 1600 с опорой']
        value = int(stoika['number'])
        stoika['number'] = value + kol_total+ dop_stoyka
    else:
        stoika = complekts['Стойка 2400 с опорой']
        value = int(stoika['number'])
        stoika['number'] = value + kol_total+ dop_stoyka

    if base_polka == '500':
        bokovina = complekts['Боковина 500 с опорой']
        value = int(bokovina['number'])
        bokovina['number'] = value + kol_total+ dop_stoyka
    elif base_polka == '400':
        bokovina = complekts['Боковина 400 с опорой']
        value = int(bokovina['number'])
        bokovina['number'] = value + kol_total+ dop_stoyka
    else:
        bokovina = complekts['Боковина 600 с опорой']
        value = int(bokovina['number'])
        bokovina['number'] = value + kol_total+ dop_stoyka

    pass



def overall_dic(kol_total, list_post, complekts):

    stoyki_dic(list_post, kol_total, complekts)

    pass












