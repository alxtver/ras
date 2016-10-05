from django.shortcuts import render_to_response, render
from calculation.models import ComplektSK, ComplektSKCal
from calculation.foo.itog import overall, createbase, deletenull, createdickt
from calculation.foo.itog_ostrov import overall_ostrov
from calculation.foo.excel_out import WriteToExcel
from django.template import loader, RequestContext
from django.db import transaction
from django.http import HttpResponse





@transaction.atomic
def base(request):
    errors = []
    if request.method == 'POST':

        list_post = request.POST.copy()
        nacenka = int(request.POST['nacenka'])
        discont = int(request.POST['discont'])

        height_stell_ostrov = request.POST['height_stell_ostrov']
        base_polka_ostrov = request.POST['base_polka_ostrov']
        dop_stoyka_ostrov = int(request.POST['dop_stoyka_ostrov'])
        #Колличество пристенных стеллажей
        kol_total = int(request.POST['kol_125']) +\
                    int(request.POST['kol_100']) +\
                    int(request.POST['kol_80']) +\
                    int(request.POST['kol_65']) +\
                    int(request.POST['kol_sku'])+\
                    int(request.POST['kol_skun'])
        #Колличество островных стеллажей
        kol_total_ostrov = int(request.POST['kol_125_ostrov']) +\
                    int(request.POST['kol_100_ostrov']) +\
                    int(request.POST['kol_80_ostrov']) +\
                    int(request.POST['kol_65_ostrov'])

        count = ComplektSK.objects.all().count()
        ComplektSKCal.objects.all().delete()
        #Расчет стоимости с учетом скидки и наценки
        i = 1
        while i <= count:
                 b = ComplektSK.objects.get(id=i)
                 price_i = round(b.price+(b.price/100*nacenka)-(b.price/100*discont), 2)
                 c = ComplektSKCal(id = b.id, name=b.name, number=0, summ=0, price=price_i,  weight=b.weight)
                 c.save()
                 i += 1

        overall(kol_total, list_post)
        overall_ostrov(kol_total_ostrov, list_post)
        #Расчет сумм цены и веса
        i = 1
        itog_price = 0
        itog_weight = 0
        while i <= count:
                 b = ComplektSKCal.objects.get(id=i)
                 b.summ = b.number*b.price
                 weight = ComplektSKCal.objects.get(id=i).weight
                 number = ComplektSKCal.objects.get(id=i).number
                 i_weight = weight*number
                 b.weight = i_weight
                 itog_weight += i_weight
                 itog_price += b.summ
                 b.save()
                 i += 1
        deletenull()

        order = ComplektSKCal.objects.all().order_by('name')
        x = list(order)
        complekts = createdickt()
        return render(request, 'itogform.html', locals())
        # return render_to_response('itogform.html', locals(), context=RequestContext(request))
    else:
        return render_to_response('baseform.html', {'errors': errors})


def catalog(request):
    order = ComplektSK.objects.all().order_by('id')
    maches = list(order)
    return render_to_response('alldb.html', {'maches': maches})


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Введите поисковый запрос!')
        elif len(q) > 20:
            errors.append('Введите не более 20 символов!')
        else:
            names = ComplektSK.objects.filter(name__icontains=q)
            matches = list(names)
            return render_to_response('search_results.html', {'matches': matches, 'query': q})
    return render_to_response('search.html', {'errors': errors})


def excel(request):
    response = WriteToExcel()
    return response
