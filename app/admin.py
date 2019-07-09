from django.contrib import admin
from django.forms import ModelChoiceField
from django.forms import ModelForm
from django.forms import RadioSelect

from app.models import Coleccion
from app.models import Entry
from app.models import Foto
from app.models import TagEntry
from app.models import Tipo


class TipoAdmin(admin.ModelAdmin):
    list_display = ('idtipo', 'nombre',)
    fields = ('idtipo', 'nombre',)


admin.site.register(Tipo, TipoAdmin)


class TagInline(admin.TabularInline):
    model = TagEntry
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


class FotoInline(admin.TabularInline):
    list_display = ('idfoto', 'handle')
    model = Foto
    extra = 0


class ColeccionAdmin(admin.ModelAdmin):
    fields = ('nombre', 'prompt', 'mensaje_exito', 'mensaje_falla', 'nombre_token',)
    inlines = (FotoInline,)
    list_display = ('nombre',)


admin.site.register(Coleccion, ColeccionAdmin)
