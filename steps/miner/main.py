# -*- coding: utf-8 -*-
import codecs
import os
import time
import urllib.parse
import logging

from datetime import datetime, timedelta

from requests.utils import requote_uri

from config import headers

from core.Parser import Parser
from core.sendRequest import requestPage

import constants

os.system('cls' if os.name == 'nt' else 'clear')
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

logger = logging.getLogger(__name__)


DAYS=120
class GitMiner(object):
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s -   %(message)s',
                        datefmt='%m/%d/%Y %H:%M:%S',
                        level=logging.INFO)
    def __init__(self):
        self.seen_links = set()
        # query = urllib.parse.quote(f"amazon.awscdk language:java")
        # self.search_term = requote_uri(f"/search/code?q={query}&per_page=100")
        query = urllib.parse.quote(f"aws cdk created:FROM_DATE..TO_DATE language:java")
        self.search_term = requote_uri(f"/search/repositories?q={query}&per_page=100")
        self.std_search = [
                    "aws cdk in:description",
                    "aws cdk in:readme",
                    "aws cdk"
                ]
        self.queries =  {
            "java": {
               "repositories": self.std_search,
               "code": self.create_paths("software.amazon.awscdk")
            },
            "typescript": {
                "repositories": self.std_search,
                "code":  self.create_paths("aws-cdk-lib")
            },
            "go": {
                "repositories": self.std_search,
                "code":  self.create_paths("aws-cdk-go")
            },
            "python": {
                "repositories": self.std_search,
                "code":  self.create_paths("aws_cdk")
            },
            "javascript": {
                "repositories": self.std_search,
                "code":  self.create_paths("aws-cdk-go")
            }
        }

    def create_paths(self, term):
        return [
                    f"{term}",
                    f"{term} path:/main/",
                    f"{term} path:/src/",
                    f"{term} path:/main/",
                    f"{term} path:/test/",
                    f"{term} path:/package/",
                    f"{term} path:/code/",
                    f"{term} path:/internal/",
                    f"{term} path:/public/",
                    f"{term} path:/private/",
                    f"{term} path:/pkg/",
                ]

    def persist_repos(self, repos, file):
        logger.info("peristing repos %d ", len(repos))
        for link in repos:
            if file is not None:
                file.write(link)
                file.write('\n')
                file.flush()


    def save_repos(self, data, file, retries):

        def map_to_repo(item):
            if "repository" in item: return item['repository']['html_url']
            else: return item['html_url']
        if retries >= 3:
            return False
        logger.info("total repo %d" , len(data["items"]))
        if not "items" in data:
            return self.save_repos(data, file, retries + 1)
        repo_links = map(map_to_repo, data['items'])
        repo_links_filtered = []
        for link in repo_links:
            if not link in self.seen_links:
                self.seen_links.add(link)
                repo_links_filtered.append(link)
        self.persist_repos(repo_links_filtered, file)
        return True

    def logError(self, message):
        with open('errors.txt', 'a') as file:
            file.write(message)
            file.write("\n")
            file.flush()

    def search_page(self, url_search, headers_github, output_file):
        for i in range(1, constants.MAX_PAGE):
            try:
                data, status = requestPage(url_search + "&page=" + str(i), headers_github )
                logger.info("status %s", status)
                if status == "OK":
                    if len(data["items"]) == 0:
                        logger.info("No results jumping")
                        break
                    repos_saved = self.save_repos(data, output_file, 0)
                    if not repos_saved:
                       self.logError(f'error saving repos from page {i}')
                else:
                    logger.info("Page failed  %d", i)
                    break
                time.sleep(10)
            except:
                logger.info("Error in page %d for search term  $s", i, url_search )
                self.logError(f'error saving repos from page {i} in search {url_search}')


    def send_query(self, headers_github, output_file, language):
        for search_type in self.queries[language]:
            for search_term in self.queries[language][search_type]:
                logger.info("searching for %s %s %s", search_type, search_term, language)
                time.sleep(5)
                if search_type == 'repositories':
                    for d in range(2):
                        url_search = self.build_url(search_type, search_term,  language, d)
                        logger.info("searching for %s", url_search)
                        self.search_page(url_search, headers_github, output_file)
                else:
                    url_search = self.build_url(search_type, search_term, language)
                    self.search_page(url_search, headers_github, output_file )

    def build_url(self,search_type, search_term, language, days_passes=0):
        query = search_term
        if search_type == 'repository':
            offset = 15
            bottom = datetime.today() - timedelta(days=days_passes * offset)
            top = bottom + timedelta(days=offset)
            bottom_str = bottom.strftime("%Y-%m-%d")
            top_str = top.strftime("%Y-%m-%d")
            query += f" created:{bottom_str}..{top_str}"
        query += f" language:{language}"
        logger.info(query)
        query = urllib.parse.quote(query, safe='')
        query = requote_uri(f"/search/{search_type}?q={query}&per_page=100")
        return Parser.GITHUB_URL + query

    def start(self):
        url_search = Parser.GITHUB_URL + self.search_term
        #url_search = "https://api.github.com/search/code?q=aws-sdk"
        #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
        #
        headers_github = headers.get_headers(url_search)
        headers_github['Accept'] = 'application/vnd.github+json'
        headers_github['X-GitHub-Api-Version'] = '2022-11-28'
        headers_github['Authorization'] = f'Bearer {constants.BEARER_TOKEN}'


        for language in self.queries:
            filename = f"{constants.RESULTS_OUTPUT}/{language}-repos.csv"
            with open(filename, 'a') as file:
                self.parser = Parser(headers_github, file)
                self.send_query(headers_github, file, language)
        return
GitMiner().start()

