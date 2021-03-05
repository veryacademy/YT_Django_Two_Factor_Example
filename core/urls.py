import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from two_factor.urls import urlpatterns as tf_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("store.urls", namespace="store")),
    path("basket/", include("basket.urls", namespace="basket")),
    path("payment/", include("payment.urls", namespace="payment")),
    path("", include(tf_urls)),
    path("account/", include("account.urls", namespace="account")),
    path("orders/", include("orders.urls", namespace="orders")),
    path("__debug__/", include(debug_toolbar.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
