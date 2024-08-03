use proconio::input;

fn main() {
    input! {
        n: usize,
        q: [i32; n],
        a: [i32; n],
        b: [i32; n],
    }

    let mut res = 0;
    let mut a_amt = 0;
    loop {
        let mut r = vec![0; n];
        for i in 0..n {
            r[i] = q[i] - a[i] * a_amt as i32;
        }

        let not_ok = r.iter().any(|&e| e < 0);
        if not_ok {
            break;
        }

        let mut b_amt = i32::MAX;
        for i in 0..n {
            if b[i] == 0 {
                continue;
            };

            b_amt = b_amt.min(r[i] / b[i]);
        }

        res = res.max(a_amt + b_amt);
        a_amt += 1;
    }

    println!("{}", res);
}
