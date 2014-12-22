from django import forms


class SearchForm(forms.Form):
    oponent1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'@twitter-name'}))
    oponent2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'@twitter-name'}))





# from django import forms

# class ContactForm(forms.Form):
#     subject = forms.CharField(max_length=100)
#     message = forms.CharField(widget=forms.Textarea)
#     sender = forms.EmailField()
#     cc_myself = forms.BooleanField(required=False)

# Rendering fields manually
# We don’t have to let Django unpack the form’s fields; we can do it manually 
# if we like (allowing us to reorder the fields, for example). 
# Each field is available as an attribute of the form using {{ form.name_of_field }},
#  and in a Django template, will be rendered appropriately. For example:

# {{ form.non_field_errors }}
# <div class="fieldWrapper">
#     {{ form.subject.errors }}
#     <label for="{{ form.subject.id_for_label }}">Email subject:</label>
#     {{ form.subject }}
# </div>
# <div class="fieldWrapper">
#     {{ form.message.errors }}
#     <label for="{{ form.message.id_for_label }}">Your message:</label>
#     {{ form.message }}
# </div>
# <div class="fieldWrapper">
#     {{ form.sender.errors }}
#     <label for="{{ form.sender.id_for_label }}">Your email address:</label>
#     {{ form.sender }}
# </div>
# <div class="fieldWrapper">
#     {{ form.cc_myself.errors }}
#     <label for="{{ form.cc_myself.id_for_label }}">CC yourself?</label>
#     {{ form.cc_myself }}
# </div>
# Complete <label> element can also be generated using the label_tag(). For example:

# <div class="fieldWrapper">
#     {{ form.subject.errors }}
#     {{ form.subject.label_tag }}
#     {{ form.subject }}
# </div>