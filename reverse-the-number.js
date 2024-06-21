let n = 1234;
let r = 0;
while(n > 0) {
    r = (r * 10) + n % 10;
    n = parseInt(n / 10);
}
console.log(r);