#!/usr/bin/env python
import os, sys

# To skip test_site_profile_not_available from django.contrib.auth.tests.models.ProfileTestCase
# see https://code.djangoproject.com/ticket/17966
sys.modules['django.contrib.auth.tests'] = None


if __name__ == "__main__":
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
