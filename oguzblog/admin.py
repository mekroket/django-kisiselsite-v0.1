from django.contrib import admin

# Register your models here.
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date"]    # makalelerdeki ismleri göstermeye yarar
    list_display_links = ["title","created_date"]  #makalelere link vermeye yarar

    search_fields = ["title"]  #makale kısmında arama yapar

    list_filter = ["created_date"]   #Makalede Tarihleri Sıralar

    class Meta:  #Yapılması zorunlu
        model = Article