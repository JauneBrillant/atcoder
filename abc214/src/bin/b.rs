use proconio::input;

fn main() {
    input! {
        s: usize,
        t: usize,
    }

    let mut res = 0;
    for i in 0..= s {
        for j in 0..= s - i {
            for k in 0..= s - i - j {
                if i * j * k <= t {
                    res += 1;
                }
            }
        }
    }

    println!("{}", res);
}
