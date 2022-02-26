from django.test import TestCase
from django.urls import reverse
import pytest

def test_homepage_access():
    url = reverse('home')
    assert url == "/"
    