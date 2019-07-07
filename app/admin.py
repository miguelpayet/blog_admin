from django.contrib import admin
from django.forms import ModelChoiceField
from django.forms import ModelForm
from django.forms import RadioSelect

from app.models import Entry
from app.models import Foto
from app.models import Tag
from app.models import TagFoto
from app.models import Tipo


class TipoAdmin(admin.ModelAdmin):
    list_display = ('idtipo', 'nombre',)
    fields = ('idtipo', 'nombre',)


admin.site.register(Tipo, TipoAdmin)


class TagInline(admin.TabularInline):
    model = Tag
    fields = ('tag',)
    extra = 0


class EntryForm(ModelForm):
    tipo = ModelChoiceField(
        initial=Tipo.BLOG,
        label='Tipo',
        queryset=Tipo.objects.all(),
        widget=RadioSelect(attrs={'class': 'inline'}),
    )

    class Meta:
        model = Entry
        fields = ('titulo', 'handle', 'descripcion', 'tipo',)


class EntryAdmin(admin.ModelAdmin):
    form = EntryForm
    list_display = ('identry', 'titulo', 'tags',)
    inlines = (TagInline,)


admin.site.register(Entry, EntryAdmin)


class TagFotoInline(admin.TabularInline):
    model = TagFoto
    fields = ('tag',)
    extra = 0


class FotoAdmin(admin.ModelAdmin):
    list_display = ('idfoto', 'handle')
    inlines = (TagFotoInline,)


admin.site.register(Foto, FotoAdmin)
