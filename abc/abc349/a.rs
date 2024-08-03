use proconio::input;

fn main() {
    input! {
        n: usize,
        arr: [i32; n - 1],
    }

    let res: i32 = arr.iter().sum();
    println!("{}", res * -1);
}
