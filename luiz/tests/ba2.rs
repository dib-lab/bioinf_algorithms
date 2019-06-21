use std::io::Write;
use std::process::Command;

use assert_cmd::prelude::*;
use predicates::str::contains;
use tempfile::NamedTempFile;

use bioinformatics_algorithms::score;

#[test]
fn ba2a_test() -> Result<(), Box<std::error::Error>> {
    let mut file = NamedTempFile::new()?;
    writeln!(
        file,
        "3 1
ATTTGGC
TGCCTTA
CGGTATC
GAAAATT"
    )?;

    let mut cmd = Command::cargo_bin("ba2a")?;
    cmd.arg(file.path());
    cmd.assert().success();

    for kmer in &["ATA", "ATT", "GTT", "TTT"] {
        cmd.assert().stdout(contains(*kmer));
    }

    Ok(())
}

#[test]
fn ba2c_test() -> Result<(), Box<std::error::Error>> {
    let mut file = NamedTempFile::new()?;
    writeln!(
        file,
        "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT
5
0.2 0.2 0.3 0.2 0.3
0.4 0.3 0.1 0.5 0.1
0.3 0.3 0.5 0.2 0.4
0.1 0.2 0.1 0.1 0.2"
    )?;

    let mut cmd = Command::cargo_bin("ba2c")?;
    cmd.arg(file.path());
    cmd.assert().success().stdout("CCGAG\n");

    Ok(())
}

#[test]
fn ba2d_test() -> Result<(), Box<std::error::Error>> {
    let mut file = NamedTempFile::new()?;
    writeln!(
        file,
        "3 5
GGCGTTCAGGCA
AAGAATCAGTCA
CAAGGAGTTCGC
CACGTCAATCAC
CAATAATATTCG"
    )?;

    let mut cmd = Command::cargo_bin("ba2d")?;
    cmd.arg(file.path());
    cmd.assert().success().stdout(
        "CAG
CAG
CAA
CAA
CAA
",
    );

    Ok(())
}

#[test]
fn ba2e_test() -> Result<(), Box<std::error::Error>> {
    let mut file = NamedTempFile::new()?;
    writeln!(
        file,
        "3 5
GGCGTTCAGGCA
AAGAATCAGTCA
CAAGGAGTTCGC
CACGTCAATCAC
CAATAATATTCG"
    )?;

    let mut cmd = Command::cargo_bin("ba2e")?;
    cmd.arg(file.path());
    cmd.assert().success().stdout(
        "TTC
ATC
TTC
ATC
TTC
",
    );

    Ok(())
}

#[test]
fn ba2f_test() -> Result<(), Box<std::error::Error>> {
    let mut file = NamedTempFile::new()?;
    writeln!(
        file,
        "8 5
CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA
GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG
TAGTACCGAGACCGAAAGAAGTATACAGGCGT
TAGATCAAGTTTCAGGTGCACGTCGGTGAACC
AATCCACCAGCTCCACGTGCAATGTTGGCCTA"
    )?;

    let mut cmd = Command::cargo_bin("ba2f")?;
    cmd.arg(file.path());
    cmd.assert().success();

    let best_score = score(&[
        "TCTCGGGG".into(),
        "CCAAGGTG".into(),
        "TACAGGCG".into(),
        "TTCAGGTG".into(),
        "TCCACGTG".into(),
    ]);

    let motifs: Vec<String> = String::from_utf8_lossy(&cmd.assert().get_output().stdout)
        .lines()
        .map(String::from)
        .collect();
    let new_score = score(&motifs);

    assert!(new_score <= best_score + 1);

    Ok(())
}

#[test]
fn ba2g_test() -> Result<(), Box<std::error::Error>> {
    let mut file = NamedTempFile::new()?;
    writeln!(
        file,
        "8 5 100
CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA
GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG
TAGTACCGAGACCGAAAGAAGTATACAGGCGT
TAGATCAAGTTTCAGGTGCACGTCGGTGAACC
AATCCACCAGCTCCACGTGCAATGTTGGCCTA"
    )?;

    let mut cmd = Command::cargo_bin("ba2g")?;
    cmd.arg(file.path());
    cmd.assert().success();

    let best_score = score(&[
        "TCTCGGGG".into(),
        "CCAAGGTG".into(),
        "TACAGGCG".into(),
        "TTCAGGTG".into(),
        "TCCACGTG".into(),
    ]);

    let motifs: Vec<String> = String::from_utf8_lossy(&cmd.assert().get_output().stdout)
        .lines()
        .map(String::from)
        .collect();
    let new_score = score(&motifs);

    dbg!((best_score, new_score));
    assert!(new_score <= best_score + 1);

    Ok(())
}
