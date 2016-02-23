package {{resource.namespace}}.{{resource.name.lower()}}.impl;

import com.linkedin.restli.server.annotations.RestLiCollection;
import com.linkedin.restli.server.resources.CollectionResourceTemplate;
import {{resource.namespace}}.{{resource.name.lower()}}.{{resource.name}};
{% if 'update' in resource.methods or 'delete' in resource.methods %}import com.linkedin.restli.server.UpdateResponse;{% endif %}
{% if 'create' in resource.methods %}import com.linkedin.restli.server.CreateResponse;{% endif %}
{% if 'create' in resource.methods or 'update' in resource.methods or 'delete' in resource.methods %}import com.linkedin.restli.common.HttpStatus;{% endif %}
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
    {% elif method == 'update' %}
    public UpdateResponse update(Long key, {{resource.name}} entity) 
    {
        return new UpdateResponse(HttpStatus.S_200_OK);
    }
    {% elif method == 'create' %}
    public CreateResponse create({{resource.name}} entity) 
    {
        return new CreateResponse(HttpStatus.S_200_OK);
    }
    {% elif method == 'delete' %}
    public UpdateResponse delete(Long key)
    {
        return new UpdateResponse(HttpStatus.S_200_OK);
    }
    {% endif %}
    {% endfor %}
}
