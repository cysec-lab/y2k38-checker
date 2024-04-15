# !/bin/bash

# 概要: リポジトリの一覧を取得し、JSON ファイルに保存する。
# sh fetch_repo_list.sh ghp_XXXX
# 事前条件: GitHub Personal Access Token (ghp_から始まる) を取得しておくこと。

# Search repositories | GitHub Rest API Documentation
# https://docs.github.com/en/rest/search/search?apiVersion=2022-11-28#search-repositories

max_star=2000
min_star=1000
page=1
file_name=$page.json

curl -X GET \
    -H "Accept: application/vnd.github+json" \
    -H "Authorization: Bearer $1" \
    -H "X-GitHub-Api-Version: 2022-11-28" \
    "https://api.github.com/search/repositories?q=language:C&stars:$min_star..$max_star&sort=stars&order=desc&per_page=100&page=$page" \
    >./$file_name