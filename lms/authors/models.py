from django.db import models

# Create your models here.
class Author(models.Model):
    # id = models.UUIDField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    image = models.ImageField(upload_to="author_images/", default="defaults/default_author.jpg")

    # class Meta:
    #     table_name = "authors"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

 