async function insertionSort(chart, inputArray) {
    for (let i = 1; i < inputArray.length; i++) {
        let key = inputArray[i];
        let j = i - 1;

        while (j >= 0 && inputArray[j] > key) {
            inputArray[j + 1] = inputArray[j];
            j = j - 1;

            chart.data.datasets[0].data = [...inputArray];
            chart.update();
            await sleep(1000);
        }

        inputArray[j + 1] = key;

        chart.data.datasets[0].data = [...inputArray];
        chart.update();
        await sleep(1000);
    }
}