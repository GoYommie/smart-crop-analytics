from django.shortcuts import render
from django.db.models import Q, Sum, Avg
from .models import CropData
import json


# =========================
# DATA PAGE (TABLE)
# =========================
def home(request):

    # Get all records from the database
    crops = CropData.objects.all()

    # Get filter values from the URL
    year = request.GET.get('year')
    region = request.GET.get('region')
    search = request.GET.get('search')
    sort = request.GET.get('sort')

    # Apply filters if user selects them
    if year:
        crops = crops.filter(year=year)

    if region:
        crops = crops.filter(region=region)

    # Search by crop name or region (case-insensitive)
    if search:
        crops = crops.filter(
            Q(crop__icontains=search) |
            Q(region__icontains=search)
        )

    # Sort results
    if sort == 'production':
        crops = crops.order_by('-production')  # highest production first
    elif sort == 'yield':
        crops = crops.order_by('-yield_amount')  # highest yield first

    # Get unique values for dropdown filters
    years = CropData.objects.values_list('year', flat=True).distinct()
    regions = CropData.objects.values_list('region', flat=True).distinct()

    # Send data to HTML table
    return render(request, 'crops/data.html', {
        'crops': crops,
        'years': years,
        'regions': regions,
    })


# =========================
# CHART PAGE
# =========================
def chart_page(request):

    # Start with all data
    crops = CropData.objects.all()

    # Get filter values
    year = request.GET.get('year')
    region = request.GET.get('region')
    crop_name = request.GET.get('crop')

    # Apply filters
    if year:
        crops = crops.filter(year=year)

    if region:
        crops = crops.filter(region=region)

    if crop_name:
        crops = crops.filter(crop=crop_name)

    # Dropdown values
    years = CropData.objects.values_list('year', flat=True).distinct()
    regions = CropData.objects.values_list('region', flat=True).distinct()
    crop_names = CropData.objects.values_list('crop', flat=True).distinct()

    # -------------------------
    # CHART 1: Production by Crop
    # -------------------------
    production_data = (
        crops.values('crop')  # group by crop
        .annotate(total_production=Sum('production'))  # total production
        .filter(total_production__isnull=False)  # remove nulls
        .order_by('-total_production')[:10]  # top 10
    )

    production_labels = [item['crop'] for item in production_data]
    production_values = [item['total_production'] or 0 for item in production_data]

    # -------------------------
    # CHART 2: Yield Over Time
    # -------------------------
    yield_data = (
        crops.values('year')  # group by year
        .annotate(avg_yield=Avg('yield_amount'))  # average yield
        .filter(avg_yield__isnull=False)
        .order_by('year')
    )

    yield_labels = [item['year'] for item in yield_data]
    yield_values = [float(item['avg_yield'] or 0) for item in yield_data]

    # -------------------------
    # CHART 3: Production by Region
    # -------------------------
    region_data = (
        crops.values('region')
        .annotate(total_production=Sum('production'))
        .filter(total_production__isnull=False, total_production__gt=0)
        .order_by('-total_production')
    )

    region_labels = [item['region'] for item in region_data]
    region_values = [item['total_production'] or 0 for item in region_data]

    # Convert Python lists to JSON for Chart.js
    return render(request, 'crops/charts.html', {
        'years': years,
        'regions': regions,
        'crop_names': crop_names,

        'production_labels': json.dumps(production_labels),
        'production_values': json.dumps(production_values),

        'yield_labels': json.dumps(yield_labels),
        'yield_values': json.dumps(yield_values),

        'region_labels': json.dumps(region_labels),
        'region_values': json.dumps(region_values),
    })