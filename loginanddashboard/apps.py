from django.apps import AppConfig


class LoginanddashboardConfig(AppConfig):
    name = 'loginanddashboard'

    def ready(self):
    	import loginanddashboard.signals