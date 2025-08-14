from django.test import TestCase
from django.urls import reverse

from .models import Book

# Create your tests here.
class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Django for APIs",
            subtitle="DRF",
            author="William S. Vincent",
            isbn="1234567891011",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "Django for APIs")
        self.assertEqual(self.book.subtitle, "DRF")
        self.assertEqual(self.book.author, "William S. Vincent")
        self.assertEqual(self.book.isbn, "1234567891011")

    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "DRF")
        self.assertTemplateUsed(response, "books/book_list.html")