use proconio::input;

fn main() {
    input! {
        mut s: String,
    }

    if let Some(_) = s.pop() { s.push('4') }
    println!("{}", s);
}
