from __future__ import unicode_literals
from frappe import _


def get_data():
    return [
        {
            "label": _("Integrations"),
            "icon": "icon-star",
            "items": [
                {
                    "type": "doctype",
                    "name": "OWM API Settings",
                    "description": _("Setup Open Weather Map API credentials"),
                    "hide_count": True
                }
            ]
        }
    ]
