from django.shortcuts import render
from .models import Taxi

def taxi_list(request):
    taxi_name = request.GET.get('taxi_name')
    license_plate = request.GET.get('license_plate')
    driver_name = request.GET.get('driver_name')
    pass_capacity = request.GET.get('pass_capacity')
    car_model = request.GET.get('car_model')
    status = request.GET.get('status')
    if (taxi_name is not None
            and license_plate is not None
            and driver_name is not None
            and pass_capacity is not None
            and car_model is not None
            and status is not None):
        Taxi.objects.create(
            taxi_name=taxi_name,
            license_plate=license_plate,
            driver_name=driver_name,
            pass_capacity=pass_capacity,
            car_model=car_model,
            status=status
        )
    taxi = Taxi.objects.all()
    ctx = {'taxis': taxi}
    return render(request, 'taxi/taxi_list.html', ctx)


