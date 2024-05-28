use proconio::input;

fn main() {
    input! {
        n: usize,
    }

    let mut a = vec![];
    let mut t = vec![];
    for _ in 0..n {
        input! {
            ti: usize,
            k: usize,
        }
        t.push(ti);

        let mut ai = vec![];
        for _ in 0..k {
            input! {
                v: usize,
            }
            ai.push(v);
        }
        a.push(ai);
    }

    let mut need = vec![false; n];
    need[n - 1] = true;
    for i in (0..n).rev() {
        if need[i] {
            for &ch in a[i].iter() {
                need[ch - 1] = true;
            }
        }
    }

    let res = need
        .iter()
        .enumerate()
        .filter(|(_, e)| **e)
        .map(|(i, _)| t[i])
        .sum::<usize>();

    println!("{}", res);
}
