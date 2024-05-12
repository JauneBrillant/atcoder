use proconio::input;

fn main() {
    input! {
        n: usize,
        k: usize,
        a: [usize; n],
    }

    let mut res = 1;
    let mut i = 0;
    let mut space = k;
    while i < n {
        if space < a[i] {
            res += 1;
            space = k;
        } 
        space -= a[i];
        i += 1;
    }

    println!("{}", res);
}
