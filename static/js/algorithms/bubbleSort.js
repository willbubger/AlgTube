async function bubbleSort(chart, inputArray){
  for(var i = 0; i < inputArray.length; i++){
    for(var j = 0; j < (inputArray.length - 1); j++){
      if(inputArray[j] > inputArray[j+1]){
        var temp = inputArray[j];
        inputArray[j] = inputArray[j+1];
        inputArray[j+1] = temp;
        chart.data.datasets[0].data = inputArray;
        chart.update();
        await sleep(1000);
      }
    }
  }
}