use proconio::input;

fn main() {
    input! {
        n: usize,
        h: [i32; n],
    }

    let i = h.iter().enumerate().find(|(_, &v)|  h[0] < v).map(|(i, _)| i);
    if let Some(index) = i {
        println!("{}", index + 1);
    } else {
        println!("{}", -1);
    }
}
