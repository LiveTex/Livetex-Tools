## **Namespace: {{name}}**
{% if description %}
{{description}}
{% endif %}

{% if typedefs %}
### **Type Definition:**

<table>
  <tr>
    <th>Nane</th><th>Type</th><th>Description</th>
  </tr>
  {% for typedef in typedefs%}
  <tr>
    <td>{{typedef.name}}</td><td>{{typedef.type}}</td><td>{{typedef.description}}</td>
  </tr>
  {% endfor %}
</table>
{% endif %}

{% if properties %}
### **Properties:**

<table>
  <tr>
    <th>Name</th><th>Value</th><th>Type</th><th>Description</th>
  </tr>
  {% for property in properties%}
  <tr>
    <td>{{property.name}}</td><td>{{property.value}}</td><td>{{property.type}}</td><td>{{property.description}}</td>
  </tr>
  {% endfor %}
</table>
{% endif %}


{% if methods %}
### **Methods:**

{% for method in methods %}

#### {{method.signature}}
{% if method.description %}{{method.description}}{% endif %}

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


{% if enums %}
### **Enumerations:**
{% for enum in enums%}

#### {{enum.name}}
{% if enum.description %}{{enum.description}}{% endif %}
{% if enum.type %}Type:{{enum.type}}{% endif %}

<table>
  <tr>
    <th>Name</th><th>Value</th>
  </tr>
  {% for i in range(enum.number)%}
  <tr>
    <td>{{enum.keys[i]}}</td><td>{{enum.values[i]}}</td>
  </tr>
  {% endfor %}
</table>

{% endfor %}
{% endif %}
