from calculation.models import ComplektSKCal

def kol_pol(list_post):
    k125 = int(ComplektSKCal.objects.get(name='Полка 300 СК125').number) + \
           int(ComplektSKCal.objects.get(name='Полка 400 СК125').number) + \
           int(ComplektSKCal.objects.get(name='Полка 500 СК125').number) + \
           int(ComplektSKCal.objects.get(name='Полка 600 СК125').number)
    k100 = int(ComplektSKCal.objects.get(name='Полка 300 СК100').number) + \
           int(ComplektSKCal.objects.get(name='Полка 400 СК100').number) + \
           int(ComplektSKCal.objects.get(name='Полка 500 СК100').number) + \
           int(ComplektSKCal.objects.get(name='Полка 600 СК100').number)
    k80 = int(ComplektSKCal.objects.get(name='Полка 300 СК80').number) + \
           int(ComplektSKCal.objects.get(name='Полка 400 СК80').number) + \
           int(ComplektSKCal.objects.get(name='Полка 500 СК80').number) + \
           int(ComplektSKCal.objects.get(name='Полка 600 СК80').number)
    k65 = int(ComplektSKCal.objects.get(name='Полка 300 СК65').number) + \
           int(ComplektSKCal.objects.get(name='Полка 400 СК65').number) + \
           int(ComplektSKCal.objects.get(name='Полка 500 СК65').number) + \
           int(ComplektSKCal.objects.get(name='Полка 600 СК65').number)
    return k125, k100, k80, k65

def opcii(list_post, base_dict):
    k125 = int(base_dict['Полка 300 СК125']['number']) + \
           int(base_dict['Полка 400 СК125']['number']) + \
           int(base_dict['Полка 500 СК125']['number']) + \
           int(base_dict['Полка 600 СК125']['number'])
    k100 = int(base_dict['Полка 300 СК100']['number']) + \
           int(base_dict['Полка 400 СК100']['number']) + \
           int(base_dict['Полка 500 СК100']['number']) + \
           int(base_dict['Полка 600 СК100']['number'])
    k80 = int(base_dict['Полка 300 СК80']['number']) + \
          int(base_dict['Полка 400 СК80']['number']) + \
          int(base_dict['Полка 500 СК80']['number']) + \
          int(base_dict['Полка 600 СК80']['number'])
    k65 = int(base_dict['Полка 300 СК65']['number']) + \
          int(base_dict['Полка 400 СК65']['number']) + \
          int(base_dict['Полка 500 СК65']['number']) + \
          int(base_dict['Полка 600 СК65']['number'])

    if 'cennniki' in list_post:
        base_dict['Ценникодержатель 125см']['number'] += k125
        base_dict['Ценникодержатель 100см']['number'] += k100
        base_dict['Ценникодержатель 80см']['number'] += k80
        base_dict['Ценникодержатель 65см']['number'] += k65

    if 'ogragdeniya'in list_post:
        base_dict['Ограждение на полку хром. 125см']['number'] += k125
        base_dict['Ограждение на полку хром. 100см']['number'] += k100
        base_dict['Ограждение на полку хром. 80см']['number'] += k80
        base_dict['Ограждение на полку хром. 65см']['number'] += k65
    return base_dict


def overall_opcii(list_post, base_dict):
    opcii(list_post, base_dict)
    return base_dict
