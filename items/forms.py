from django import forms

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category','name', 'description','price','image',)

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }
    
    def save(self, commit=True):
        instance = super(NewItemForm, self).save(commit=commit)

        if 'image' in self.cleaned_data:
            image = self.cleaned_data['image']

            # Check if the file is an in-memory uploaded file
            if isinstance(image, InMemoryUploadedFile):
                img = Image.open(image)
                img_resized = img.resize((500, 500))

                # Save the resized image back to the in-memory file
                buffer = BytesIO()
                img_resized.save(buffer, format='PNG' if img.format == 'PNG' else 'JPEG')
                instance.image.file = buffer
            else:
                # Open the uploaded image from file
                img = Image.open(image.path)
                img_resized = img.resize((500, 500))

                # Save the resized image back to the file
                img_resized.save(image.path, format='PNG' if img.format == 'PNG' else 'JPEG')

        return instance
    
class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description','price','image','is_sold')

        widgets = {
            
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }
    
    def save(self, commit=True):
        instance = super(EditItemForm, self).save(commit=commit)

        if 'image' in self.cleaned_data:
            image = self.cleaned_data['image']

            # Check if the file is an in-memory uploaded file
            if isinstance(image, InMemoryUploadedFile):
                img = Image.open(image)
                img_resized = img.resize((500, 500))

                # Save the resized image back to the in-memory file
                buffer = BytesIO()
                img_resized.save(buffer, format='PNG' if img.format == 'PNG' else 'JPEG')
                instance.image.file = buffer
            else:
                # Open the uploaded image from file
                img = Image.open(image.path)
                img_resized = img.resize((500, 500))

                # Save the resized image back to the file
                img_resized.save(image.path, format='PNG' if img.format == 'PNG' else 'JPEG')

        return instance
#iamsaikat