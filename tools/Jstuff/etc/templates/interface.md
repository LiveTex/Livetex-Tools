## **Interface: {{name}}**
{% if description %}
{{description}}
{% endif %}


{% if parents %}
### **Extends:**
{% for parent in parents %}
#### {{parent.name}}
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


{% if users %}
### **Users:**
{% for user in users %}
#### {{user}}
{% endfor %}
{% endif %}