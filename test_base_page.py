import pytest
from new_post import New_Post
from base_page import Base_Page


@pytest.fixture
def base(request):
    fixture = Base_Page()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_new_post(base):
    base.home_page()
    base.sign_in(user="SomeNewUser", password="secret1")
    base.new_post(New_Post(path="C:/Users/yhurt/image1.png", title="cat and the glass"))
    base.sign_out()


def test_search_by_topic(base):
    base.home_page()
    base.search_by_topic("space")


def test_random_mode(base):
    base.home_page()
    base.random_mode()
