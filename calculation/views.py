from django.shortcuts import render_to_response, render
from calculation.models import ComplektSK, ComplektSKCal
from calculation.foo.itog import overall, createbase, deletenull, createdickt
from calculation.foo.itog_ostrov import overall_ostrov
from calculation.foo.opcii import overall_opcii
from calculation.foo.excel_out import WriteToExcel
from django.template import loader, RequestContext
from django.db import transaction
from django.http import HttpResponse



y = 0
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

        for b in ComplektSK.objects.all():
            price_i = round(b.price+(b.price/100*nacenka)-(b.price/100*discont), 2)
            c = ComplektSKCal(id = b.id, name=b.name, number=0, summ=0, price=price_i,  weight=b.weight)
            c.save()

        overall(kol_total, list_post)
        overall_ostrov(kol_total_ostrov, list_post)
        overall_opcii(list_post)

        #Расчет сумм цены и веса
        itog_price = 0
        itog_weight = 0
        for b in ComplektSKCal.objects.all():
            b.summ = b.number*b.price
            weight = b.weight
            number = b.number
            i_weight = weight*number
            b.weight = i_weight
            itog_weight += i_weight
            itog_price += b.summ
            b.save()

        deletenull()

        order = ComplektSKCal.objects.all().order_by('name')

        x = list(order)
        #make json type array begin
        response_data = []
        final_response = {}

        for p in ComplektSKCal.objects.all():
            response_record = {}
            response_record['pname'] = p.name
            response_record['pnumber'] = p.number
            response_record['pprice'] = p.price
            response_record['psumm'] = p.summ
            response_record['pweight'] = p.weight
            response_data.append(response_record)

        final_response["product"] = response_data
        #make json type array end

        request.session['product'] = final_response
        print(request.session['product'])
        complekts = createdickt()
        return render(request, 'itogform.html', locals())
        # return render_to_response('itogform.html', locals(), context=RequestContext(request))
    else:
        return render_to_response('baseform.html', {'errors': errors})


def catalog(request):
    maches = list(ComplektSK.objects.all().order_by('id'))
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
    a = request.session['product']
    print(a['product'])
    response = WriteToExcel(a['product'])
    return response
