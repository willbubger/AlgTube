//source: https://www.geeksforgeeks.org/dsa/heap-sort/
async function heapify(chart, inputArray, n, i) {
    let largest = i;
    let l = 2 * i + 1;
    let r = 2 * i + 2;

    if (l < n && inputArray[l] > inputArray[largest]) {
        largest = l;
    }

    if (r < n && inputArray[r] > inputArray[largest]) {
        largest = r;
    }

    if (largest !== i) {
        [inputArray[i], inputArray[largest]] = [inputArray[largest], inputArray[i]];

        chart.data.datasets[0].data = [...inputArray];
        chart.update();
        await sleep(1000);

        await heapify(chart, inputArray, n, largest);
    }
}

async function heapSort(chart, inputArray) {
    let n = inputArray.length;

    for (let i = Math.floor(n / 2) - 1; i >= 0; i--) {
        await heapify(chart, inputArray, n, i);
    }

    for (let i = n - 1; i > 0; i--) {
        [inputArray[0], inputArray[i]] = [inputArray[i], inputArray[0]];

        chart.data.datasets[0].data = [...inputArray];
        chart.update();
        await sleep(1000);

        await heapify(chart, inputArray, i, 0);
    }
}