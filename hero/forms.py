from django import forms
from hero.models.occupation import Occupation
from hero.models.ability import Ability


class HeroCreateForm(forms.Form):
    name = forms.CharField(max_length=35)
    occupation = forms.ChoiceField(choices=Occupation.OCCUPATIONS)


class HeroStatisticsChangeForm(forms.Form):
    def __init__(self, fields_names_and_min_values, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, min_value in fields_names_and_min_values.items():
            self.fields[field_name] = forms.IntegerField(min_value=min_value, label=field_name)

class AbilitiesChangeForm(forms.Form):
    def __init__(self, fields_names_and_min_values, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, min_value in fields_names_and_min_values.items():
            self.fields[field_name] = forms.IntegerField(min_value=min_value, label=field_name)
