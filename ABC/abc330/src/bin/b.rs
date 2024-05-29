use proconio::input;

fn main() {
    input! {
        n: usize,
        l: usize,
        r: usize,
        arr: [usize; n],
    }

    let mut res = vec![];
    for num in arr {
        if num < l {
            res.push(l);
        } else if l <= num && num <= r {
            res.push(num);
        } else {
            res.push(r);
        }
    }

    for v in res {
        print!("{} ", v);
    }
}
