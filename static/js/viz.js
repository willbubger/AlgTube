let chart = null;

//source: https://stackoverflow.com/questions/16873323/javascript-sleep-wait-before-continuing updated using AI
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function testInput(algFn){ 
  var input = document.getElementById("searchValues").value;
  var inputArray = input.split(",");
  for(var i = 0; i < inputArray.length; i++){
    inputArray[i] = parseInt(inputArray[i]);
  }
    if (chart !== null) {
    chart.destroy();
  }
  chart = createTable(inputArray, algFn);
  
  await algFn(chart, inputArray);
}

function createTable(inputArray, algFn){
  var yValues = inputArray;
  var xValues = [];
  for (var i = 0; i < inputArray.length; i++){
    xValues[i] = i; 
  }

  var chart = new Chart("myChart", {
      type: "bar",
      data: {
        labels: xValues,
        datasets: [{
          data: yValues
        }]
      },
      options: {
        animation: false,
        legend: {display: false},
        title: {
          display: true,
          text: algFn.name
        }
      }
    });

    return chart;
}