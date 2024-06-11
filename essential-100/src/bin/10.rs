use proconio::input;

fn main() {
    input! {
        n: usize,
        a: [usize; n],
        q: usize,
        m: [usize; q],
    }

    'outer: for &mi in m.iter() {
        for bit in 0..(1 << n) {
            let bs = format!("{:b}", bit);
            let sums =
                bs.chars().rev().enumerate().fold(
                    0,
                    |acc, (i, e)| {
                        if e == '1' {
                            acc + a[i]
                        } else {
                            acc
                        }
                    },
                );
            if sums == mi {
                println!("Yes");
                continue 'outer;
            }
        }
        println!("No");
    }
}
