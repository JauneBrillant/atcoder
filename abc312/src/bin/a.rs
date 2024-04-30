use proconio::input;

fn main() {
    input! {
        s: String,
    }

    match &s[..] {
        "ACE" | "BDF" | "CEG" | "DFA" | "EGB" | "FAC" | "GBD" => println!("Yes"),
        _ => println!("No"),
    }
}
