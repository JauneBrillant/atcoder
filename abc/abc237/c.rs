use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        s: Chars,
    }

    let mut l = 0;
    let mut r = s.len() - 1;
    loop {
        if l >= r {
            println!("Yes");
            return;
        }

        if s[l] == 'a' && s[r] == 'a' {
            l += 1;
            r -= 1;
        } else if s[r] == 'a' {
            r -= 1;
        } else {
            break;
        }
    }

    let st = (l..=r).map(|i| s[i]).collect::<String>();
    let rev_st = st.chars().rev().collect::<String>();

    println!("{}", if st == rev_st { "Yes" } else { "No" });
}
