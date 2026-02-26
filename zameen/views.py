from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from listings.models import listings, Booking , RoomBooking
from listings.forms import RoomBookingForm



def login(request):
    final=0
    data={}
    try:
        if request.method=="post":
        
            user = request.POST.get['user']
            phone = request.POST.get['phone']
            adhar = request.POST.get['adhar']
            password = request.POST.get['password']
            final=phone
            data={
                'u':user,
                'phone': phone,
                'password':password,
                'adhar': adhar,
            }
    except:
        pass

    
    return render(request, "login.html",data)

def room(request, id):
    roomd = get_object_or_404(listings,id=id)
    # room_obj = get_object_or_404(listings,id=id)

    listing=listings.objects.get(id=id)
    # # request.session['id']=listings.id
    listingdata=listings.objects.all()
    # Booking.objects.create(
    #     user=request.user,
    #     listings = room_obj
    # )

    
    
    data={
        'listingdata':listingdata,
        
    }
    
    
    images=[
        listing.Room_images1,
        listing.Room_images2,
        listing.Room_images3,
        listing.Room_images4,
        listing.Room_images5,
    ]
    
   
    return render( request, "room.html",{'room': roomd ,'images':images,'data':data,})

def base(request):
    listingdata=listings.objects.all()
    title=request.GET.get('search')
    if title:
        listingdata=listingdata.filter(Room_title__icontains=title)
    data={
        'listingdata':listingdata,
        'title':title
    }

    

    return render(request, "base.html",data)
def bhk2(request):
    listingdata=listings.objects.filter(Room_title="2bhk")
    title=request.GET.get('search')
    if title:
        listingdata=listingdata.filter(Room_title__icontains=title)
    data={
        'listingdata':listingdata,
        'title':title
    }

    return render(request, "bhk2.html",data)
def AboutUs(response):
    

    return render(response, "About-Us.html")
def bhk3(response):
    listingdata=listings.objects.filter(Room_title="3bhk")
    data={
        'listingdata':listingdata
    }

    return render(response, "bhk3.html",data)
def pg(response):
    listingdata=listings.objects.filter(Room_title="pg")
    data={
        'listingdata':listingdata
    }

    return render(response, "pg.html",data)
def bookingcon(request,id):
    roomt = get_object_or_404(listings,id=id)

    bookingdata=get_object_or_404(RoomBooking,id=id)
    # Booking.objects.create(
       
    #     roomti=listings.Room_title,

    #  )
    

    
        # {"room":room,'detail':detail,'list':room_obj,'booking':booking}
    return render(request, "bookingconfirm.html",{'room':roomt,'bookingd':bookingdata})
def mybooking(request):
    listingdata=listings.objects.all()
    
    # Bookings = Booking.objects.filter(RoomBooking,id=id)
    # data={
    #     'listingdata':listingdata,
        
    # }
    # name = request.GET.get("name")  # same name jo booking me dala

    # bookings = RoomBooking.objects.filter(name=name)

    return render(request, 'mybooking.html')
    
    
    


def more(request):
    listingdata=listings.objects.all()
    
    data={
        'listingdata':listingdata,
        
    }

    

    return render(request, "more.html",data )
def bookingform(request,id):
    roomd = get_object_or_404(listings,id=id)
    bookingdata=get_object_or_404(RoomBooking,id=id)

    if request.method == 'POST':
        
        form = RoomBookingForm(request.POST)
        # listings=listings.objects.get(id=id)
        # Booking.objects.create(
        #     user=request.user,
        #     listings=listings,

        # )

        # id=id
        
        formdata=listings.objects.all()
        if form.is_valid():
            booking = form.save(commit=False)
            # booking.user = request.user   # logged-in user assign
            booking.save()
            
            # return redirect("bookingconfirm", )  # success ke baad
    else:
        form = RoomBookingForm()
    

    return render(request, "bookingform.html",{'form':form,'room':roomd,'id':id})