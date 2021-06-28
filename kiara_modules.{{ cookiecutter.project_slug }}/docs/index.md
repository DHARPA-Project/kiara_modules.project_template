# kiara modules for: {{ cookiecutter.project_name }}

This package contains a set of commonly used/useful modules, pipelines, types and metadata schemas for [*Kiara*](https://github.com/DHARPA-project/kiara).


## Description

TODO

## Package content

### [Core modules](https://dharpa.org/kiara/modules/core_modules/)

{{ get_module_list_for_package('kiara_modules.{{ cookiecutter.project_slug }}', include_pipelines=False) }}

### [Pipelines](https://dharpa.org/kiara/modules/pipeline_modules/)

{% raw %}{{{% endraw %} get_module_list_for_package('kiara_modules.{{ cookiecutter.project_slug }}', include_core_modules=False) {% raw %}}}{% endraw %}


### Value types

{% raw %}{{ get_value_types_for_package('kiara_modules.{{ cookiecutter.project_slug }}') {% raw %}}}{% endraw %}

### Metadata schemas

{% raw %}{{ get_metadata_schemas_for_package('kiara_modules.{{ cookiecutter.project_slug }}') {% raw %}}}{% endraw %}

## Links

 - Documentation: [https://dharpa.org/kiara_modules.{{ cookiecutter.project_slug }}](https://dharpa.org/kiara_modules.{{ cookiecutter.project_slug }})
 - Code: [https://github.com/DHARPA-Project/kiara_modules.{{ cookiecutter.project_slug }}](https://github.com/DHARPA-Project/kiara_modules.{{ cookiecutter.project_slug }})


