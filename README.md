# Amadventure
## Status: in development

Amadventure is a browser game concept where user can create his own hero which must face against monsters in many fantastic locations, accomplish
received quests, gain experience to progress and many more!

### Technical description
Amadventure is created separated applications which are:
- Django application for prototype views and game     structure like models
- Django Rest API to share data with other            systems
- Node server to perform tasks in real time by        usage of socket.io
- Vue.js application for client side actions and      layout

### Features 
- hero
- abilities
- statistics
- locations
- mobs

### In progress
- combat system
- opponents scaling
- quests
- items
- equipment

### Technologies:
- django
- dajngo-rest-framework
- django-cors-headers
- django-rest-framework-braces


### Setup
Initialize database objects.
```
python3 manage.py create_initials
```
