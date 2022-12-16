"""
assets.py

Created: Wed Dec 14 14:51:46 CET 2022

CSS and JS bundles that will be compiled and served by Flask-Assets.
"""
from flask_assets import Bundle, Environment


def compile_static_assets(assets: Environment) -> None:
    """Compile static assets."""

    # Cascading Style Sheets
    css_bundle = Bundle(
        "src/less/*.less",
        filters="less, cssmin",
        output="dist/css/style.min.css",
        extra={"rel": "stylesheet/css"}
    )

    # JS
    js_bundle = Bundle(
        "src/js/main.js",
        filters="jsmin",
        output="dist/js/main.min.js"
    )

    # Register bundles
    assets.register("main_styles", css_bundle)
    #assets.register("main_js", js_bundle)

    # Build less styles
    css_bundle.build()
    #js_bundle.build()
