from django import forms

from .models import Review_Entity


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review_Entity
        fields = ('rid', 'hid', 'Review_Date', 'Reviewer_Nationality', 'Positive_Review', 'Negative_Review','Review_Total_Positive_Word_Counts', 'Review_Total_Negative_Word_Counts', 'Total_Number_of_Reviews_Reviewer_Has_Given','Reviewer_Score', 'Tags' )
