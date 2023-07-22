from django.conf.urls import url 
from products.views import review_edit,deletereview,makeup,haircare,skincare,contact,addreview,allreviews

urlpatterns= [
    url(r'^makeup/$',makeup,name="makeup"),
    url(r'^haircare/$',haircare,name="haircare"),
    url(r'^skincare/$',skincare,name="skincare"),
    url(r'^contact/$',contact,name="contact"),
    # url(r'^cart/$',cart,name="cart"),
    url(r'^addreview/$',addreview,name="addreview"),
    url(r'^$',allreviews,name="allreviews"),
    url(r'^edit/(?P<pk>\d+)/$',review_edit,name='review_edit'),
    url(r'^delete/(?P<pk>\d+)/$',deletereview,name='deletereview')

]