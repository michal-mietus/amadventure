from hero.models.hero import Hero
from artifical.models import mob, location


class MobService:
    def __init__(self, request):
        self.request = request

    def create_mob(self, data):
        """
            This function creates mob only for fight time,
            level and statistics are dynamically created 
            and they depends on user level.
        """
        mob_class = self.get_mob_class(data['mob_class'])
        location = self.get_location(data['location'])
        data['mob_class'] = mob_class
        data['location'] = location
        mob_object = mob.Mob.objects.create(**data)
        mob_object.save()

    def calculate_mob_level(self, mob_difficulty):
        hero_level = self.get_hero().level
        

    def get_hero(self):
        return Hero.objects.get(user__pk=self.request.user.pk)

    def get_mob_class(self, mob_class_name):
        return mob.MobClass.objects.get(name=mob_class_name)

    def get_location(self, location_name):
        return location.Location.objects.get(name=location_name)

