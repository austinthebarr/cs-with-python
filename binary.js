// Bisection Search
// e: element your looking for
// a: array your searching through
const bisectionSearch = (e, a) => {
    let low = 0;
    let t = a.length - 2;
    let high = a[t];

    while (a[low] <= a[high]) {
        let ans = Math.round((high + low) / 2);
        if (a[ans] === e) {
            return a[ans];
        } else if (a[ans] < e) {
            low = ans + 1;
        } else  {
            high = ans - 1;
        } 
    }
    return null;
}


console.log(bisectionSearch(7, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))