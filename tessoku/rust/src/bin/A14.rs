use proconio::input;

fn main() {
    input! {
       n: usize,
       k: usize,
       a: [usize; n],
       b: [usize; n],
       c: [usize; n],
       d: [usize; n],
    }

    let mut p = vec![];
    for av in a.iter() {
        for bv in b.iter() {
            p.push(av + bv);
        }
    }

    let mut q = vec![];
    for cv in c.iter() {
        for dv in d.iter() {
            q.push(cv + dv);
        }
    }

    q.sort();
    for pv in p.iter() {
        if let Ok(_) = q.binary_search(&(k - pv)) {
            println!("Yes");
            return;
        }
    }

    println!("No");
}
