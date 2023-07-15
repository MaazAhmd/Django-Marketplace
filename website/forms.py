from django import forms

from .models import Item

# INPUTCLASSES = 'w-full py-2 px-5 rounded-xl border'
INPUTCLASSES = "w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-2 px-3 leading-8 transition-colors duration-200 ease-in-out"

class addItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image', 'brand')
        widgets = {
            'category': forms.Select(attrs={
                'class': "w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-2 px-3 leading-8 transition-colors duration-200 ease-in-out"
            }),
            'description': forms.Textarea(attrs={
                'class': "w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 h-32 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out"
            }),
            'name': forms.TextInput(attrs={
                'class': "w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
            }),
            'price': forms.TextInput(attrs={
                'class': INPUTCLASSES
            }),
            'image': forms.FileInput(attrs={
                # 'class': "w-full rounded border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out"
                'class': INPUTCLASSES
            }),
            'brand': forms.TextInput(attrs={
                'class': INPUTCLASSES
            }),
        }


class editItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'brand')
        widgets = {
            'description': forms.Textarea(attrs={
                'class': "w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 h-32 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out"
            }),
            'name': forms.TextInput(attrs={
                'class': "w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
            }),
            'price': forms.TextInput(attrs={
                'class': INPUTCLASSES
            }),
            'image': forms.FileInput(attrs={
                # 'class': "w-full rounded border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out"
                'class': INPUTCLASSES
            }),
            'brand': forms.TextInput(attrs={
                'class': INPUTCLASSES
            }),
        }