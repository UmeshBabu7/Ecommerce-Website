from django.urls import path
from .views import *

app_name='ecomapp'

urlpatterns = [
     # client side pages
    path('',HomeView.as_view(),name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("all-products/", AllProductsView.as_view(), name="allproducts"),
    path("product/<slug:slug>/", ProductDetailView.as_view(), name="productdetail"),
    path("add-to-cart-<int:pro_id>/", AddToCartView.as_view(), name="addtocart"),
    path("my-cart/", MyCartView.as_view(), name="mycart"),
    path("manage-cart/<int:cp_id>/", ManageCartView.as_view(), name="managecart"),
    path("empty-cart/", EmptyCartView.as_view(), name="emptycart"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("register/",
         CustomerRegistrationView.as_view(), name="customerregistration"),
    path("logout/", CustomerLogoutView.as_view(), name="customerlogout"),
    path("login/", CustomerLoginView.as_view(), name="customerlogin"),
    path("profile/", CustomerProfileView.as_view(), name="customerprofile"),
    path("profile/order-<int:pk>/", CustomerOrderDetailView.as_view(),
         name="customerorderdetail"), 
    path("search/", SearchView.as_view(), name="search"),
     # payment method (khalti)
     path("khalti-request/", KhaltiRequestView.as_view(), name="khaltirequest"),
     # reset password
    path("forgot-password/", PasswordForgotView.as_view(), name="passwordforgot"),
     path("password-reset/<email>/<token>/",
         PasswordResetView.as_view(), name="passwordreset"),




# adminpages
    path("admin-login/", AdminLoginView.as_view(), name="adminlogin"),
    path("admin-home/", AdminHomeView.as_view(), name="adminhome"),
    path("admin-order/<int:pk>/", AdminOrderDetailView.as_view(),
         name="adminorderdetail"),
    path("admin-all-orders/", AdminOrderListView.as_view(), name="adminorderlist"),
    path("admin-order-<int:pk>-change/",
         AdminOrderStatuChangeView.as_view(), name="adminorderstatuschange"),
     path("admin-product/list/", AdminProductListView.as_view(),
         name="adminproductlist"),
     # for admin product create form 
     path("admin-product/add/", AdminProductCreateView.as_view(),
         name="adminproductcreate"),
    path("admin-product/update/<int:pk>/", AdminProductUpdateView.as_view(), name="adminproductupdate"),
    path("admin-product/delete/<int:pk>/", AdminProductDeleteView.as_view(), name="adminproductdelete"),





   
]

