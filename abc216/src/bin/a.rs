use proconio::input;

fn main() {
    input! {
        s: String,
    }

    let parts = s.trim().split('.').collect::<Vec<_>>();
    let x: usize = parts[0].parse().unwrap();
    let y: usize = parts[1].parse().unwrap();

    match y {
        0..=2 => println!("{}-", x),
        3..=6 => println!("{}", x),
        7..=9 => println!("{}+", x),
        _ => (),
    }
}
