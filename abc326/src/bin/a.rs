use proconio::input;

fn main() {
    input! {
        x: usize,
        y: usize,
    }

    if x > y {
        let diff = x - y;
        if diff <= 3 {
            println!("Yes");
        } else {
            println!("No");
        }
    } else {
        let diff = y - x;
        match diff {
        diff <= 2 => println!("Yes");
        _ => println!("No");
        }
        if diff <= 2 {
            println!("Yes");
        } else {
            println!("No");
        }
    }
}
