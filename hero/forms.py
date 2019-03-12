from django import forms
from hero_upgrade_system.models.occupation import Occupation


class HeroCreateForm(forms.Form):
    name = forms.CharField(max_length=35)
    occupation = forms.ChoiceField(choices=Occupation.OCCUPATIONS)


class StatisticsChangeForm(forms.Form):
    strength = forms.IntegerField(min_value=1, initial=1)
    agility = forms.IntegerField(min_value=1, initial=1)
    intelligence = forms.IntegerField(min_value=1, initial=1)


class AbilitiesChangeForm(forms.Form):
    pass
