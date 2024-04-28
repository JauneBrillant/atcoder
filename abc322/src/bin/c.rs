use proconio::input;

fn main() {
    input! {
        n: usize,
        m: usize,
        a: [usize; m],
    }

    let mut days = vec![false; n];
    for day in &a {
        days[day - 1] = true;
    }

    let mut ans = Vec::with_capacity(n);
    let mut cnt = 0;
    for &is_fire in days.iter().rev() {
        cnt = if is_fire { 0 } else { cnt + 1 };
        ans.push(cnt);
    }

    for v in ans.iter().rev() {
        println!("{}", v);
    }
}
