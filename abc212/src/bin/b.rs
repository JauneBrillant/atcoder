use proconio::input;

fn main() {
    input! {
        pass: String,
    }

    let res = is_weak(&pass);
    println!("{}", if res { "Weak" } else { "Strong" });
}

fn is_weak(pass: &str) -> bool {
    let digit: Vec<_> = pass.chars().map(|e| e.to_digit(10).unwrap()).collect();
    digit.iter().all(|&e| e == digit[0]) || digit.windows(2).all(|e| (e[0] + 1) % 10 == e[1])
}
