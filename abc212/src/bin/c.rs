use proconio::input;

fn main() {
    input! {
        n: usize,
        m: usize,
        mut a: [i32; n],
        mut b: [i32; m],
    }

    a.sort();
    b.sort();

    let mut ai = 0;
    let mut bi = 0;
    let mut res = i32::MAX;
    while ai < n && bi < m {
        let diff = (a[ai] - b[bi]).abs();
        res = res.min(diff);
        if a[ai] < b[bi] { ai += 1 } else { bi += 1 }
    }

    println!("{}", res);
}
