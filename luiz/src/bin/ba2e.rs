use std::env;
use std::error::Error;
use std::fs;
use std::str;

use bioinformatics_algorithms::{pos_to_nt, profile_most_probable, score, Matrix};

pub fn profile_matrix_with_pseudocounts(motifs: &[String], k: usize) -> Matrix {
    let mut matrix: Matrix = vec![vec![0.0; k]; 4];

    for i in 0..k {
        for nt in 0..4 {
            matrix[nt][i] = (motifs
                .iter()
                .filter(|motif| motif.as_bytes()[i] == pos_to_nt(nt))
                .count() as f64
                + 1.)
                / (motifs.len() as f64 + 4.);
        }
    }

    matrix
}

pub fn greedy_motif_search_with_pseudocounts(text: &[&str], k: usize) -> Vec<String> {
    let t = text.len();

    let mut best: Vec<String> = text.iter().map(|motif| motif[..k].into()).collect();
    let mut score_best = score(&best);

    for motif in text[0].as_bytes().windows(k) {
        let mut motifs = vec![String::from_utf8_lossy(motif).into()];
        for j in 1..t {
            let profile = profile_matrix_with_pseudocounts(&motifs, k);
            let motifs_j = profile_most_probable(text[j], k, &profile);
            motifs.push(motifs_j);
        }

        let score_motifs = score(&motifs);
        if score_motifs < score_best {
            best = motifs;
            score_best = score_motifs;
        }
    }

    best.into_iter().map(String::from).collect()
}

fn main() -> Result<(), Box<dyn Error>> {
    let input: String = env::args()
        .nth(1)
        .unwrap_or("data/rosalind_ba2e.txt".into());
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

    for kmer in greedy_motif_search_with_pseudocounts(&text, k) {
        println!("{}", kmer);
    }

    Ok(())
}
