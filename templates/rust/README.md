# Rust Template

Copy these files to your Rust project:

```
.
├── Cargo.toml
├── Cargo.lock (gitignore this)
├── src/
│   └── main.rs
└── tests/
    └── integration_test.rs
```

## Usage

```bash
# Run tests
cargo test

# Run linter
cargo clippy

# Format code
cargo fmt

# Build
cargo build --release
```

## Cargo.toml Template

```toml
[package]
name = "my-project"
version = "0.1.0"
edition = "2021"

[dependencies]
```

See https://doc.rust-lang.org/cargo/ for more details.
