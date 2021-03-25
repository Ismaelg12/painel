google.charts.load("current", {packages:["corechart"]});
    google.charts.setOnLoadCallback(drawChart);
    function drawChart() {
      var data = google.visualization.arrayToDataTable([
        ['Faixa etária', 'Total', {role: 'style'}],
          ["0 a 9", parseInt(etaria_zero), "orange"],
          ["10 a 19", parseInt(etaria_um), "orange"],
          ["20 a 29", parseInt(etaria_dois), "orange"],
          ["30 a 39", parseInt(etaria_tres), "orange"],
          ['40 a 49', parseInt(etaria_quatro), "orange"],
          ['50 a 59', parseInt(etaria_cinco), "orange"],
          ['60 a 69', parseInt(etaria_seis),"orange"],
          ['70 a 79', parseInt(etaria_sete), "orange"],
          ['80 e mais', parseInt(etaria_oito), "orange"]
        ]);

      var view = new google.visualization.DataView(data);
      view.setColumns([0, 1,
                       { calc: "stringify",
                         sourceColumn: 1,
                         type: "string",
                         role: "annotation" },
                       2]);

      var options = {
        title: "",
        width: 270,
        height: 400,
        bar: {groupWidth: "80%"},
        legend: { position: "none" },
      };
      var chart = new google.visualization.BarChart(document.getElementById("caso_idade"));
      chart.draw(view, options);
  };






      
