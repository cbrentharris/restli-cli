package {{resource.namespace}}.{{resource.name.lower()}};
import com.linkedin.r2.transport.http.server.HttpServer;
import org.junit.Before;
import org.junit.After;
import org.junit.Test;

public class Test{{resource.name}}sResource
{
    private HttpServer testServer;
    private static final int PORT = 7777;
    private static final String HOST = "http://localhost:" + PORT;

    @Before
    public void init() 
    {
    }

    {% for method in resource.methods %}
//    @Test
    public void test{{method.capitalize()}}()
    {
    }
    {% endfor %}

    @After
    public void cleanup()
    {
    }

}
