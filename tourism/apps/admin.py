from django.contrib import admin

from .models import City, Tour, Hotel, Customer, BookTour, Author, Blogs, Comments

# Register your models here.

admin.site.register(City)
admin.site.register(Tour)
admin.site.register(Hotel)
admin.site.register(BookTour)
admin.site.register(Blogs)
admin.site.register(Comments)



