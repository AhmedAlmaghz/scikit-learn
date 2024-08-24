{{ objname | escape | underline(line="=") }}

{% if objtype == "module" -%}

.. وحدة نمطية تلقائية:: {{ fullname }}

{%- elif objtype == "function" -%}

.. currentmodule:: {{ module }}

.. دالة تلقائية:: {{ objname }}

.. معرض مصغر:: {{ module }}.{{ objname }}
   :add-heading: أمثلة المعرض
   :heading-level: -

{%- elif objtype == "class" -%}

.. currentmodule:: {{ module }}

.. فئة تلقائية:: {{ objname }}
   :members:
   :inherited-members:
   :special-members: __call__

.. معرض مصغر:: {{ module }}.{{ objname }} {% for meth in methods %}{{ module }}.{{ objname }}.{{ meth }} {% endfor %}
   :add-heading: أمثلة المعرض
   :heading-level: -

{%- else -%}

.. currentmodule:: {{ module }}

.. auto{{ objtype }}:: {{ objname }}

{%- endif -%}

يرجى ملاحظة أنني قمت بترجمة المصطلحات التقنية إلى اللغة العربية، ولكن قد تحتاج إلى تعديل الترجمة اعتمادًا على السياق المحدد لمشروعك.