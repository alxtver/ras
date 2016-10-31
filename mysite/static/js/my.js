function ras(){
    var table = document.getElementById('table');
    var number;
    var price;
    var summ = 0;
    var summweight = 0;
    var weight;
    var i;
    for (i = 1; i < table.rows.length-1; i++) {
        number = Number(table.rows[i].cells[1].innerHTML);
        price = parseFloat(table.rows[i].cells[2].innerHTML.replace(',', '.'));
        summ += price * number;
        table.rows[i].cells[3].innerHTML = (price * number).toFixed(1).toString().replace('.', ',');
        if (number == 0) {
            table.rows[i].cells[4].innerHTML = '0,0';
        } else {
            weight = parseFloat(table.rows[i].cells[4].innerHTML.replace(',', '.'))/number;
            summweight += weight * number;
            table.rows[i].cells[4].innerHTML = (weight * number).toFixed(1).toString().replace('.', ',');
        }
    }
    table.rows[i].cells[3].innerHTML = (summ).toFixed(1).toString().replace('.', ',');
    table.rows[i].cells[4].innerHTML = (summweight).toFixed(1).toString().replace('.', ',');
    var  data = [];
    for (i = 1; i < table.rows.length-1; i++) {
        console.log(table.rows[i].cells[2].innerHTML.replace(',', '.'));
        data.push({name: table.rows[i].cells[0].innerHTML + '//'
         + table.rows[i].cells[1].innerHTML.replace(',', '.') + '//'
          + table.rows[i].cells[2].innerHTML.replace(',', '.') + '//'
           + table.rows[i].cells[3].innerHTML.replace(',', '.') + '//'
            + table.rows[i].cells[4].innerHTML.replace(',', '.')});
    }

    $.ajax({
      type: "POST",
      url: "/excel/",
      data: data
    })
}


function printDiv()
  {
    var divToPrint=document.getElementById("table");
    newWin= window.open("");
    newWin.document.write(divToPrint.outerHTML);
    newWin.print();
    newWin.close();
  }
