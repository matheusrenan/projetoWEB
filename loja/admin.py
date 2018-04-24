from django.contrib import admin

# Register your models here.
from .models import loja, Categoria, Produto

class profileAdmin(admin.ModelAdmin):
	class Meta:
		model = loja

admin.site.register(loja, profileAdmin)

class categoriaAdmin(admin.ModelAdmin):
	class Meta:
		model = Categoria

admin.site.register(Categoria, categoriaAdmin)

class produtoAdmin(admin.ModelAdmin):
	class Meta:
		model = Produto

admin.site.register(Produto, produtoAdmin)