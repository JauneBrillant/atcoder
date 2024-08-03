use proconio::input;

fn main() {
    input! {
        n: usize,
        coordinates: [(f64, f64); n],
    }


    for i in 0..n {
        let mut max_distance = 0.0;
        let mut max_distance_point = i;
        for j in 0..n {
            let distance = get_distance(coordinates[i], coordinates[j]);
            if max_distance < distance {
                max_distance = distance;
                max_distance_point = j;
            }
        }
        println!("{}", max_distance_point + 1);
    }
}

fn get_distance((x1, y1): (f64, f64), (x2, y2): (f64, f64)) -> f64 {
    ((x1 - x2).powf(2.0) + (y1 - y2).powf(2.0)).sqrt()
}
