from django.shortcuts import render_to_response, render
from calculation.models import ComplektSK
from calculation.foo.itog_prist import overall_prist
from calculation.foo.itog_ostrov import overall_ostrov
from calculation.foo.opcii import overall_opcii
from calculation.foo.excel_out import WriteToExcel
#from django.template import loader, RequestContext

def base(request):
    errors = []
    if request.method == 'POST':
        nacenka = int(request.POST['nacenka'])
        discont = int(request.POST['discont'])

        list_post = request.POST.copy().dict()

        # создание словаря из базы данных
        base_dict = {}
        for value in ComplektSK.objects.all():
            price = round(value.price + (value.price / 100 *
                                         nacenka) - (value.price / 100 * discont), 2)
            base_dict[value.name] = {
                'number': 0, 'price': price, 'summ': 0, 'weight': value.weight}

        overall_prist(list_post, base_dict)
        overall_ostrov(list_post, base_dict)
        overall_opcii(list_post, base_dict)

        # удаление строк с нулевым количеством
        base_dict = {value: {'number': base_dict[value]['number'], 'price': base_dict[value]['price'], 'summ': base_dict[
            value]['summ'], 'weight': base_dict[value]['weight']} for value in base_dict if int(base_dict[value]['number']) != 0}
        # расчет суммы цен и веса
        for value in base_dict:
            base_dict[value]['summ'] = round(float(base_dict[value]['number']) * float(base_dict[value]['price']), 2)
            base_dict[value]['weight'] = round(float(base_dict[value]['number']) * float(base_dict[value]['weight']), 1)
        # сортировка вывода
        l = sorted(list(base_dict.keys()))
        list_base_dict = [[j, base_dict[j]['number'], base_dict[j]['price'], base_dict[j]['summ'],base_dict[j]['weight']] for j in l]
        itog_price = round(sum([l[3] for l in list_base_dict]), 2)
        itog_weight = round(sum([l[4] for l in list_base_dict]), 1)

        #создание массива json begin
        response_data = []
        final_response = {}
        for a, b, c, d, e in list_base_dict:
            response_record = {}
            response_record['pname'] = a
            response_record['pnumber'] = b
            response_record['pprice'] = c
            response_record['psumm'] = d
            response_record['pweight'] = e
            response_data.append(response_record)
        final_response['product'] = response_data
        request.session['product'] = final_response
        #создание массива json end
        return render(request, 'itog.html', locals())
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
    response = WriteToExcel(a['product'])
    return response
