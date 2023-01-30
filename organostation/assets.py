"""
assets.py

Created: Wed Dec 14 14:51:46 CET 2022

CSS and JS bundles that will be compiled and served by Flask-Assets.

"""
from flask import current_app as myapp
from flask_assets import Bundle, Environment


def compile_static_assets(assets: Environment) -> None:
    """Compile static assets. Cascading Style Sheets (CSS) and JavaScript that
    will override standard Bootstrap5.0 CSS"""

    # Cascading Style Sheets will override Bootstrap CSS
    css_bundle = Bundle(
        "src/less/*.less",
        filters="less, cssmin",
        output="dist/css/style.min.css",
        extra={"rel": "text/css"},
    )

    # Tutorials assets bundle will add customized CSS
    tutorials_css_bundle = Bundle(
        "tutorials_bp/src/less/*.less",
        filters="less, cssmin",
        output="dist/css/tutorials.min.css",
        extra={"rel": "text/css"},
    )

    # JavaScript Standard
    js_bundle = Bundle(
        "src/js/*.js",
        filters="jsmin",
        output="dist/js/main.min.js",
        extra={"type": "text/javascript"},
    )

    # JavaScript Tutorials
    js_tutorials = Bundle(
        "tutorials_bp/src/js/*.js",
        filters="jsmin",
        output="dist/js/tutorials.min.js",
        extra={"type": "text/javascript"},
    )

    # Register bundles
    assets.register("main_styles", css_bundle)
    assets.register("tutorials_styles", tutorials_css_bundle)
    assets.register("main_js", js_bundle)
    assets.register("tutorials_js", js_tutorials)

    # Build less styles and JavaScript in development
    if myapp.config["FLASK_ENV"] == "development":
        print("Building LESS styles and JavaScript in development")
        css_bundle.build()
        tutorials_css_bundle.build()
        js_bundle.build()
        js_tutorials.build()
