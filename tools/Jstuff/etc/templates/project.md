## **Project: {{name}}**
{% if description %}
{{description}}
{% endif %}

{% if namespaces %}
### **Namespaces:**
{% for namespace in namespaces %}
* {{namespace.name}}
{% endfor %}
{% endif %}

{% if classes %}
### **Classes:**
{% for class in classes %}
* {{class.name}}
{% endfor %}
{% endif %}

{% if interfaces %}
### **Interfaces:**
{% for interface in interfaces %}
* {{interface.name}}
{% endfor %}
{% endif %}