import unittest

import datetime

from rauth.service import OAuth1Service


class TestApi(unittest.TestCase):
    """Twitter API test"""
    def setUp(self):
        self.auth = OAuth1Service(
            name='hardtail_python',
            consumer_key='JpU9Lb1PEpFtLgC7XOlkw',
            consumer_secret='k6TsCWbybimpcBMhi8o5simuuoX3XjoMGtG5Ij9U',
            request_token_url='https://api.twitter.com/oauth/request_token',
            access_token_url='https://api.twitter.com/oauth/access_token',
            authorize_url='https://api.twitter.com/oauth/authorize')
        self.access_token = {
            'access_token': '132108032-vQ58uSC6HE0IOOMtmZcRjjko4gbykAOmDF4Vg3tI',
            'access_token_secret': 'Q2uMS4NvwPhAs6BthJ19ImdYCixXmxfUos1B76D4'}
        self.endpoint = 'https://api.twitter.com/1.1/{path}.json'

    def test_get_rate_limit_status(self):
        """application/rate_limit_status test"""
        response = self.auth.get(
            self.endpoint.format(path='application/rate_limit_status'),
            **self.access_token)
        content = response.content
        limit = content['resources']['search']['/search/tweets']['limit']
        self.assertEqual(180, limit)

    def test_post_statuses_update(self):
        """statuses/update test"""
        text = 'test {now}'.format(now=datetime.datetime.now())
        params = {'status': text}
        response = self.auth.post(
            self.endpoint.format(path='statuses/update'),
            params=params,
            **self.access_token)
        content = response.content
        self.assertEqual(text.decode('utf-8'), content['text'])

if __name__ == '__main__':
    unittest.main()
