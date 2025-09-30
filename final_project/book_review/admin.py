from django.contrib import admin

from .models import Author, Book, Review
# Register your models here.


admin.site.register(Author)
admin.site.register(Book)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "book", "added_by", "rating", "created_at")  # shows in list view
    readonly_fields = ("created_at",)  # makes it visible on detail page, but not editable
    list_filter = ("rating", "created_at", "book")  # optional: filters in sidebar
    search_fields = ("content", "book__title", "added_by__username")  # optional: search bar
