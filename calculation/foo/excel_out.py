from django.http import HttpResponse
import io
from xlsxwriter.workbook import Workbook


def WriteToExcel(a):
    output = io.BytesIO()
    sorted_a = []
    for i in a:
        data = []
        data.append(i['pname'])
        data.append(i['pnumber'])
        data.append(i['pprice'])
        data.append(i['psumm'])
        data.append(i['pweight'])
        sorted_a.append(data)

    workbook = Workbook(output, {'in_memory': True})
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': 1, 'font_size': 16})
    formate = workbook.add_format({'border': 2, 'bold': 1})
    format1 = workbook.add_format({'border': 1})
    money = workbook.add_format({'border': 1, 'num_format': '#,##0р.'})
    format2 = workbook.add_format({'right': 2,'bottom': 1})
    worksheet.set_column('A:A', 5)
    worksheet.set_column('B:B', 30)
    worksheet.set_column('C:C', 13)

    worksheet.write(0, 1, 'Расчет стеллажей', bold)
    worksheet.write(2, 1, 'Наименование', formate)
    worksheet.write(2, 2, 'Количество', formate)
    worksheet.write(2, 3, 'Цена', formate)
    worksheet.write(2, 4, 'Сумма', formate)
    worksheet.write(2, 5, 'Вес', formate)

    row = 3
    sm, sw = 0, 0
    for naim, number, price, summ, weight in sorted(sorted_a):
        worksheet.write(row, 1, naim, formate)
        worksheet.write(row, 2, int(number), format1)
        worksheet.write(row, 3, round(float(price), 2), format1)
        worksheet.write(row, 4, round(float(summ), 2), format1)
        sm += float(summ)
        worksheet.write(row, 5, float(weight), format2)
        sw += float(weight)
        row += 1
    strrow = str(row)

# Write a total using a formula.
    worksheet.write(row, 1, 'Итого', formate)
    worksheet.write(row, 2, '', formate)
    worksheet.write(row, 3, '', formate)
    worksheet.write(row, 4, round(sm, 2), formate)
    worksheet.write(row, 5, round(sw, 2), formate)

    workbook.close()
    output.seek(0)
    response = HttpResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = "attachment; filename=report.xlsx"
    return response
