use proconio::input;

fn main() {
    input! {
        n: usize,
        ta: [(char, i64); n],
    }

    let div = 10000;

    let mut res = 0;
    for (t, a) in ta.iter() {
        match t {
            '+' => res += a,
            '-' => res -= a,
            '*' => res *= a,
            _ => (),
        }

        if res < 0 {
            res += div;
        }
        res %= div;

        println!("{}", res);
    }
}
