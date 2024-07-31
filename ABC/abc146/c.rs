use proconio::input;

fn main() {
    input! {
        a: usize,
        b: usize,
        x: usize,
    }

    let mut ok = 0;
    let mut no = 1_000_000_001;
    while ok + 1 != no {
        let mid = (ok + no) / 2;
        if check(mid, a, b, x) {
            ok = mid;
        } else {
            no = mid;
        }
    }

    println!("{}", ok);
}

fn check(n: usize, a: usize, b: usize, x: usize) -> bool {
    let l = n.to_string().len();
    a * n + b * l <= x
}
