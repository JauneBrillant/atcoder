use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {
        s1: Chars,
        s2: Chars,
    }

    let mut cnt = 0;
    for i in 0..2 {
        if s1[i] == '#' {
            cnt += 1;
        }
        if s2[i] == '#' {
            cnt += 1;
        }
    }

    if cnt == 2 && s1[0] == '#' && s2[1] == '#' || cnt == 2 && s1[1] == '#' && s2[0] == '#' {
        println!("No");
    } else {
        println!("Yes");
    }
}
