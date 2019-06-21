use std::env;
use std::error::Error;
use std::fs;
use std::str;

type Matrix = Vec<Vec<f64>>;

pub fn kmer_prob(kmer: &[u8], matrix: &Matrix) -> f64 {
    let mut prob = 1.;
    for (i, nt) in kmer.iter().enumerate() {
        let pos = match nt {
            b'A' => 0,
            b'C' => 1,
            b'G' => 2,
            b'T' => 3,
            _ => unimplemented!(),
        };
        prob = prob * matrix[pos][i];
    }

    prob
}

pub fn profile_most_probable(text: &str, k: usize, matrix: &Matrix) -> String {
    let mut most_probable_kmer = text[0..k].as_bytes();
    let mut max_prob = kmer_prob(most_probable_kmer, matrix);

    for kmer in text[1..].as_bytes().windows(k) {
        let prob = kmer_prob(kmer, matrix);
        if prob > max_prob {
            max_prob = prob;
            most_probable_kmer = kmer
        }
    }

    String::from_utf8_lossy(most_probable_kmer).into()
}

fn main() -> Result<(), Box<dyn Error>> {
    let input: String = env::args()
        .nth(1)
        .unwrap_or("data/rosalind_ba2c.txt".into());
    let data = fs::read_to_string(input)?;
    let mut lines = data.lines();

    let text: String = lines.next().unwrap().into();
    let k = lines.next().unwrap().parse()?;

    let mut matrix: Matrix = vec![vec![0.0; k]; 4];

    for i in 0..4 {
        lines
            .next()
            .unwrap()
            .split(' ')
            .map(|x| x.parse().unwrap())
            .take(k)
            .enumerate()
            .map(|(j, x)| matrix[i][j] = x)
            .count();
    }

    println!("{}", profile_most_probable(&text, k, &matrix));

    Ok(())
}
