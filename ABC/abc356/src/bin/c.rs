use proconio::input;

struct Question {
    c: usize,
    a: Vec<usize>,
    r: char,
}

fn main() {
    input! {
        n: usize,
        m: usize,
        k: usize,
    }

    let mut aa = vec![];
    for _ in 0..m {
        input! {
            c: usize,
            a: [usize; c],
            r: char,
        }
        aa.push(Question { c: c, a: a, r: r });
    }

    let mut res = 0;
    'outer: for bit in 0..(1 << n) {
        for q in aa.iter() {
            let mut correct_key_count = 0;
            for &key in q.a.iter() {
                if (bit & (1 << (key - 1))) != 0 {
                    correct_key_count += 1;
                }
            }
            if (q.r == 'o' && correct_key_count < k) || (q.r == 'x' && correct_key_count >= k) {
                continue 'outer;
            }
        }
        res += 1;
    }

    println!("{}", res);
}
