from django.db import models
from django.contrib import auth
# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=50, help_text="The name of the Publisher")
    website = models.URLField(help_text="Publisher's Website")
    email = models.EmailField(help_text="Publisher's email Address ")

    def __str__(self):
        return self.name


class Book(models.Model):
    """A Published Book"""
    title = models.CharField(max_length=70, help_text="Title Of the Book")
    publication_date = models.DateField(verbose_name="Date the Book was published")
    isbn = models.CharField(max_length=20, verbose_name="ISBN number of the book")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField('Contributor', through="BookContributor")

    def __str__(self):
        return self.title


class Contributor(models.Model):
    """A contributor to a book, e.g. author, editor, co-author"""
    first_name = models.CharField(max_length=50, help_text="Contributor's first name")
    last_name = models.CharField(max_length=50, help_text="Contributor's last name")
    email = models.EmailField(help_text="Contact email for Contributor")

    def __str__(self):
        return self.first_name


class BookContributor(models.Model):
    class ContributionRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co_Author"
        EDITOR = "EDITOR", "Editor"

    book = models.ForeignKey(Book , on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor , on_delete=models.CASCADE)
    role = models.CharField(verbose_name="The role this contributor had in the book", choices=ContributionRole.choices, max_length=20)


class Review(models.Model):
    content = models.TextField(help_text="The Review text")
    rating = models.IntegerField(help_text="The rating reviewer has given")
    date_created = models.DateTimeField(auto_now_add=True, help_text="The data and time the review was created")
    date_edited = models.DateTimeField(null=True, help_text="Last edited")
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book , on_delete=models.CASCADE, help_text="Book that this review is for")