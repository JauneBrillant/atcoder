use proconio::input;

fn main() {
    input! {
        a: f32,
        b: f32,
        c: f32,
    }

    let res = ((a / c).ceil()) as i32 * c as i32;
    println!("{}", if res <= b as i32 { res } else { -1 });
}
