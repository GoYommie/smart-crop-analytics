from django.shortcuts import render
from django.db.models import Q, Sum, Avg
from .models import CropData
import json


# =========================
# DATA PAGE (TABLE)
# =========================
def home(request):
    crops = CropData.objects.all()

    year = request.GET.get('year')
    region = request.GET.get('region')
    search = request.GET.get('search')
    sort = request.GET.get('sort')

    # FILTERS
    if year:
        crops = crops.filter(year=year)

    if region:
        crops = crops.filter(region=region)

    if search:
        crops = crops.filter(
            Q(crop__icontains=search) |
            Q(region__icontains=search)
        )

    # SORT
    if sort == 'production':
        crops = crops.order_by('-production')
    elif sort == 'yield':
        crops = crops.order_by('-yield_amount')

    # DROPDOWNS
    years = CropData.objects.values_list('year', flat=True).distinct()
    regions = CropData.objects.values_list('region', flat=True).distinct()

    return render(request, 'crops/data.html', {
        'crops': crops,
        'years': years,
        'regions': regions,
    })


# =========================
# CHART PAGE
# =========================
def chart_page(request):
    crops = CropData.objects.all()

    year = request.GET.get('year')
    region = request.GET.get('region')
    crop_name = request.GET.get('crop')

    if year:
        crops = crops.filter(year=year)

    if region:
        crops = crops.filter(region=region)

    if crop_name:
        crops = crops.filter(crop=crop_name)

    years = CropData.objects.values_list('year', flat=True).distinct()
    regions = CropData.objects.values_list('region', flat=True).distinct()
    crop_names = CropData.objects.values_list('crop', flat=True).distinct()

    # CHART 1
    production_data = (
        crops.values('crop')
        .annotate(total_production=Sum('production'))
        .filter(total_production__isnull=False)
        .order_by('-total_production')[:10]
    )

    production_labels = [item['crop'] for item in production_data]
    production_values = [item['total_production'] or 0 for item in production_data]

    # CHART 2
    yield_data = (
        crops.values('year')
        .annotate(avg_yield=Avg('yield_amount'))
        .filter(avg_yield__isnull=False)
        .order_by('year')
    )

    yield_labels = [item['year'] for item in yield_data]
    yield_values = [float(item['avg_yield'] or 0) for item in yield_data]

    # CHART 3
    region_data = (
        crops.values('region')
        .annotate(total_production=Sum('production'))
        .filter(total_production__isnull=False, total_production__gt=0)
        .order_by('-total_production')
    )

    region_labels = [item['region'] for item in region_data]
    region_values = [item['total_production'] or 0 for item in region_data]

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