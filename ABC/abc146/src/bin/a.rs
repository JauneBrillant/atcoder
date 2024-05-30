use proconio::input;

fn main() {
    input! {
        s: String,
    }

    let mut res = 0;
    match s.as_str() {
        "SUN" => res += 7,
        "MON" => res += 6,
        "TUE" => res += 5,
        "WED" => res += 4,
        "THU" => res += 3,
        "FRI" => res += 2,
        "SAT" => res += 1,
        _ => (),
    }

    println!("{}", res);
}
