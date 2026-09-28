# mdformat-presenterm

A simple mdformat plugin to format [presenterm](https://github.com/mfontanini/presenterm) slides.

## Features

- [ ] Keep presenterm slide titles (`foo\n===`) instead of replacing them with `# foo`

Yes, this plugin is very simple.
Further features like list numbering or keeping the YAML metadata are required for presenterm to work properly, but they are out of scope for me as other tools do this job already (see below). 

## Usage

I myself use this plugin via the following pre-commit hook:

```yaml
repos:
- repo: https://github.com/hukkin/mdformat
  rev: 1.0.0
  hooks:
  - id: mdformat
    args:
      # keep lists numbered in plain text
      - --number
    additional_dependencies:
      # keep YAML metadata blocks
      - mdformat-front-matters
      # format tables
      - mdformat-gfm
      # this plugin (make sure to keep version up to date)
      - git+https://github.com/p-fruck/mdformat-presenterm@v0.1.0
```
