#! /usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import mock


_timestamp = "2019-07-27 19:14:19.872839"


def _construct_expected_published_date(published_date):
    expected_published_date = published_date.replace(" ", "T")
    expected_published_date += 'Z'
    return expected_published_date


MockedDateTime = mock.MagicMock(
    return_value="2019-07-27 19:14:19.872839",
    timezoned=_construct_expected_published_date(_timestamp)
)
