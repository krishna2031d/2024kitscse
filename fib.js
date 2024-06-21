function fibSeries(n){
    let fibSeries=[0,1];
    for(let i=2;i<n;i++){
        fibSeries[i]=fibSeries[i-1]+fibSeries[i-2]
    }
    return fibSeries;
}

let n=10;
let series=fibSeries(n);
console.log("Series:" +series.join(","));