from django import forms
from hero_upgrade_system.models.occupation import Occupation
from hero_upgrade_system.models.ability import Ability


class HeroCreateForm(forms.Form):
    name = forms.CharField(max_length=35)
    occupation = forms.ChoiceField(choices=Occupation.OCCUPATIONS)


class StatisticsChangeForm(forms.Form):
    strength = forms.IntegerField(min_value=1, initial=1)
    agility = forms.IntegerField(min_value=1, initial=1)
    intelligence = forms.IntegerField(min_value=1, initial=1)


class AbilitiesChangeForm(forms.Form):
    def __init__(self, fields_names, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in fields_names:
            self.fields[field_name] = forms.IntegerField(min_value=0, label=field_name)
