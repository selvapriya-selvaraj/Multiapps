"""
URL configuration for multapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
def home(request):
    return HttpResponse("""
        <h1>Welcome to Multi-App Django Project</h1>
        <h2>Available Apps</h2>
        <a href="/accounts/">Accounts</a><br><br>
        <a href="/products/">Products</a><br><br>
        <a href="/orders/">Orders</a>
    """)

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <html>
    <head>
        <title>Multi App Django</title>
        <style>
            body {
                font-family: Arial;
                text-align: center;
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
                padding-top: 80px;
            }

            h1 {
                font-size: 45px;
            }

            .container {
                display: flex;
                justify-content: center;
                gap: 25px;
                margin-top: 50px;
            }

            a {
                text-decoration: none;
                color: white;
                background: white;
                color: #667eea;
                padding: 20px 35px;
                border-radius: 15px;
                font-size: 20px;
                font-weight: bold;
            }

            a:hover {
                background: #eee;
            }
        </style>
    </head>

    <body>

        <h1>🚀 Multi-App Django Project</h1>

        <p>Welcome to my Django Practical 1</p>

        <div class="container">
            <a href="/accounts/">👤 Accounts</a>
            <a href="/products/">🛍️ Products</a>
            <a href="/orders/">📦 Orders</a>
        </div>

    </body>
    </html>
    """)

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)