#!/usr/bin/env python3
"""Unit tests for boto3auth."""

import boto3auth


def test_init_class():
    """Test instantiating Boto3Auth class."""
    b3a = boto3auth.Boto3Auth()
    assert b3a.region == 'us-east-1'
    assert b3a.account_id is False
    assert b3a.role is False
    assert b3a.sts is None


def test_init_class_with_region():
    """Test instantiating Boto3Auth class with a region."""
    test_region = 'ca-central-1'
    b3a = boto3auth.Boto3Auth(test_region)
    assert b3a.region == test_region
    assert b3a.account_id is False
    assert b3a.role is False
    assert b3a.sts is None


def test_init_class_with_account_role():
    """Test instantiating Boto3Auth class with an account/role."""
    test_data = {
        'region': 'us-east-1',
        'account_id': '123412341234',
        'role': 'my-cool-role'
    }
    b3a = boto3auth.Boto3Auth(test_data['region'], test_data['account_id'],
                              test_data['role'])
    assert b3a.region == test_data['region']
    assert b3a.account_id == test_data['account_id']
    assert b3a.role == test_data['role']
    assert b3a.sts is None
