from django import forms

from .models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ['content',]
        widget = {
            'content': forms.Textarea(attrs={
                'class': 'w-full py-4 px-4 border rounded-lg focus:outline-none focus:ring-1 focus:ring-blue-600 focus:border-transparent',
                }),
        }