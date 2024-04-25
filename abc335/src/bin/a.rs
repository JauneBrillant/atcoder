use proconio::input;

fn main() {
    input! {
        mut s: String,
    }

    if let Some(last_char) = s.pop() {
        if last_char != '4' {
            s.push('4');
        }
    }
    println!("{}", s);
}
