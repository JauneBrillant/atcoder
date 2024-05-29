use proconio::input;

fn main() {
    input! {
        k: usize,
    }

    let binary_string = format!("{:b}", k);
    let res: String = binary_string
        .chars()
        .map(|c| if c == '1' { '2' } else { c })
        .collect();

    println!("{}", res);
}
