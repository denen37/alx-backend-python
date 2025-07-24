#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from unittest.mock import patch, MagicMock
from utils import access_nested_map, get_json, memoize


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
        ('http://example.com', {"payload": True}),
        ('http://holberton.io', {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, url, payload, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = payload
        mock_get.return_value = mock_response

        result = get_json(url)

        self.assertEqual(payload)
        mock_get.assert_called_once_with(url)



class TestClass:
    def a_method(self):
        return 42

    @memoize
    def a_property(self):
        return self.a_method()
    

class TestMemoize(unittest.TestCase):
    @patch('__main__.TestClass.a_method') 
    def test_memoize(self, mock_method):
        mock_method.return_value = 42

        obj = TestClass()
        result1 = obj.a_property
        result2 = obj.a_property

        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)

        mock_method.assert_called_once()

if __name__ == '__main__':
    unittest.main()