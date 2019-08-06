import xadmin
from .models import Frank

class FrankAdmin(object):
    pass
xadmin.site.register(Frank, FrankAdmin)
