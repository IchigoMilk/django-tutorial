from django.contrib import admin

from .models import Choice, Question

# Questionオブジェクト作成時にChoiceを一通り作成するにはInlineクラスを追加する
# StackedInlineはより幅をとるインラインが使用できる
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

# オプションを変更したいときは、モデルごとにAdminクラスを作って、registerの第二引数に渡す
class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,					{'fields': ['question_text']}),
		('Date Information',	{'fields': ['pub_date']})
	]
	inlines = [ChoiceInline]
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
