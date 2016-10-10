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

def opcii(list_post):
    if 'cennniki' in list_post:
        cen_125 = ComplektSKCal.objects.get(name='Ценникодержатель 125см')
        cen_100 = ComplektSKCal.objects.get(name='Ценникодержатель 100см')
        cen_80 = ComplektSKCal.objects.get(name='Ценникодержатель 80см')
        cen_65 = ComplektSKCal.objects.get(name='Ценникодержатель 65см')
        cen_125.number, cen_100.number, cen_80.number, cen_65.number, = kol_pol(list_post)
        cen_125.save()
        cen_100.save()
        cen_80.save()
        cen_65.save()
    if 'ogragdeniya'in list_post:
        ogr_125 = ComplektSKCal.objects.get(name='Ограждение на полку хром. 125см')
        ogr_100 = ComplektSKCal.objects.get(name='Ограждение на полку хром. 100см')
        ogr_80 = ComplektSKCal.objects.get(name='Ограждение на полку хром. 80см')
        ogr_65 = ComplektSKCal.objects.get(name='Ограждение на полку хром. 65см')
        ogr_125.number, ogr_100.number, ogr_80.number, ogr_65.number, = kol_pol(list_post)
        ogr_125.save()
        ogr_100.save()
        ogr_80.save()
        ogr_65.save()
    pass


def overall_opcii(list_post):
    opcii(list_post)
    pass
