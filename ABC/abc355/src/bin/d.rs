use proconio::input;

pub struct AccumulateVector {
    accum_table: Vec<usize>,
}

impl AccumulateVector {
    pub fn new(v: &[usize]) -> Self {
        let mut accum_table = vec![0; v.len() + 1];
        for i in 0..v.len() {
            accum_table[i + 1] = accum_table[i] + v[i];
        }
        AccumulateVector { accum_table }
    }

    pub fn len(&self) -> usize {
        self.accum_table.len() - 1
    }

    pub fn rank(&self, i: usize) -> usize {
        self.accum_table[i]
    }
}

pub struct WaveletMatrix {
    bit_table: Vec<AccumulateVector>,
    sorted_deduped_v: Vec<usize>,
    accum_table: Vec<AccumulateVector>,
    accum_v: AccumulateVector,
}

impl WaveletMatrix {
    const WAVELET_MATRIX_HEIGHT: usize = 20;

    pub fn new(v: &[usize]) -> Self {
        let mut sorted_deduped_v = v.to_vec();
        sorted_deduped_v.sort_unstable();
        sorted_deduped_v.dedup();

        let mut compress = v
            .iter()
            .map(|&x| sorted_deduped_v.partition_point(|&y| y < x))
            .collect::<Vec<_>>();

        let mut bit_table = vec![];
        let mut accum_table = vec![];
        for i in (0..WaveletMatrix::WAVELET_MATRIX_HEIGHT).rev() {
            bit_table.push(AccumulateVector::new(
                &compress.iter().map(|&x| (x >> i) & 1).collect::<Vec<_>>(),
            ));

            accum_table.push(AccumulateVector::new(
                &compress
                    .iter()
                    .map(|&x| {
                        if (x >> i) & 1 == 0 {
                            sorted_deduped_v[x]
                        } else {
                            0
                        }
                    })
                    .collect::<Vec<_>>(),
            ));
            compress = compress
                .iter()
                .filter(|&x| (x >> i) & 1 == 0)
                .chain(compress.iter().filter(|&x| (x >> i) & 1 == 1))
                .cloned()
                .collect::<Vec<_>>();
        }

        let accum_v = AccumulateVector::new(v);

        WaveletMatrix {
            bit_table,
            sorted_deduped_v,
            accum_table,
            accum_v,
        }
    }

    pub fn count_less_than(&self, mut l: usize, mut r: usize, upper: usize) -> usize {
        if r <= l {
            return 0;
        }

        let upper = self.sorted_deduped_v.partition_point(|&x| x < upper);
        let mut res = 0;

        for (i, bit) in (0..Self::WAVELET_MATRIX_HEIGHT)
            .rev()
            .zip(self.bit_table.iter())
        {
            if (upper >> i) & 1 == 0 {
                l = l - bit.rank(l);
                r = r - bit.rank(r);
            } else {
                res += (r - l) - (bit.rank(r) - bit.rank(l));
                l = bit.rank(l) + (bit.len() - bit.rank(bit.len()));
                r = bit.rank(r) + (bit.len() - bit.rank(bit.len()));
            }
        }

        res
    }

    pub fn count(&self, l: usize, r: usize, lower: usize, upper: usize) -> usize {
        if r <= l {
            return 0;
        }

        self.count_less_than(l, r, upper) - self.count_less_than(l, r, lower)
    }
}

fn main() {
    input! {
        n: usize,
        mut lr: [(usize, usize); n],
    }

    lr.sort();

    let wm = WaveletMatrix::new(&lr.iter().map(|x| x.0).collect::<Vec<_>>());

    let mut ans = 0;
    for l in 0..n {
        ans += wm.count(l + 1, n, 0, lr[l].1 + 1);
    }
    println!("{}", ans);
}
