{%- extends 'null.tpl' -%}
{%- block header %}
{%- if 'metadata' in resources -%} 
# Generated from {{ resources['metadata'].get('path') }}/{{ resources['metadata'].get('name') }}.ipynb
{%- endif -%}
{% set params = [] %}
{%- if nb.cells %}
    {% set docstring, params = nb.cells[0].source | extract_docstring_and_param %}
    {% if params %}{{ not nb.cells.pop(0) or '' }}{% endif %}
{% endif %}
{% set func_name = resources.get('metadata', {'name': 'input_func'}).get('name').replace(' ', '').lower() %}

def {{ func_name }}({{ ', '.join(params) }}):
{% for line in docstring %}
    {{ line }}
{% endfor %}
{% endblock header %}

{% block input %}
{% set pythonized = cell.source | ipython2python %}    
{%- for line in pythonized.split('\n') -%}
{% if line %}
    {{ line.replace('\n', '') }}{% endif %}
{%- endfor -%}
{% endblock input %}


{% block markdowncell scoped %}
{{ cell.source | comment_lines }}
{% endblock markdowncell %}

