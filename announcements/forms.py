fromdjangoimportforms
from.modelsimportAnnouncement
classAnnouncementForm(forms.ModelForm):
    classMeta:
        model=Announcement
        fields=["title","message"]
        widgets = {
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "message":forms.Textarea(attrs={"class":"form-control","rows":4}),
        }
