use proconio::input;

fn main() {
    input! {
        m: usize,
        d: usize,
        mut year: usize,
        mut month: usize,
        mut day: usize,
    }

    // 年末
    if month == m && day == d {
        println!("{} {} {}", year + 1, 1, 1);
    }
    // 月末
    else if day == d {
        println!("{} {} {}", year, month + 1, 1);
    }
    // その他
    else {
        println!("{} {} {}", year, month, day + 1);
    }
}
