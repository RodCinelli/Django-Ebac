import pytest
from blog.factories import PostFactory

@pytest.fixture
def draft_post():
    """Fixture que cria um post com status rascunho"""
    return PostFactory(status=0, title='draft post')

@pytest.fixture
def published_post():
    """Fixture que cria um post com status publicado"""
    return PostFactory(status=1, title='published post')

@pytest.mark.django_db
class TestPostStatus:
    def test_create_draft_post(self, draft_post):
        """Testa a criação de um post como rascunho"""
        assert draft_post.status == 0
        assert draft_post.title == 'draft post'

    def test_create_published_post(self, published_post):
        """Testa a criação de um post como publicado"""
        assert published_post.status == 1
        assert published_post.title == 'published post'

    def test_change_post_status(self, draft_post):
        """Testa a mudança de status de um post"""
        draft_post.status = 1
        draft_post.save()
        assert draft_post.status == 1