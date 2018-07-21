from django.shortcuts import render
from django.views.generic import View

from .models import Organizations, Cities


class OrgListView(View):
    def get(self, request):
        # 获取所有机构
        all_orgs = Organizations.objects.all()
        # 获取所有城市
        all_cities = Cities.objects.all()

        # 获取符合条件机构的数量
        orgs_count = all_orgs.count()

        return render(request, 'org-list.html', {
            'all_orgs':all_orgs,
            'all_cities':all_cities,
            'orgs_count':orgs_count,
        })
