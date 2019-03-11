from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .models.hero import Hero
from .forms import HeroCreateForm


class HeroCreateView(FormView):
    form_class = HeroCreateForm
    template_name = 'hero/hero_create.html'
    success_url = reverse_lazy('hero:hero')

    def form_valid(self, form):
        Hero.objects.create(

        )
        return super().form_valid(form)
