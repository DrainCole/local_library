from django.contrib import admin

# Register your models here.
from catalog.models import Author, Genre, Book, BookInstance, Language


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra=0

 
# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

class BooksInline(admin.TabularInline):
    model = Book
    extra=0

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]

@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
	list_display = ('status', 'due_back', 'borrower', 'id')
	list_filter = ('status', 'due_back')
	fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'borrower', 'due_back')
        }),
    )

admin.site.register(Language)
admin.site.register(Genre)