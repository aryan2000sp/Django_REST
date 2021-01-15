# What are managers?
---

A Manager is the interface through which database query operations are provided to Django models. At least one Manager exists for every model in a Django application. __By default, Django adds a Manager with the name objects to every Django model class.__

Adding extra Manager methods is the preferred way to add “table-level” functionality to your models. (For “row-level” functionality – i.e., functions that act on a single instance of a model object – use Model methods, not custom Manager methods.)

[Click Here To Learn More](https://docs.djangoproject.com/en/3.1/topics/db/managers/)