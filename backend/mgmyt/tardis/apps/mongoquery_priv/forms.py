from django import forms

class QueryForm(forms.Form):
    #collection_name = forms.CharField(label='Collection name:', max_length=100)
    #query_text = forms.CharField(label='Enter your query:', max_length=500)
    query_text = forms.CharField(label='Enter your query:', widget=forms.Textarea)
