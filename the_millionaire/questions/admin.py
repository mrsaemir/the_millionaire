from django.contrib import admin

from .models import Question, QuestionOption


class QuestionInline(admin.StackedInline):
    model = QuestionOption
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    inlines = (QuestionInline,)
    list_display = ('title', 'score')

    def get_form(self, request, obj=None, **kwargs):
        form = super(QuestionAdmin, self).get_form(request, obj, **kwargs)

        if obj:
            form.base_fields['answer']._queryset = QuestionOption.objects.filter(question=obj) # noqa
        else:
            form.base_fields['answer']._queryset = QuestionOption.objects.none() # noqa

        return form


admin.site.register(Question, QuestionAdmin)
