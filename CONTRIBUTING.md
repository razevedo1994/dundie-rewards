# Contributing to Dundie Project

Summary of project

## Guidelines

- Backwards compatibility
- Multiplatform
- Python 3 only

## Code of Conduct

- Be gentle

## How to contribute

### Fork repository

- Click fork button on [github repo](https://github.com/...)

### Clone to local dev environment

```bash
git clone https://github.com/seunome/...

```

### Prepare virtual env

```bash
cd dundie-rewards
make virtualenv
make install
```

### Coding style

- This project follows PEP8

### Run tests

```bash
make test
```

### Commit rules

- We follow conventional commit messages ex: `[bugfix] reason #issue`
- We require signed commits

### Pull request rules

- We require all tests to be passing