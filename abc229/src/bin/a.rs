use proconio::input;

fn main() {
    input! {
        s1: String,
        s2: String,
    }

    match (s1.as_str(), s2.as_str()) {
        ("#.", ".#") => println!("No"),
        (".#", "#.") => println!("No"),
        (_, _) => println!("Yes"),
    }
}
