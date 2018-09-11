#!/usr/bin/env python
'''
Unit tests
'''

from unittest import TestCase
from mock import patch
import project1.authentication as auth

class StandAloneTests(TestCase):
	
	@patch('__builtin__.open')
	def test_login(self, mock_open):
		"""正确的测试"""
		mock_open.return_value.read.return_value = \
		    "netease|password\n"
		self.assertTrue(auth.login('netease', 'password'))
	
#	@patch('__builtin__.open')
	