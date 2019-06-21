use std::env;
use std::error::Error;
use std::fs;
use std::str;

use rand::distributions::{Distribution, Uniform};
use rand::rngs::ThreadRng;

use bioinformatics_algorithms::{profile_matrix_with_pseudocounts, profile_most_probable, score};

pub fn gibbs_sampler(text: &[&str], k: usize, n: usize, rng: &mut ThreadRng) -> Vec<String> {
    let mut motifs: Vec<String> = text
        .iter()
        .map(|seq| {
            let range = Uniform::from(0..seq.len() - k);
            let rand_pos = range.sample(rng);
            seq[rand_pos..rand_pos + k].into()
        })
        .collect();

    let mut best = motifs.clone(); // TODO avoid this clone
    let mut score_best = score(&best);

    for _ in 0..n {
        let range = Uniform::from(0..text.len() - 1);
        let i = range.sample(rng);

        let mut motif_subset = motifs.clone();
        motif_subset.swap_remove(i);

        let profile = profile_matrix_with_pseudocounts(&motif_subset, k);
        motifs[i] = profile_most_probable(text[i], k, &profile);

        let score_motifs = score(&motifs);
        if score_motifs < score_best {
            best = motifs.clone(); // TODO avoid this clone
            score_best = score_motifs
        }
    }

    best
}

pub fn repeated_gibbs_sampler(
    text: &[&str],
    k: usize,
    n: usize,
    rng: &mut ThreadRng,
    times: Option<usize>,
) -> Vec<String> {
    let times = times.unwrap_or(20);
    let mut best = gibbs_sampler(text, k, n, rng);
    let mut score_best = score(&best);

    for _ in 1..times {
        let new_best = gibbs_sampler(text, k, n, rng);
        let new_score = score(&new_best);
        if new_score < score_best {
            best = new_best;
            score_best = new_score;
        }
    }

    best
}

fn main() -> Result<(), Box<dyn Error>> {
    let input: String = env::args()
        .nth(1)
        .unwrap_or("data/rosalind_ba2g.txt".into());
    let data = fs::read_to_string(input)?;
    let mut lines = data.lines();

    let mut ints = lines
        .next()
        .unwrap()
        .split(' ')
        .map(|x| x.parse().unwrap())
        .take(3);
    let k = ints.next().unwrap();
    let _t = ints.next().unwrap();
    let n = ints.next().unwrap();

    let text: Vec<&str> = lines.collect();

    let mut rng = rand::thread_rng();

    for kmer in repeated_gibbs_sampler(&text, k, n, &mut rng, None) {
        println!("{}", kmer);
    }

    Ok(())
}
