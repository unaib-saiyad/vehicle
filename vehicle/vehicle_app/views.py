from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import VehicleMod

# Create your views here.
global_messages = []


class Vehicle:
    def index(self):
        if self.method == 'GET':
            try:
                objs = []
                all_obj = VehicleMod.objects.all()
                for item in all_obj:
                    objs.append({
                        'avg_speed': item.avg_speed,
                        'temperature': item.temperature,
                        'fuel_level': item.fuel_level,
                        'id': item.id
                    })
            except:
                return render(self, 'vehicle/index.html', {'nav': 'home'})
            if global_messages:
                messages = [global_messages.pop()]
            else:
                messages = None
            return render(self, 'vehicle/index.html', {'nav': 'home', 'objects': objs, 'messages': messages})
        else:
            return render(self, 'error/error500.html', {'Status': False,
                                                        'Message': 'Only get request allowed to this page'})

    def add(self, id=None):
        if self.method == 'GET':
            return render(self, 'vehicle/add_update.html', {'nav': 'add'})
        speed = self.POST.get('speed')
        avgSpeed = self.POST.get('avg-speed')
        temperature = self.POST.get('temperature')
        fuelLevel = self.POST.get('fuel-level')
        ltd = self.POST.get('latitude')
        lng = self.POST.get('Longitude')
        leakage = self.POST.get('leakage')
        oil_level = self.POST.get('oil-level')
        oil_quality = self.POST.get('oil-quality')
        engine_status = {'leakage': leakage, 'oil_level': oil_level, 'oil_quality': oil_quality}
        if (ltd and lng) == "":
            messages = [{'type': 'danger', 'status': 'Error!...', 'message': 'Make sure you have added location'}]
            return render(self, 'vehicle/add_update.html',
                          {'nav': 'add', 'messages': messages})
        if VehicleMod.objects.filter(id=id).exists():
            VehicleMod.objects.filter(id=id).update(speed=speed, avg_speed=avgSpeed, temperature=temperature,
                                                    fuel_level=fuelLevel, engine_status=engine_status, latitude=ltd,
                                                    longitude=lng)
            return True
        else:
            if id is not None:
                return False
        try:
            VehicleMod.objects.create(speed=speed, avg_speed=avgSpeed, temperature=temperature,
                                      fuel_level=fuelLevel, engine_status=engine_status, latitude=ltd,
                                      longitude=lng)
            messages = [{'type': 'success', 'status': 'Success!...',
                         'message': 'Vehicle status successfully added'}]
        except:
            return render(self, 'error/error500.html',
                          {'Status': False, 'Message': 'Error occurred while creating the instance!...'})
        return render(self, 'vehicle/add_update.html',
                      {'nav': 'add', 'messages': messages})

    def status(self, id):
        if self.method == 'GET':
            if VehicleMod.objects.filter(id=id).exists():
                obj = VehicleMod.objects.filter(id=id).get()
                credential = {'speed': obj.speed, 'avg_speed': obj.avg_speed, 'temperature': obj.temperature,
                              'fuel_level': obj.fuel_level, 'engine_status': obj.engine_status,
                              'latitude': obj.latitude, 'longitude': obj.longitude}
            return render(self, 'vehicle/view_status.html', {'nav': 'none', 'credential': credential})
        return render(self, 'error/error500.html', {'Status': False,
                                                    'Message': 'Only get request allowed to this page!...'})

    def update(self, id):
        if self.method == 'POST':
            status = Vehicle.add(self, id)
            if status:
                global_messages.append({'type': 'success', 'status': 'success!...',
                                        'message': 'Object updated successfully'})
                return redirect('/')
            return render(self, 'error/error500.html', {'Status': False,
                                                        'Message': 'Something went wrong!...'})
        if VehicleMod.objects.filter(id=id).exists():
            obj = VehicleMod.objects.filter(id=id).get()
            credentials = {'speed': obj.speed, 'avg_speed': obj.avg_speed, 'temperature': obj.temperature,
                           'fuel_level': obj.fuel_level, 'engine_status': obj.engine_status, 'latitude': obj.latitude,
                           'longitude': obj.longitude}
            return render(self, 'vehicle/add_update.html', {'nav': 'add', 'credentials': credentials})
        return render(self, 'error/error500.html', {'Status': False,
                                                    'Message': 'Something went wrong!...'})

    def delete(self, id):
        if self.method == 'GET':
            return render(self, 'error/error500.html',
                          {'Status': False, 'Message': 'Only get request allowed to this page'})
        if VehicleMod.objects.filter(id=id).exists():
            VehicleMod.objects.filter(id=id).delete()
            global_messages.append({'type': 'success', 'status': 'success!...', 'message': 'Object deleted successfully'})
            return redirect('/')
        return render(self, 'error/error500.html', {'Status': False,
                                                    'Message': 'Something went wrong!...'})
