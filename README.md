# Kata Baku Checker for PO File

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/209d0abd94964e0380c2ed897acd052d)](https://app.codacy.com/app/berviantoleo/Kata-Baku-Checker-for-PO-File?utm_source=github.com&utm_medium=referral&utm_content=berviantoleo/Kata-Baku-Checker-for-PO-File&utm_campaign=Badge_Grade_Settings)

## Build Status

| Travis | Github Action - Docker | Python Package |
|:------:|:----------------------:|:--------------:|
| [![Build Status](https://travis-ci.com/bervProject/Kata-Baku-Checker-for-PO-File.svg?branch=master)](https://travis-ci.com/bervProject/Kata-Baku-Checker-for-PO-File) | ![Docker](https://github.com/bervProject/Kata-Baku-Checker-for-PO-File/workflows/Docker/badge.svg) | ![Upload Python Package](https://github.com/bervProject/Kata-Baku-Checker-for-PO-File/workflows/Upload%20Python%20Package/badge.svg) |

## Usage

```bash
  python check.py -i [Input File] -t po
```

### Docker Image & Docker Compose

#### Build

```bash
docker-compose build
```

#### Running

```bash
docker-compose run console python check.py -i example/id.po -t po
```

## Forked from

This project forked from [Indonesian Kata Baku Checkr](https://github.com/turfaa/IndonesianKataBakuChecker)

## Data Example Source

From Geany Repository.

## LICENSE

```markdown
MIT License

Copyright (c) 2018 Bervianto Leo Pratama

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```
