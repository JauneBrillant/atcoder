use proconio::input;

fn main() {
    input! {
        n: usize,
        mut a: [usize; n],
    }

    a.sort();
    let max = a[a.len() - 1];
    let mut second_max = 0;
    for i in (0..a.len()).rev() {
        if max != a[i] {
            second_max = a[i];
            break;
        }
    }

    println!("{}", second_max);
}
