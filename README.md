# GitHub Availability Report Analysis

This repository includes the result of analyzing GitHub Availability Report. This program aims to collect realistic failure scenario for my study.

The original data source is GitHub Tech Blog as below.

https://github.blog/tag/github-availability-report/

## Usage

```
python -m venv env
. env/bin/activate
pip install BeautifulSoup4 requests
python crawl.py
```

## Prerequisite

```
$ python --version
Python 3.12.2
```


## Summary

```
ggrep -RoP -h '\(lasting [^)]+' results/* | gsed -e 's/(lasting //g' -e 's/for //g' | perl -pe 'BEGIN { %m = (one=>1, two=>2, three=>3, four=>4, five=>5, six=>6, seven=>7, eight=>8, nine=>9) } s/\b(one|two|three|four|five|six|seven|eight|nine)\b/$m{lc($1)}/g' - | gsed 's/and //g' | tr -d ,
```
