# Templates 寫法
- 2018/07/02
- [Django Template {{ block.super }} example](https://gist.github.com/issackelly/928783)

```html
# Template: A.html
<html>
    <head></head>
    <body>
        {% block hello %}
            HELLO 
        {% endblock %}
    </body>
</html>

# Template B.html
{% extends "A.html" %}
{% block hello %}
World
{% endblock %}

# Rendered Template B
<html>
    <head></head>
    <body>
World
    </body>
</html>

# Template C
{% extends "A.html" %}
{% block hello %}
{{ block.super }} World
{% endblock %}


# Rendered Template C
<html>
    <head></head>
    <body>
Hello World
    </body>
</html>
```