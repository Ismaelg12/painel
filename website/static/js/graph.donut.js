$(function () {
	// Óbitos por Sexo

	var donutChartCanvas = $('#obitosSe').get(0).getContext('2d')
    var donutData        = {
      labels: [
          'Masculino (%)', 
          'Feminino (%)',
      ],
      datasets: [
        {
          data: [(obito_sexo_m/obito)*100,(obito_sexo_f/obito)*100],
          backgroundColor : ['#00a65a', '#f56954'],borderColor: "#dddddd"
        }
      ]
    }
    var donutOptions     = {
      maintainAspectRatio : false,
      responsive : true,
    }
    //Create pie or douhnut chart
    // You can switch between pie and douhnut using the method below.
    var donutChart = new Chart(donutChartCanvas, {
      type: 'doughnut',
      data: donutData,
      options: donutOptions      
    })


// Confirmados por Sexo
    var donutChartCanvas = $('#confSe').get(0).getContext('2d')
    var donutData        = {
      labels: [
          'Masculino (%)', 
          'Feminino (%)',

      ],
      datasets: [
        {
          data: [(conf_sexo_m/confirmado)*100,(conf_sexo_f/confirmado)*100],
          backgroundColor : ['#00a65a', '#f56954'],
        }
      ]
    }
    var donutOptions     = {
      maintainAspectRatio : false,
      responsive : true,
    }
    //Create pie or douhnut chart
    // You can switch between pie and douhnut using the method below.
    var donutChart = new Chart(donutChartCanvas, {
      type: 'doughnut',
      data: donutData,
      options: donutOptions      
    })

// Recuperados por Sexo
      
  })

