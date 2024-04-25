use proconio::input;

fn main() {
    input! {
        n: usize,
        s: i64,
        k: i64,
        items: [(i64, i64); n],
    }

    let mut total = items.iter().map(|(price, amount)| price * amount).sum::<i64>();
    if total < s { total += k }
    println!("{}", total);
}
