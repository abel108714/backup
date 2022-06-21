#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'manage_panel.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # modulename = 'manage_panel.models'
	# if modulename not in sys.modules:
	# 	print("You have not imported the {} module".format(modulename))
    try:
        from manage_panel.models import Line
        #import sys
        print("456")
    except ImportError:
        print("123")
    main()
