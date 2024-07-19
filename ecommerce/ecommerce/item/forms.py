from django import forms

from .models import Item

INPUT_CLASSES = 'w-1/2 py-2 px-4 border border-gray-300 bg-white rounded-lg text-sm focus:outline-none focus:border-gray-400 focus:ring-2'
#INPUT_CLASSES = 'w-1/2 px-4 py-2 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'name', 'price', 'description', 'image']


        widgets = {
            'category': forms.Select(attrs={'class': INPUT_CLASSES}),
            'name': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'price': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'description': forms.Textarea(attrs={'class': INPUT_CLASSES}),
            'image': forms.FileInput(attrs={'class': INPUT_CLASSES}),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [ 'name', 'price', 'description', 'image', 'is_sold']


        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'price': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'description': forms.Textarea(attrs={'class': INPUT_CLASSES}),
            'image': forms.FileInput(attrs={'class': INPUT_CLASSES}),
        }
