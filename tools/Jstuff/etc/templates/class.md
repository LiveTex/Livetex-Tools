## **Class: {{name}}**
{% if description %}
{{description}}
{% endif %}

### **Constructor:**
####{{signature}}
{% if parameters%}
<table>
  <tr>
    <th>Parameter</th><th>Type</th><th>Description</th>
  </tr>
  {% for parameter in parameters%}
  <tr>
    <td>{{parameter.name}}</td><td>{{parameter.type}}</td><td>{{parameter.description}}</td>
  </tr>
  {% endfor %}
</table>
{% endif %}

{% if attributes %}
**Attributes**
<table>
  <tr>
    <th>Attribute</th><th>Type</th><th>Description</th>
  </tr>
  {% for attribute in attributes %}
  <tr>
    {% if attribute.signature%}
    <td>{{attribute.signature}}</td><td>{{attribute.type}}</td><td>{{attribute.description}}</td>
    {% else %}
    <td>{{attribute.name}}</td><td>{{attribute.type}}</td><td>{{attribute.description}}</td>
    {% endif %}
  </tr>
  {% endfor %}
</table>
{% endif %}

{% if parents %}
### **Extends:**
{% for parent in parents %}
* {{parent.name}}
{% endfor %}
{% endif %}

{% if interfaces %}
### **Implements:**
{% for interface in interfaces %}
* {{interface.name}}
{% endfor %}
{% endif %}

{% if methods %}
### **Methods:**

{% for method in methods %}


#### {{method.signature}}
{% if method.description %}
{{method.description}}
{% endif %}

{% if method.parameters %}
<table>
  <tr>
    <th>Parameter</th><th>Type</th><th>Description</th>
  </tr>
  {% for parameter in method.parameters%}
  <tr>
    <td>{{parameter.name}}</td><td>{{parameter.type}}</td><td>{{parameter.description}}</td>
  </tr>
  {% endfor %}
</table>
{% endif %}
{% if method.result %}
<table>
  <tr>
    <th>Returns</th><td>{{method.result.type}}</td><td>{{method.result.description}}</td>
  </tr>
</table>
{% endif %}

{% endfor %}
{% endif %}