from django.shortcuts import render
from django.db.models import Q, Sum, Avg
from .models import CropData


def home(request):
    crops = CropData.objects.all()

    # ✅ GET FILTER VALUES
    year = request.GET.get('year')
    region = request.GET.get('region')
    search = request.GET.get('search')
    sort = request.GET.get('sort')

    # ✅ FILTERS 
    if year:
        crops = crops.filter(year=year)

    if region:
        crops = crops.filter(region=region)

    if search:
        crops = crops.filter(
            Q(crop__icontains=search) |
            Q(region__icontains=search)
        )

    # This retains a copy BEFORE slicing for charts
    filtered = crops

    # ✅ SORT NEXT
    if sort == 'production':
        crops = crops.order_by('-production')
    elif sort == 'yield':
        crops = crops.order_by('-yield_amount')

    # ✅ SLICE (ONLY FOR TABLE)
    crops = crops[:50]

    # 🔹 DROPDOWNS
    years = CropData.objects.values_list('year', flat=True).distinct()
    regions = CropData.objects.values_list('region', flat=True).distinct()

    # =========================
    # 📊 CHART DATA (FILTERED DATA)
    # =========================

    # 🔹 Production by crop
    production_data = (
        filtered
        .values('crop')
        .annotate(total_production=Sum('production'))
        .filter(total_production__isnull=False, total_production__gt=0)
        .order_by('-total_production')[:10]
    )

    production_labels = [item['crop'] for item in production_data]
    production_values = [item['total_production'] or 0 for item in production_data]

    # 🔹 Yield over time 
    yield_data = (
        filtered
        .values('year')
        .annotate(avg_yield=Avg('yield_amount'))
        .filter(avg_yield__isnull=False, avg_yield__gt=0)
        .order_by('year')
    )

    yield_labels = [item['year'] for item in yield_data]
    yield_values = [float(item['avg_yield']) for item in yield_data]

    # 🔹 Production by region
    region_data = (
        filtered
        .values('region')
        .annotate(total_production=Sum('production'))
        .filter(total_production__isnull=False, total_production__gt=0)
        .order_by('-total_production')
    )

    region_labels = [item['region'] for item in region_data]
    region_values = [item['total_production'] for item in region_data]

    return render(request, 'crops/home.html', {
        'crops': crops,
        'years': years,
        'regions': regions,
        'production_labels': production_labels,
        'production_values': production_values,
        'yield_labels': yield_labels,
        'yield_values': yield_values,
        'region_labels': region_labels,
        'region_values': region_values
    })