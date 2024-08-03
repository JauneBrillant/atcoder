use proconio::input;

fn main() {
    input! {
        n: usize,
        a: [usize; n],
    }

    let mut res = 0;
    for i in 1..=n {
        for j in 1..=a[i - 1] {
            let day = format!("{}{}", i, j);
            let is_all_same = day.chars().all(|c| c == day.chars().next().unwrap());
            res += is_all_same as usize;
        }
    }

    println!("{}", res);
}
