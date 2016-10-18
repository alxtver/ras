def overall_ostrov(list_post, base_dict):
    base_polka_ostrov = list_post['base_polka_ostrov']
    kol_125_ostrov = int(list_post['kol_125_ostrov'])
    kol_100_ostrov = int(list_post['kol_100_ostrov'])
    kol_80_ostrov = int(list_post['kol_80_ostrov'])
    kol_65_ostrov = int(list_post['kol_65_ostrov'])
    height_stell_ostrov = list_post['height_stell_ostrov']
    dop_stoyka_ostrov = int(list_post['dop_stoyka_ostrov'])
    kol_125_30_ostrov = int(list_post['125_30_ostrov'])
    kol_100_30_ostrov = int(list_post['100_30_ostrov'])
    kol_80_30_ostrov = int(list_post['80_30_ostrov'])
    kol_65_30_ostrov = int(list_post['65_30_ostrov'])
    kol_125_40_ostrov = int(list_post['125_40_ostrov'])
    kol_100_40_ostrov = int(list_post['100_40_ostrov'])
    kol_80_40_ostrov = int(list_post['80_40_ostrov'])
    kol_65_40_ostrov = int(list_post['65_40_ostrov'])
    kol_125_50_ostrov = int(list_post['125_50_ostrov'])
    kol_100_50_ostrov = int(list_post['100_50_ostrov'])
    kol_80_50_ostrov = int(list_post['80_50_ostrov'])
    kol_65_50_ostrov = int(list_post['65_50_ostrov'])
    kol_125_60_ostrov = int(list_post['125_60_ostrov'])
    kol_100_60_ostrov = int(list_post['100_60_ostrov'])
    kol_80_60_ostrov = int(list_post['80_60_ostrov'])
    kol_65_60_ostrov = int(list_post['65_60_ostrov'])

    # Колличество островных стеллажей
    kol_total_ostrov = kol_125_ostrov + kol_100_ostrov + kol_80_ostrov + kol_65_ostrov

    # расчет базовых полок и боковин
    if base_polka_ostrov == '500':
        base_dict['Полка 500 СК125']['number'] += kol_125_ostrov * 2
        base_dict['Полка 500 СК100']['number'] += kol_100_ostrov * 2
        base_dict['Полка 500 СК80']['number'] += kol_80_ostrov * 2
        base_dict['Полка 500 СК65']['number'] += kol_65_ostrov * 2
        base_dict['Боковина 500 с опорой'][
            'number'] += (kol_total_ostrov + dop_stoyka_ostrov) * 2
    if base_polka_ostrov == '600':
        base_dict['Полка 600 СК125']['number'] += kol_125_ostrov * 2
        base_dict['Полка 600 СК100']['number'] += kol_100_ostrov * 2
        base_dict['Полка 600 СК80']['number'] += kol_80_ostrov * 2
        base_dict['Полка 600 СК65']['number'] += kol_65_ostrov * 2
        base_dict['Боковина 600 с опорой'][
            'number'] += (kol_total_ostrov + dop_stoyka_ostrov) * 2
    if base_polka_ostrov == '400':
        base_dict['Полка 400 СК125']['number'] += kol_125_ostrov * 2
        base_dict['Полка 400 СК100']['number'] += kol_100_ostrov * 2
        base_dict['Полка 400 СК80']['number'] += kol_80_ostrov * 2
        base_dict['Полка 400 СК65']['number'] += kol_65_ostrov * 2
        base_dict['Боковина 400 с опорой'][
            'number'] += (kol_total_ostrov + dop_stoyka_ostrov) * 2

    # расчет стоек и панелей фриза
    if height_stell_ostrov == '2200':
        base_dict['Стойка 2200 с опорой'][
            'number'] += kol_total_ostrov + dop_stoyka_ostrov
        base_dict['Панель фриза СК125']['number'] += kol_125_ostrov * 4
        base_dict['Панель фриза СК100']['number'] += kol_100_ostrov * 4
        base_dict['Панель фриза СК80']['number'] += kol_80_ostrov * 4
        base_dict['Панель фриза СК65']['number'] += kol_65_ostrov * 4
    if height_stell_ostrov == '1600':
        base_dict['Стойка 1600 с опорой'][
            'number'] += kol_total_ostrov + dop_stoyka_ostrov
        base_dict['Панель фриза СК125']['number'] += kol_125_ostrov * 2
        base_dict['Панель фриза СК100']['number'] += kol_100_ostrov * 2
        base_dict['Панель фриза СК80']['number'] += kol_80_ostrov * 2
        base_dict['Панель фриза СК65']['number'] += kol_65_ostrov * 2
    if height_stell_ostrov == '2400':
        base_dict['Стойка 2400 с опорой'][
            'number'] += kol_total_ostrov + dop_stoyka_ostrov
        base_dict['Панель фриза СК125']['number'] += kol_125_ostrov * 6
        base_dict['Панель фриза СК100']['number'] += kol_100_ostrov * 6
        base_dict['Панель фриза СК80']['number'] += kol_80_ostrov * 6
        base_dict['Панель фриза СК65']['number'] += kol_65_ostrov * 6

    # расчет задних панелей
    if height_stell_ostrov != '1600':
        kol_zad_panel_125 = kol_125_ostrov * 8
        kol_zad_panel_100 = kol_100_ostrov * 8
        kol_zad_panel_80 = kol_80_ostrov * 8
        kol_zad_panel_65 = kol_65_ostrov * 8
    else:
        kol_zad_panel_125 = kol_125_ostrov * 6
        kol_zad_panel_100 = kol_100_ostrov * 6
        kol_zad_panel_80 = kol_80_ostrov * 6
        kol_zad_panel_65 = kol_65_ostrov * 6
    base_dict['Панель задняя СК125']['number'] += kol_zad_panel_125
    base_dict['Панель задняя СК100']['number'] += kol_zad_panel_100
    base_dict['Панель задняя СК80']['number'] += kol_zad_panel_80
    base_dict['Панель задняя СК65']['number'] += kol_zad_panel_65

    # расчет кронштейнов
    kol_kron_30 = (kol_125_ostrov * kol_125_30_ostrov + kol_100_ostrov * kol_100_30_ostrov +
                   kol_80_ostrov * kol_80_30_ostrov + kol_65_ostrov * kol_65_30_ostrov) * 2
    kol_kron_40 = (kol_125_ostrov * kol_125_40_ostrov + kol_100_ostrov * kol_100_40_ostrov +
                   kol_80_ostrov * kol_80_40_ostrov + kol_65_ostrov * kol_65_40_ostrov) * 2
    kol_kron_50 = (kol_125_ostrov * kol_125_50_ostrov + kol_100_ostrov * kol_100_50_ostrov +
                   kol_80_ostrov * kol_80_50_ostrov + kol_65_ostrov * kol_65_50_ostrov) * 2
    kol_kron_60 = (kol_125_ostrov * kol_125_60_ostrov + kol_100_ostrov * kol_100_60_ostrov +
                   kol_80_ostrov * kol_80_60_ostrov + kol_65_ostrov * kol_65_60_ostrov) * 2
    base_dict['Кронштейн 300']['number'] += kol_kron_30
    base_dict['Кронштейн 400']['number'] += kol_kron_40
    base_dict['Кронштейн 500']['number'] += kol_kron_50
    base_dict['Кронштейн 600']['number'] += kol_kron_60

    # расчет полок
    base_dict['Полка 300 СК125']['number'] += kol_125_30_ostrov * kol_125_ostrov
    base_dict['Полка 400 СК125']['number'] += kol_125_40_ostrov * kol_125_ostrov
    base_dict['Полка 500 СК125']['number'] += kol_125_50_ostrov * kol_125_ostrov
    base_dict['Полка 600 СК125']['number'] += kol_125_60_ostrov * kol_125_ostrov

    base_dict['Полка 300 СК100']['number'] += kol_100_30_ostrov * kol_100_ostrov
    base_dict['Полка 400 СК100']['number'] += kol_100_40_ostrov * kol_100_ostrov
    base_dict['Полка 500 СК100']['number'] += kol_100_50_ostrov * kol_100_ostrov
    base_dict['Полка 600 СК100']['number'] += kol_100_60_ostrov * kol_100_ostrov

    base_dict['Полка 300 СК80']['number'] += kol_80_30_ostrov * kol_80_ostrov
    base_dict['Полка 400 СК80']['number'] += kol_80_40_ostrov * kol_80_ostrov
    base_dict['Полка 500 СК80']['number'] += kol_80_50_ostrov * kol_80_ostrov
    base_dict['Полка 600 СК80']['number'] += kol_80_60_ostrov * kol_80_ostrov

    base_dict['Полка 300 СК65']['number'] += kol_65_30_ostrov * kol_65_ostrov
    base_dict['Полка 400 СК65']['number'] += kol_65_40_ostrov * kol_65_ostrov
    base_dict['Полка 500 СК65']['number'] += kol_65_50_ostrov * kol_65_ostrov
    base_dict['Полка 600 СК65']['number'] += kol_65_60_ostrov * kol_65_ostrov
    return base_dict
