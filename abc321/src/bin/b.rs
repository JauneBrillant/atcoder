use proconio::input;

fn main() {
    input! {
        n: usize,
        x: i32,
        a: [i32; n - 1],
    }

    let mut res = i32::MAX;
    for i in 0..=100 {
        let mut arr = a.clone();
        arr.push(i);

        let total = arr.iter().sum::<i32>();
        let min = *arr.iter().min().unwrap();
        let max = *arr.iter().max().unwrap();

        if total - (max + min) >= x {
            res = res.min(i);
        }
    }

    if res == i32::MAX {
        println!("{}", -1)
    } else {
        println!("{}", res);
    }
}
