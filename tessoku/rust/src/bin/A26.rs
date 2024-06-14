use proconio::input;

fn main() {
    input! {
        n: usize,
        x: [usize; n],
    }

    let max_val = *x.iter().max().unwrap();
    let mut eratosthenes = vec![true; max_val + 1];
    eratosthenes[0] = false;
    eratosthenes[1] = false;

    for i in 2.. {
        if i * i > max_val {
            break;
        }

        if eratosthenes[i] {
            let mut curr = i;
            while curr + i <= max_val {
                curr += i;
                eratosthenes[curr] = false;
            }
        }
    }

    for &xi in x.iter() {
        if eratosthenes[xi] {
            println!("Yes");
        } else {
            println!("No");
        }
    }
}
