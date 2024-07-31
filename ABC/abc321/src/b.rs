use proconio::input;

fn main() {
    input! {
        n: usize,
        x: i32,
        mut a: [i32; n - 1],
    }

    let res = (0..=100)
        .filter(|&i| {
            a.push(i);
            let total = a.iter().sum::<i32>();
            let max = *a.iter().max().unwrap();
            let min = *a.iter().min().unwrap();
            a.pop();
            total - (min + max) >= x
        })
        .min()
        .unwrap_or(-1);

    println!("{}", res);
}
