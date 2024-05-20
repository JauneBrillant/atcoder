use proconio::input;

#[derive(Debug)]
struct Card {
    a: usize,
    c: usize,
    i: usize,
}

fn main() {
    input! {
        n: usize,
    }
    
    let mut acs = vec![];
    for i in 0..n {
        input! {
            ai: usize,
            ci: usize,
        }
        let aci = Card {a: ai, c: ci, i: i + 1};
        acs.push(aci);
    }
    
    acs.sort_by_key(|aci| aci.c);

    let mut res = vec![];
    let mut v = 0;
    for card in acs.iter() {
        if card.a > v {
            v = card.a;
            res.push(card.i);
        }
    }

    res.sort();
    println!("{}", res.len());
    for v in res {
        print!("{} ", v);
    }
}

