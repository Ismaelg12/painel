 google.charts.load('current', {'packages':['bar']});
      google.charts.setOnLoadCallback(drawStuff);

      function drawStuff() {
        var data = new google.visualization.arrayToDataTable([
          ['Casos', 'Total'],
          ["Suspeitos",suspeito],
          ["Descartados", descartado],
          ["Confirmados", confirmado],
          ["Alta Médica", isolado],
          ["Óbitos", obito],
          ["Crônicos", cronico],
          ["Isolamento Domiciliar", isolado],
          ["Internados", internado],
          ["Internados em UTI", uti]
        ]);
        var options = {
          title: '',
          legend: { position: 'none' },
          
          bars: 'vertical', // Required for Material Bar Charts.
          axes: {
            x: {
              0: { side: 'top', label: ''} // Top x-axis.
            }
          },
          bar: { groupWidth: "100%" }
        };

        var chart = new google.charts.Bar(document.getElementById('todos_casos'));
        chart.draw(data, options);
      };

      