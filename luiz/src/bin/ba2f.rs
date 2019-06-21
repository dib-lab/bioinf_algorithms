use std::env;
use std::error::Error;
use std::fs;
use std::str;

use rand::distributions::{Distribution, Uniform};

use bioinformatics_algorithms::{profile_matrix, profile_most_probable, score};

pub fn randomized_motif_search(
    text: &[&str],
    k: usize,
    rng: &mut rand::rngs::ThreadRng,
) -> Vec<String> {
    let mut motifs: Vec<String> = text
        .iter()
        .map(|seq| {
            let range = Uniform::from(0..seq.len() - k);
            let rand_pos = range.sample(rng);
            seq[rand_pos..rand_pos + k].into()
        })
        .collect();

    let mut best = motifs.clone(); // TODO avoid this clone // TODO avoid this clone
    let mut score_best = score(&best);

    loop {
        let profile = profile_matrix(&motifs, k);
        motifs = text
            .iter()
            .map(|seq| profile_most_probable(seq, k, &profile))
            .collect();

        let score_motifs = score(&motifs);
        if score_motifs < score_best {
            best = motifs.clone(); // TODO avoid this clone
            score_best = score_motifs
        } else {
            return best.clone(); // TODO avoid this clone
        }
    }
}

pub fn repeated_randomized_motif_search(
    text: &[&str],
    k: usize,
    rng: &mut rand::rngs::ThreadRng,
    times: Option<usize>,
) -> Vec<String> {
    let times = times.unwrap_or(1000);
    let mut best = randomized_motif_search(text, k, rng);
    let mut score_best = score(&best);

    for _ in 1..times {
        let new_best = randomized_motif_search(text, k, rng);
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
        .unwrap_or("data/rosalind_ba2f.txt".into());
    let data = fs::read_to_string(input)?;
    let mut lines = data.lines();

    let mut ints = lines
        .next()
        .unwrap()
        .split(' ')
        .map(|x| x.parse().unwrap())
        .take(2);
    let k = ints.next().unwrap();
    let _t = ints.next().unwrap();

    let text: Vec<&str> = lines.collect();

    let mut rng = rand::thread_rng();

    for kmer in repeated_randomized_motif_search(&text, k, &mut rng, None) {
        println!("{}", kmer);
    }

    Ok(())
}
