import pytest
import requests
from unittest import mock

from src.gh_bot.auth import authenticate_with_github_api


def test_authenticate_with_github_api_successful():
    expected_response = {'login': 'my-username', 'name': 'My Name'}

    with mock.patch.object(requests, 'get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = expected_response

        response = authenticate_with_github_api('my-token')

        mock_get.assert_called_once_with(
            'https://api.github.com/user',
            headers={'Authorization': 'token my-token'}
        )
        assert response == expected_response


def test_authenticate_with_github_api_failure():
    with mock.patch.object(requests, 'get') as mock_get:
        mock_get.return_value.status_code = 401

        response = authenticate_with_github_api('my-token')

        mock_get.assert_called_once_with(
            'https://api.github.com/user',
            headers={'Authorization': 'token my-token'}
        )
        assert response is None
