# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "openweather_integration"
app_title = "Openweather Integration"
app_publisher = "Brandon Fox, Foxtrot"
app_description = "Openweathermap.org"
app_icon = "glyphicon glyphicon-cloud"
app_color = "grey"
app_email = "bfox@foxtrot.email"
app_version = "0.0.2"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/openweather_integration/css/openweather_integration.css"
# app_include_js = "/assets/openweather_integration/js/openweather_integration.js"

# include js, css files in header of web template
# web_include_css = "/assets/openweather_integration/css/openweather_integration.css"
# web_include_js = "/assets/openweather_integration/js/openweather_integration.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "openweather_integration.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "openweather_integration.install.before_install"
# after_install = "openweather_integration.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "openweather_integration.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"openweather_integration.tasks.all"
# 	],
# 	"daily": [
# 		"openweather_integration.tasks.daily"
# 	],
# 	"hourly": [
# 		"openweather_integration.tasks.hourly"
# 	],
# 	"weekly": [
# 		"openweather_integration.tasks.weekly"
# 	]
# 	"monthly": [
# 		"openweather_integration.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "openweather_integration.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "openweather_integration.event.get_events"
# }

