def overall_prist(list_post, base_dict):
    base_polka = list_post['base_polka']
    kol_125 = int(list_post['kol_125'])
    kol_100 = int(list_post['kol_100'])
    kol_80 = int(list_post['kol_80'])
    kol_65 = int(list_post['kol_65'])
    kol_sku = int(list_post['kol_sku'])
    kol_skun = int(list_post['kol_skun'])
    height_stell = list_post['height_stell']
    dop_stoyka = int(list_post['dop_stoyka'])
    kol_125_30 = int(list_post['125_30'])
    kol_100_30 = int(list_post['100_30'])
    kol_80_30 = int(list_post['80_30'])
    kol_65_30 = int(list_post['65_30'])
    kol_sku_30 = int(list_post['sku_30'])
    kol_skun_30 = int(list_post['skun_30'])
    kol_125_40 = int(list_post['125_40'])
    kol_100_40 = int(list_post['100_40'])
    kol_80_40 = int(list_post['80_40'])
    kol_65_40 = int(list_post['65_40'])
    kol_sku_40 = int(list_post['sku_40'])
    kol_skun_40 = int(list_post['skun_40'])
    kol_125_50 = int(list_post['125_50'])
    kol_100_50 = int(list_post['100_50'])
    kol_80_50 = int(list_post['80_50'])
    kol_65_50 = int(list_post['65_50'])
    kol_sku_50 = int(list_post['sku_50'])
    kol_skun_50 = int(list_post['skun_50'])
    kol_125_60 = int(list_post['125_60'])
    kol_100_60 = int(list_post['100_60'])
    kol_80_60 = int(list_post['80_60'])
    kol_65_60 = int(list_post['65_60'])
    kol_sku_60 = int(list_post['sku_60'])
    kol_skun_60 = int(list_post['skun_60'])

    # Колличество пристенных стеллажей
    kol_total = kol_125 + kol_100 + kol_80 + kol_65 + kol_sku + kol_skun

    # расчет базовых полок и боковин
    if base_polka == '500':
        base_dict['Полка 500 СК125']['number'] += kol_125
        base_dict['Полка 500 СК100']['number'] += kol_100
        base_dict['Полка 500 СК80']['number'] += kol_80
        base_dict['Полка 500 СК65']['number'] += kol_65
        base_dict['Полка 500 СКУ']['number'] += kol_sku
        base_dict['Полка 500 СКУН']['number'] += kol_skun
        base_dict['Боковина 500 с опорой']['number'] += kol_total + dop_stoyka
        base_dict['Панель нижняя СКУ боковина 500']['number'] += kol_sku
        base_dict['Панель нижняя СКУН (боковина 500)']['number'] += kol_skun
    if base_polka == '600':
        base_dict['Полка 600 СК125']['number'] += kol_125
        base_dict['Полка 600 СК100']['number'] += kol_100
        base_dict['Полка 600 СК80']['number'] += kol_80
        base_dict['Полка 600 СК65']['number'] += kol_65
        base_dict['Полка 600 СКУ']['number'] += kol_sku
        base_dict['Полка 600 СКУН']['number'] += kol_skun
        base_dict['Боковина 600 с опорой']['number'] += kol_total + dop_stoyka
        base_dict['Панель нижняя СКУ (боковина 600)']['number'] += kol_sku
        base_dict['Панель нижняя СКУН (боковина 600)']['number'] += kol_skun
    if base_polka == '400':
        base_dict['Полка 400 СК125']['number'] += kol_125
        base_dict['Полка 400 СК100']['number'] += kol_100
        base_dict['Полка 400 СК80']['number'] += kol_80
        base_dict['Полка 400 СК65']['number'] += kol_65
        base_dict['Полка 400 СКУ']['number'] += kol_sku
        base_dict['Полка 400 СКУН']['number'] += kol_skun
        base_dict['Боковина 400 с опорой']['number'] += kol_total + dop_stoyka

    # расчет стоек и панелей фриза
    if height_stell == '2200':
        base_dict['Стойка 2200 с опорой']['number'] += kol_total + dop_stoyka
        base_dict['Панель фриза СК125']['number'] += kol_125 * 2
        base_dict['Панель фриза СК100']['number'] += kol_100 * 2
        base_dict['Панель фриза СК80']['number'] += kol_80 * 2
        base_dict['Панель фриза СК65']['number'] += kol_65 * 2
        base_dict['Панель задняя верхняя СКУ']['number'] += kol_sku
        base_dict['Панель задняя верхняя СКУН']['number'] += kol_skun
    if height_stell == '1600':
        base_dict['Стойка 1600 с опорой']['number'] += kol_total + dop_stoyka
        base_dict['Панель фриза СК125']['number'] += kol_125
        base_dict['Панель фриза СК100']['number'] += kol_100
        base_dict['Панель фриза СК80']['number'] += kol_80
        base_dict['Панель фриза СК65']['number'] += kol_65
    if height_stell == '2400':
        base_dict['Стойка 2400 с опорой']['number'] += kol_total + dop_stoyka
        base_dict['Панель фриза СК125']['number'] += kol_125 * 3
        base_dict['Панель фриза СК100']['number'] += kol_100 * 3
        base_dict['Панель фриза СК80']['number'] += kol_80 * 3
        base_dict['Панель фриза СК65']['number'] += kol_65 * 3
        base_dict['Панель задняя верхняя СКУ']['number'] += kol_sku * 2
        base_dict['Панель задняя верхняя СКУН']['number'] += kol_skun * 2

    # расчет задних панелей
    if height_stell != '1600':
        kol_zad_panel_125 = kol_125 * 4
        kol_zad_panel_100 = kol_100 * 4
        kol_zad_panel_80 = kol_80 * 4
        kol_zad_panel_65 = kol_65 * 4
        kol_zad_panel_sku = kol_sku * 4
        kol_zad_panel_skun = kol_skun * 4
    else:
        kol_zad_panel_125 = kol_125 * 3
        kol_zad_panel_100 = kol_100 * 3
        kol_zad_panel_80 = kol_80 * 3
        kol_zad_panel_65 = kol_65 * 3
        kol_zad_panel_sku = kol_sku * 3
        kol_zad_panel_skun = kol_skun * 3
    base_dict['Панель задняя СК125']['number'] += kol_zad_panel_125
    base_dict['Панель задняя СК100']['number'] += kol_zad_panel_100
    base_dict['Панель задняя СК80']['number'] += kol_zad_panel_80
    base_dict['Панель задняя СК65']['number'] += kol_zad_panel_65
    base_dict['Панель задняя СКУ']['number'] += kol_zad_panel_sku
    base_dict['Панель задняя СКУН']['number'] += kol_zad_panel_skun

    # расчет кронштейнов
    kol_kron_30 = (kol_125 * kol_125_30 + kol_100 * kol_100_30 + kol_80 * kol_80_30 +
                   kol_65 * kol_65_30 + kol_sku * kol_sku_30 + kol_skun * kol_skun_30) * 2
    kol_kron_40 = (kol_125 * kol_125_40 + kol_100 * kol_100_40 + kol_80 * kol_80_40 +
                   kol_65 * kol_65_40 + kol_sku * kol_sku_40 + kol_skun * kol_skun_40) * 2
    kol_kron_50 = (kol_125 * kol_125_50 + kol_100 * kol_100_50 + kol_80 * kol_80_50 +
                   kol_65 * kol_65_50 + kol_sku * kol_sku_50 + kol_skun * kol_skun_50) * 2
    kol_kron_60 = (kol_125 * kol_125_60 + kol_100 * kol_100_60 + kol_80 * kol_80_60 +
                   kol_65 * kol_65_60 + kol_sku * kol_sku_60 + kol_skun * kol_skun_60) * 2
    base_dict['Кронштейн 300']['number'] += kol_kron_30
    base_dict['Кронштейн 400']['number'] += kol_kron_40
    base_dict['Кронштейн 500']['number'] += kol_kron_50
    base_dict['Кронштейн 600']['number'] += kol_kron_60

    # расчет полок
    base_dict['Полка 300 СК125']['number'] += kol_125_30*kol_125
    base_dict['Полка 400 СК125']['number'] += kol_125_40*kol_125
    base_dict['Полка 500 СК125']['number'] += kol_125_50*kol_125
    base_dict['Полка 600 СК125']['number'] += kol_125_60*kol_125

    base_dict['Полка 300 СК100']['number'] += kol_100_30*kol_100
    base_dict['Полка 400 СК100']['number'] += kol_100_40*kol_100
    base_dict['Полка 500 СК100']['number'] += kol_100_50*kol_100
    base_dict['Полка 600 СК100']['number'] += kol_100_60*kol_100

    base_dict['Полка 300 СК80']['number'] += kol_80_30*kol_80
    base_dict['Полка 400 СК80']['number'] += kol_80_40*kol_80
    base_dict['Полка 500 СК80']['number'] += kol_80_50*kol_80
    base_dict['Полка 600 СК80']['number'] += kol_80_60*kol_80

    base_dict['Полка 300 СК65']['number'] += kol_65_30*kol_65
    base_dict['Полка 400 СК65']['number'] += kol_65_40*kol_65
    base_dict['Полка 500 СК65']['number'] += kol_65_50*kol_65
    base_dict['Полка 600 СК65']['number'] += kol_65_60*kol_65

    base_dict['Полка 300 СКУ']['number'] += kol_sku_30*kol_sku
    base_dict['Полка 400 СКУ']['number'] += kol_sku_40*kol_sku
    base_dict['Полка 500 СКУ']['number'] += kol_sku_50*kol_sku
    base_dict['Полка 600 СКУ']['number'] += kol_sku_60*kol_sku

    base_dict['Полка 300 СКУН']['number'] += kol_skun_30*kol_skun
    base_dict['Полка 400 СКУН']['number'] += kol_skun_40*kol_skun
    base_dict['Полка 500 СКУН']['number'] += kol_skun_50*kol_skun
    base_dict['Полка 600 СКУН']['number'] += kol_skun_60*kol_skun
    return base_dict
