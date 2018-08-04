from tastypie.resources import ModelResource
from api.models import Fleet
from tastypie.authorization import Authorization


class FleetResource(ModelResource):
    class Meta:
        queryset = Fleet.objects.all()
        resource_name = 'fleet'
        authorization = Authorization()

