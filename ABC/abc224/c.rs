use itertools::Itertools;
use proconio::input;

fn main() {
    input! {
        n: usize,
        xy: [(i64, i64); n],
    }

    let res = xy
        .iter()
        .tuple_combinations()
        .map(|(xy1, xy2, xy3)| {
            let (x1, y1) = xy1;
            let (x2, y2) = xy2;
            let (x3, y3) = xy3;
            (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
        })
        .filter(|v| *v != 0)
        .count();

    println!("{}", res);
}
