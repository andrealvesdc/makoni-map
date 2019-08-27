from django.contrib import admin

from .models import Person
from .models import Endereco
from .models import Photo
from .models import Localization
from .models import Router

# Register your models here.


admin.site.register(Person)
admin.site.register(Endereco)
admin.site.register(Photo)
admin.site.register(Localization)
admin.site.register(Router)
