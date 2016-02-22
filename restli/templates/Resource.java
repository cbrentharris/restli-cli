package {{resource.namespace}}.{{resource.name.lower()}}.impl;

import com.linkedin.restli.server.annotations.RestLiCollection;
import com.linkedin.restli.server.resources.CollectionResourceTemplate;
import {{resource.namespace}}.{{resource.name.lower()}}.{{resource.name}};

@RestLiCollection(name = "{{resource.name.lower()}}s", namespace = "{{resource.namespace}}.{{resource.name.lower()}}")
public class {{resource.name}}sResource extends CollectionResourceTemplate<Long, {{resource.name}}>
{

    {% for method in resource.methods %}
    @Override
    {% if method == 'get' %}
    public {{resource.name}} get(Long key) 
    {
        return new {{resource.name}}();
    }
    {% endif %}
    {% endfor %}
}
