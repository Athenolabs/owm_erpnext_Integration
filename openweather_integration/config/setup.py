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
                    "name": "Open Weather Map API Settings",
                    "description": _("Setup Open Weather credentials"),
                    "hide_count": True
                }
            ]
        }
    ]
