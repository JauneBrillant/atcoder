use proconio::input;

struct Card {
    a: usize,
    c: usize,
    i: usize,
}

fn main() {
    input! {
        n: usize,
    }

    let mut ac = vec![];
    for i in 1..=n {
        input! {
            ai: usize,
            ci: usize,
        }
        ac.push(Card { a: ai, c: ci, i: i });
    }

    ac.sort_by_key(|card| card.c);

    let mut res = vec![];
    let mut v = 0;
    for card in ac {
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
