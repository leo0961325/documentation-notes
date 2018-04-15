# jinja2

```py
def x():
    dict = {
        'a': 50,
        'b': 30, 
        'c': 80
        }

    return render_template('xxx.html', result=dict)
```


```html
{% for k, v in result.iteritems() %}
    <tr>
        <th> {{ k }} </th>
        <td> {{ v }} </td>
    </tr>
{% endfor %}
```