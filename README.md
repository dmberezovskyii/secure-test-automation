# About
`secure-test-autmation` Python library for encrypting and decrypting passwords, designed for integration with automated testing frameworks such as Selenium, Appium, Playwright, and others. It ensures secure password storage and allows retrieving keys from remote  or local vaults to decrypt configuration files and passwords.

## Features

- **Encryption and Decryption**: Encrypt and decrypt passwords using a Fernet key.
- **Key Management**: Support for loading, creating, saving, and deleting encryption keys from a local file and remove vault
- **Password Generation**: Generate secure, random passwords of a specified length.
- **Multiple Vault Types**: 
  - Currently: local and and [HashiCorp Vault](https://portal.cloud.hashicorp.com/sign-in)

## Documentation

You can find the full documentation for Secure Test Automation here:
[Secure Test Automation Documentation](https://secure-test-automation.readthedocs.io/en/latest/index.html)


## Requirements

- Python 3.10 +
- `cryptography` library for encryption/decryption functionality.

Install the required dependencies:

### Local Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/dmberezovskyii/secure-test-automation
   ```
2. Install required dependencies:
   ```bash
   pip install poetry
   poetry shell
   poetry env info
   copy `Executable: path to virtual env` -> Add Interpreter -> Poetry Environment -> Existing environment -> add Executable -> Apply
   poetry install
   ```
### Install Library
   ```bash
   pip install secure-test-automation
   ```
### TODO add documentation usage
