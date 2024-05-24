use proconio::{input, marker::Chars};

fn main() {
    input! {
        n: usize,
        mut s: Chars,
        q: usize,
        cd: [(char, char); q],
    }

    let mut az = ('a'..='z').collect::<Vec<char>>();
    for (c, d) in cd {
        for i in 0..26 {
            if az[i] == c {
                az[i] = d;
            }
        }
    }

    for i in 0..n {
        s[i] = az[s[i] as usize - 'a' as usize];
    }

    println!("{}", s.iter().collect::<String>());
}
