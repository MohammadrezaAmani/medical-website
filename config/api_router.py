from clinic.users.api.v2.urls import router as users_router
from clinic.utils.base import ROUTER as base_router

router = base_router()

router.registry.extend(users_router.registry)
