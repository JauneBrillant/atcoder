use proconio::input;

fn main() {
    input! {
        w: usize,
        b: usize,
    }

    let s = "wbwbwwbwbwbw";

    for i in 0..s.len() {
        let mut cnt_w = 0;
        for j in 0..(w + b) {
            if s.chars().nth((i + j) % 12).unwrap() == 'w' {
                cnt_w += 1;
            }
        }
        if w == cnt_w {
            println!("Yes");
            return;
        }
    }

    println!("No");
}
