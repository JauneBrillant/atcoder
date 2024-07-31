use proconio::input;

fn main() {
    input! {
        n: usize,
        m: usize,
        mut a: [usize; n],
        b: [usize; m],
    }

    for &bi in b.iter() {
        if let Some(idx) = a.iter().position(|&ai| ai == bi) {
            a.remove(idx);
        } else {
            println!("No");
            return;
        }
    }

    println!("Yes");
}
