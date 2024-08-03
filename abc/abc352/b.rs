use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        s: Chars,
        t: Chars,
    }

    let mut si = 0;
    let mut ti = 0;
    let mut res = vec![];
    while si < s.len() && ti < t.len() {
        if s[si] == t[ti] {
            res.push(ti + 1);
            si += 1;
            ti += 1;
        } else {
            ti += 1;
        }
    }

    for v in res {
        print!("{} ", v);
    }
}
