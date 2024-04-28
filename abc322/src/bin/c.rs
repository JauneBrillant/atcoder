use proconio::input;

fn main() {
    input! {
        n: usize,
        m: usize,
        a: [usize; m],
    }

    let mut days = vec![false; n];
    for day in a {
        days[day - 1] = true;
    }

    let mut ans = vec![0; n];
    let mut cnt = 0;
    for i in (0..n).rev() {
        cnt += 1;
        if days[i] {
            cnt = 0;
        }
        ans[i] = cnt;
    }

    for v in ans {
        println!("{}", v);
    }
}
