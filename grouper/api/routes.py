from .handlers import Users, Groups, Permissions, Stats, NotFound
from ..constants import NAME_VALIDATION, PERMISSION_VALIDATION

HANDLERS = [

    (r"/users", Users),
    (r"/users/{}".format(NAME_VALIDATION), Users),

    (r"/groups", Groups),
    (r"/groups/{}".format(NAME_VALIDATION), Groups),

    (r"/permissions", Permissions),
    (r"/permissions/{}".format(PERMISSION_VALIDATION), Permissions),

    (r"/debug/stats", Stats),

    (r"/.*", NotFound),

]
