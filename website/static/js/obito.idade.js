    google.charts.load("current", {packages:["corechart"]});
    google.charts.setOnLoadCallback(drawChart);
    function drawChart() {
      var data = google.visualization.arrayToDataTable([
          ['Faixa etária', 'Total', {role: 'style'}],
          ["0 a 9", parseInt(etaria_obt_zero), "#000"],
          ["10 a 19", parseInt(etaria_obt_um), "#000"],
          ["20 a 29", parseInt(etaria_obt_dois), "#000"],
          ["30 a 39", parseInt(etaria_obt_tres), "#000"],
          ['40 a 49', parseInt(etaria_obt_quatro), "#000"],
          ['50 a 59', parseInt(etaria_obt_cinco), "#000"],
          ['60 a 69', parseInt(etaria_obt_seis),"#000"],
          ['70 a 79', parseInt(etaria_obt_sete), "#000"],
          ['80 e mais', parseInt(etaria_obt_oito), "#000"]
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
      var chart = new google.visualization.BarChart(document.getElementById("obito_idade"));
      chart.draw(view, options);
  };