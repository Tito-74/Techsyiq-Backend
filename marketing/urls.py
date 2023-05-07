from django.urls import path
from .views import *

urlpattern = [
    # figure analysis
    path("/create", create_figure_analysis, name="create"),
    path("/fetch_analysis_details/", fetch_figure_analysis, name="fetch_analysis_details"),
    path("update_analysis_details", update_figures_details, name="update_analysis_details"),

    # subscription
    path("/subscribe", subscribe, name="subscribe"),
]