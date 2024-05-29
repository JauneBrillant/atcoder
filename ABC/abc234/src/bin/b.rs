use proconio::input;

fn main() {
    input! {
        n: usize,
        xy: [(i64, i64); n],
    }

    let mut max: f64 = 0.0;
    for i in 0..n {
        for j in 0..n {
            let dis = get_distance(xy[i].0, xy[j].0, xy[i].1, xy[j].1);
            max = max.max(dis);
        }
    }

    println!("{}", max);
}

fn get_distance(x1: i64, x2: i64, y1: i64, y2: i64) -> f64 {
    (((x2 - x1).pow(2) + (y2 - y1).pow(2)) as f64).sqrt()
}
