#!/usr/bin/env python3
# coding=utf-8
from theHarvester.discovery import linkedinsearch
import pytest
import os
import re



class TestGetLinks(object):

    def test_get_links(self):
        search = linkedinsearch.SearchLinkedin("facebook.com", '100')
        search.process()
        links = search.get_links()
        assert list(links)

    def test_links_linkedin(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        mock_response = open(dir_path + "/test_linkedin_links.txt").read()
        reg_links = re.compile(r"url=https:\/\/www\.linkedin.com(.*?)&")
        temp = reg_links.findall(mock_response)
        resul = []
        for regex_item in temp:
            stripped_url = regex_item.replace("url=", "")
            resul.append("https://www.linkedin.com" + y)
        assert set(resul)


if __name__ == '__main__':
    pytest.main()
