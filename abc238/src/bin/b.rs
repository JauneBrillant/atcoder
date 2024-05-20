use proconio::input;

fn main() {
    input! {
        n: usize,
        a: [usize; n],
    }

    let mut arr = vec![false; 360];
    let mut curr = 0;
    for ai in a {
        curr += ai;
        curr %= 360;
        arr[curr] = true;
    }

    let mut max_len = 0;
    let mut len = 0;
    for v in arr {
        if v { len = 1 } else { len += 1 }
        max_len = max_len.max(len);
    }

    println!("{}", max_len);
}
