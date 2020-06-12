// Bubble sort

const bubbleSort = (list) => {
    // Set swap to false to run while loop
    let swap = false;
    while (!swap) {
        /*
        Set swap to true to break the loop if for loop finds digits in order
        */
        swap = true;
        for (let i = 0; i < list.length; i++) {
            //save elements to swap
            let currE = list[i];
            let nextE = list[i + 1];
            if (currE > nextE) {
                list[i] = nextE;
                list[i + 1] = currE;
                // Set swap to false since we still have elements out of the order
                swap = false;
            }

        }
    }

    return list;
}


console.log(bubbleSort([7, 9, 2, 1, 10, 3]))