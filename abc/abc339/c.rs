use proconio::input;

fn main() {
    input! {
        n: usize,
        a: [i64; n],
    }

    let mut total = 0;
    for num in a {
        total += num;
        if total < 0 {
            total = 0;
        }
    }
    println!("{}", total);
}
