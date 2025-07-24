#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from unittest.mock import patch, MagicMock
import utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
       ({"a": 1}, ("a",), 1),
       ({"a": {"b": 2}}, ("a",), {"b": 2}),
       ({"a": {"b": 2}}, ("a", "b"), 2),
   ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    
    @parameterized.expand([
       ({}, ("a",)),
       ({"a": 1}, ("a", "b"))
   ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ('http://example.com', 'payload', True),
        ('http://holberton.io', 'payload', False)
    ])
    @patch('__main__.requests.get')
    def test_get_json(self, url, key, value, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {key: value}
        mock_get.return_value = mock_response

        result = get_json(url)

        self.assertEqual(result[key], value)
        mock_get.assert_called_once_with(url)


if __name__ == '__main__':
    unittest.main()