from django.urls import path
from app.views import *

urlpatterns = [
    path('',index),
    path('viewTransactions/',viewTransactions),
    path('frequentItems/',frequentItems),
    path('rules/',rules),
    path('document/',document),
    path('addTransactions/',addTransactions),

]
