use std::io::Write;
use std::process::Command;

use assert_cmd::prelude::*;
use predicates::prelude::*;
use predicates::str::contains;
use tempfile::NamedTempFile;

#[test]
fn ba1a_test() -> Result<(), Box<std::error::Error>> {
    let mut file = NamedTempFile::new()?;
    writeln!(file, "GCGCG\nGCG")?;

    let mut cmd = Command::cargo_bin("ba1a")?;
    cmd.arg(file.path());

    cmd.assert().success().stdout("2\n");

    Ok(())
}

#[test]
fn ba1b_test() -> Result<(), Box<std::error::Error>> {
    let mut file = NamedTempFile::new()?;
    writeln!(file, "ACGTTGCATGTCGCATGATGCATGAGAGCT\n4")?;

    let mut cmd = Command::cargo_bin("ba1b")?;
    cmd.arg(file.path());

    cmd.assert()
        .success()
        .stdout(contains("CATG").and(contains("GCAT")));
    Ok(())
}

#[test]
fn ba1c_test() -> Result<(), Box<std::error::Error>> {
    let mut file = NamedTempFile::new()?;
    writeln!(file, "AAAACCCGGT\n")?;

    let mut cmd = Command::cargo_bin("ba1c")?;
    cmd.arg(file.path());

    cmd.assert().success().stdout("ACCGGGTTTT\n");
    Ok(())
}

#[test]
fn ba1d_test() -> Result<(), Box<std::error::Error>> {
    let mut file = NamedTempFile::new()?;
    writeln!(file, "ATAT\nGATATATGCATATACTT\n")?;

    let mut cmd = Command::cargo_bin("ba1d")?;
    cmd.arg(file.path());

    cmd.assert().success().stdout("1 3 9 \n");
    Ok(())
}

#[test]
fn ba1e_test() -> Result<(), Box<std::error::Error>> {
    let mut file = NamedTempFile::new()?;
    writeln!(file, "CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC\n5 75 4")?;

    let mut cmd = Command::cargo_bin("ba1e")?;
    cmd.arg(file.path());
    cmd.assert().success();

    for kmer in &["CGACA", "GAAGA", "AATGT"] {
        cmd.assert().stdout(contains(*kmer));
    }

    Ok(())
}

#[test]
fn ba1f_test() -> Result<(), Box<std::error::Error>> {
    let mut file = NamedTempFile::new()?;
    writeln!(file, "CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG")?;

    let mut cmd = Command::cargo_bin("ba1f")?;
    cmd.arg(file.path());

    cmd.assert().success().stdout("53 97 \n");

    Ok(())
}

#[test]
fn ba1g_test() -> Result<(), Box<std::error::Error>> {
    let mut file = NamedTempFile::new()?;
    writeln!(file, "GGGCCGTTGGT\nGGACCGTTGAC")?;

    let mut cmd = Command::cargo_bin("ba1g")?;
    cmd.arg(file.path());

    cmd.assert().success().stdout("3\n");

    Ok(())
}

#[test]
fn ba1h_test() -> Result<(), Box<std::error::Error>> {
    let mut file = NamedTempFile::new()?;
    writeln!(file, "ATTCTGGA\nCGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC\n3")?;

    let mut cmd = Command::cargo_bin("ba1h")?;
    cmd.arg(file.path());

    cmd.assert().success().stdout("6 7 26 27 78 \n");

    Ok(())
}

#[test]
fn ba1i_test() -> Result<(), Box<std::error::Error>> {
    let mut file = NamedTempFile::new()?;
    writeln!(file, "ACGTTGCATGTCGCATGATGCATGAGAGCT\n4 1")?;

    let mut cmd = Command::cargo_bin("ba1i")?;
    cmd.arg(file.path());
    cmd.assert().success();

    for kmer in &["GATG", "ATGC", "ATGT"] {
        cmd.assert().stdout(contains(*kmer));
    }

    Ok(())
}

#[test]
fn ba1j_test() -> Result<(), Box<std::error::Error>> {
    let mut file = NamedTempFile::new()?;
    writeln!(file, "ACGTTGCATGTCGCATGATGCATGAGAGCT\n4 1")?;

    let mut cmd = Command::cargo_bin("ba1j")?;
    cmd.arg(file.path());
    cmd.assert()
        .success()
        .stdout(contains("ATGT").and(contains("ACAT")));

    Ok(())
}
