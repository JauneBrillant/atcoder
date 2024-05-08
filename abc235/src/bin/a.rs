use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        x: Chars,
    }
    
    let a = x[0].to_digit(10).unwrap();
    let b = x[1].to_digit(10).unwrap();
    let c = x[2].to_digit(10).unwrap();

    let abc = convert(a, b, c);
    let bca = convert(b, c, a);
    let cab = convert(c, a, b);

    println!("{}", abc + bca + cab);
}

fn convert(a: u32, b: u32, c: u32) -> usize {
    let mut res = 0;
    res += 100 * a;
    res += 10 * b;
    res += 1 * c;
    res as usize
}
