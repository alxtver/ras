from django.http import HttpResponse
import io
from xlsxwriter.workbook import Workbook


def WriteToExcel(a):
    output = io.BytesIO()

    workbook = Workbook(output, {'in_memory': True})
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': 1,
                                'font_size': 16})
    format = workbook.add_format({'border': 2,
                                   'bold': 1})
    format1 = workbook.add_format({'border': 1})
    format2 = workbook.add_format({'right': 2,
                                   'bottom': 1})
    worksheet.set_column('A:A', 5)
    worksheet.set_column('B:B', 30)
    worksheet.set_column('C:C', 13)

    worksheet.write(0, 1, 'Расчет стеллажей', bold)
    worksheet.write(2, 1, 'Наименование', format)
    worksheet.write(2, 2, 'Колличество', format)
    worksheet.write(2, 3, 'Цена', format)
    worksheet.write(2, 4, 'Сумма', format)
    worksheet.write(2, 5, 'Вес', format)

    row = 3
    sm, sw = 0, 0
    for i in a:
        worksheet.write(row, 1, i['pname'], format)
        worksheet.write(row, 2, i['pnumber'], format1)
        worksheet.write(row, 3, i['pprice'], format1)
        worksheet.write(row, 4, i['psumm'], format1)
        sm += int(i['psumm'])
        worksheet.write(row, 5, i['pweight'], format2)
        sw += int(i['pweight'])
        row += 1
    strrow = str(row)

# Write a total using a formula.
    worksheet.write(row, 1, 'Итого', format)
    worksheet.write(row, 2, '', format)
    worksheet.write(row, 3, '', format)
    worksheet.write(row, 4, sm, format)
    worksheet.write(row, 5, sw, format)

    workbook.close()




    output.seek(0)

    response = HttpResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = "attachment; filename=report.xlsx"
    return response
