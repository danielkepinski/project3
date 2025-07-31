from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post, Comment
from django.utils import timezone

class PostModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass')
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            body='Test content for post.',
            status=Post.Status.PUBLISHED,
            publish=timezone.now()
        )

    def test_post_str(self):
        self.assertEqual(str(self.post), 'Test Post')

    def test_get_absolute_url(self):
        url = self.post.get_absolute_url()
        self.assertIn('/blog/', url)

class CommentModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass')
        self.post = Post.objects.create(
            title='Another Post',
            slug='another-post',
            author=self.user,
            body='Some body text.',
            status=Post.Status.PUBLISHED,
            publish=timezone.now()
        )
        self.comment = Comment.objects.create(
            post=self.post,
            name='Jane',
            email='jane@example.com',
            body='A test comment'
        )

    def test_comment_str(self):
        self.assertIn('Comment by Jane', str(self.comment))

class PostViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='author', password='pass')
        self.post = Post.objects.create(
            title='View Test',
            slug='view-test',
            author=self.user,
            body='Test body for view',
            status=Post.Status.PUBLISHED,
            publish=timezone.now()
        )

    def test_post_list_view(self):
        response = self.client.get(reverse('blog:post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'View Test')

    def test_post_detail_view(self):
        response = self.client.get(self.post.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)
