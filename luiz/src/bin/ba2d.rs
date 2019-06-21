use std::collections::HashMap;
use std::env;
use std::error::Error;
use std::fs;
use std::str;

use bioinformatics_algorithms::{hamming, profile_most_probable, Matrix};

#[inline]
fn pos_to_nt(pos: usize) -> u8 {
    match pos {
        0 => b'A',
        1 => b'C',
        2 => b'G',
        3 => b'T',
        _ => unimplemented!(),
    }
}

pub fn profile_matrix(motifs: &[String], k: usize) -> Matrix {
    let mut matrix: Matrix = vec![vec![0.0; k]; 4];

    for i in 0..k {
        for nt in 0..4 {
            matrix[nt][i] = motifs
                .iter()
                .filter(|motif| motif.as_bytes()[i] == pos_to_nt(nt))
                .count() as f64
                / motifs.len() as f64;
        }
    }

    matrix
}

pub fn score(motifs: &[String]) -> u64 {
    let size = motifs[0].len();
    let mut common_kmer: String = "".into();

    for i in 0..size {
        let mut max_freq = 0;
        let mut pos_freq: HashMap<u8, u64> = HashMap::default();

        for motif in motifs {
            let nt = motif.as_bytes()[i];
            let entry = pos_freq.entry(nt).or_insert(0);
            *entry += 1;
            max_freq = u64::max(max_freq, *entry);
        }

        for (nt, freq) in pos_freq {
            if freq == max_freq {
                common_kmer.push(nt as char);
                break;
            }
        }
    }

    motifs
        .iter()
        .map(|kmer| hamming(&common_kmer, kmer) as u64)
        .sum()
}

pub fn greedy_motif_search(text: &[&str], k: usize) -> Vec<String> {
    let t = text.len();

    let mut best: Vec<String> = text.iter().map(|motif| motif[..k].into()).collect();
    let mut score_best = score(&best);

    for motif in text[0].as_bytes().windows(k) {
        let mut motifs = vec![String::from_utf8_lossy(motif).into()];
        for j in 1..t {
            let profile = profile_matrix(&motifs, k);
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
        .unwrap_or("data/rosalind_ba2d.txt".into());
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

    for kmer in greedy_motif_search(&text, k) {
        println!("{}", kmer);
    }

    Ok(())
}
