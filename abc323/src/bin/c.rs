use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        n: usize,
        m: usize,
        a: [usize; m],
        s: [Chars; n],
    }

    let mut totals = vec![];
    for (i, string) in s.iter().enumerate() {
        let total: usize = string.iter().enumerate()
            .filter(|&(_, &c)| c == 'o')
            .map(|(j, _)| a[j])
            .sum();
        totals.push(total + i + 1);
    }

    let mx = *totals.iter().max().unwrap();
    for i in 0..n {
        let mut remain = vec![];
        for j in 0..m {
            if s[i][j] == 'x' {
                remain.push(a[j]);
            }
        }
        remain.sort_by(|a, b| a.cmp(b));

        let mut res = 0;
        while totals[i] < mx {
            totals[i] += remain.pop().unwrap();
            res += 1;
        }
        println!("{}", res);
    }
}
