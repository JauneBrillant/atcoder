use proconio::input;

fn main() {
    input! {
        n: usize,
        m: usize,
        s: [String; n],
        t: [String; m],
    }

    let mut i = 0;
    let mut j = 0;
    while i < n && j < m {
        if s[i] == t[j] {
            println!("Yes");
            i += 1;
            j += 1;
        } else {
            println!("No");
            i += 1;
        }
    }
}
