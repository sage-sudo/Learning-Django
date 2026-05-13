# CSS Usage Documentation

## Overview
This document explains how CSS is loaded in the Learning-Django project, and clarifies which CSS files are active in development and production.

## Django static configuration
File: `my_tennis_club/my_tennis_club/settings.py`

Configured static settings:
```python
STATIC_ROOT = BASE_DIR / 'productionfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'mystaticfiles'
]
STATIC_URL = 'static/'
```

### Meaning
- `STATICFILES_DIRS` defines where Django looks for static assets during development and before `collectstatic`.
- `STATIC_ROOT` is the destination directory used by `collectstatic` to gather static files for production.
- In development (`DEBUG=True`), Django serves directly from `STATICFILES_DIRS`.
- In production, `collectstatic` copies assets into `STATIC_ROOT`, and the web server should serve from there.

## CSS files in the project

### Source folder
- `my_tennis_club/mystaticfiles/myglobal.css`

### Production/static root folder
- `my_tennis_club/productionfiles/myglobal.css`
- `my_tennis_club/productionfiles/myfirst.css`

### Important note
- `myglobal.css` exists in both the source folder and the production folder.
- `myfirst.css` currently exists only in `productionfiles`, not in `mystaticfiles`.

## Which CSS file is used?

### In development
- Django will use `mystaticfiles/myglobal.css` for the `myglobal.css` asset.
- `productionfiles/` is not a source directory, so it is not used directly by Django's staticfiles finder in development.

### In production
- If `python manage.py collectstatic` is run, Django will collect files from `STATICFILES_DIRS` into `STATIC_ROOT`.
- The production server should serve CSS from `productionfiles/`.
- In that case, the file at `productionfiles/myglobal.css` would be the served CSS file.

## Template references

### `members/templates/master.html`
```html
{% load static %}
<link rel="stylesheet" href="{% static 'myglobal.css' %}">
```
- This page uses `myglobal.css`.

### `members/templates/myfirst.html`
```html
{% load static %}
<link rel="stylesheet" type="text/css" href="{% static 'myglobal.css' %}">
```
- This page also uses `myglobal.css`.

### `members/templates/testing.html`
```html
{% load static %}
<link rel="stylesheet" href={% static 'myfirst.css' %}">
```
- This page uses `myfirst.css`.

## Observations and recommendations

### Observations
- `myglobal.css` is the main stylesheet referenced by templates and is available in both `mystaticfiles` and `productionfiles`.
- `myfirst.css` is referenced by `testing.html`, but it exists only in `productionfiles`, which is inconsistent with the static setup.
- Because `productionfiles` is configured as `STATIC_ROOT`, it should not normally contain source static files.

### Recommendations
1. Move `productionfiles/myfirst.css` into `mystaticfiles/` so it is available during development and before `collectstatic`.
2. Keep `productionfiles/` reserved for collected static assets only.
3. Optionally add both CSS files to `mystaticfiles/` and re-run `python manage.py collectstatic`.

## File content highlights

### `mystaticfiles/myglobal.css`
- Defines the site font and color scheme
- Styles `.topnav`, `.mycard`, `ul`, `li`, and `.main`

### `productionfiles/myglobal.css`
- Same base rules as `mystaticfiles/myglobal.css`
- Also includes a `.mylinks` class at the end

### `productionfiles/myfirst.css`
- This file exists only in productionfiles and is used by `testing.html`.

## Conclusion
- In the current setup, `mystaticfiles/myglobal.css` is the effective development source for `myglobal.css`.
- `productionfiles/myglobal.css` becomes relevant after `collectstatic` in production.
- `myfirst.css` should be moved into `mystaticfiles/` to align with Django static config and avoid broken asset resolution.
