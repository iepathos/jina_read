# Jina Read

A simple Python script to fetch and save markdown content from Jina AI URLs.

## Description

This script reads URLs from standard input, fetches the corresponding markdown content from Jina AI's servers, and saves them as individual markdown files in a `markdown_outputs` directory.

## Prerequisites

- Python 3.x
- Poetry (Python dependency management)

## Setup

1. Install Poetry if you haven't already:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Install dependencies:
```bash
poetry install
```

3. Create a `.env` file in the same directory as the script and add your Jina AI token:
```
JINA_TOKEN=your_token_here
```

## Usage

Run the script using Poetry:

1. Pipe a file containing URLs:
```bash
cat file-with-links.txt | poetry run python jina_read/jina_read.py
```

2. Or manually input URLs and press Ctrl+D when finished:
```bash
poetry run python jina_read/jina_read.py
url1
url2
^D
```
