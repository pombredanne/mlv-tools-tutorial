{%- extends 'null.tpl' -%}
{%- block header %}
{%- if 'metadata' in resources -%} 
# Generated from {{ resources['metadata'].get('path') }}/{{ resources['metadata'].get('name') }}.ipynb
{%- endif -%}
{% set params = '' %}
{%- if nb.cells and '#Parameters' in nb.cells[0].source.replace(' ', '') -%}
{% set params = ', '.join(nb.cells[0].source.split('\n')[1:]).replace(' = ', '=') %}
{{ not nb.cells.pop(0) or '' }}{% endif %}
{% set func_name = resources.get('metadata', {'name': 'input_func'}).get('name').replace(' ', '').lower() %}
def {{ func_name }}({{ params }}):
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

