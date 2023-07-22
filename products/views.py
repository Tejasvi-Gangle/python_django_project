from django.shortcuts import render,redirect,get_object_or_404
from products.forms import Contactform,Reviewform
from products.models import Review


# Create your views here.
def home(request):
    return render(request,"home.html")
def makeup(request):
    return render(request,"makeup.html")
def haircare(request):
    return render(request,"haircare.html")
def skincare(request):
    return render(request,"skincare.html")
def contact(request):  #for enquiry form and map
    contactform=Contactform(request.POST or None)
    if contactform.is_valid():
        contactform.save()
        return redirect("home")  #message will give the confirmation of submitting the enquiry
    return render(request,"contact.html",{"forms":Contactform})
def addreview(request):  #for adding reviews
    addform=Reviewform(request.POST or None)
    if addform.is_valid():
        addform.save()
        return redirect("allreviews")
    return render(request,"addreviews.html",{"forms":addform})
def allreviews(request):#for showing review
    showreview=Review.objects.all()
    return render(request,"allreviews.html",{"reviews":showreview})
def review_edit(request,pk):#for edit
    review=get_object_or_404(Review,pk=pk)
    reviewform=Reviewform(request.POST or None,instance=review)
    if reviewform.is_valid():
        reviewform.save()
        return redirect("allreviews.html")
    return render(request,"addreview.html",{"forms":Reviewform})
def deletereview(request,pk):
    review=get_object_or_404(Review,pk=pk)
    if request.method=="POST":
        review.delete()
        return redirect("allreviews")
    return render(request,"deletereview.html",{"review":review})
# def cart(request):
#     return render(request, 'cart.html')
    