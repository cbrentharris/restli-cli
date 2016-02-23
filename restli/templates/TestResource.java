import com.linkedin.r2.transport.http.server.HttpServer;

public class Test{{resource.name}}sResource
{
    private HttpServer testServer;
    private static final int PORT = 7777;
    private static final string HOST = "http://localhost:" + PORT;

    @BeforeTest
    public void init() 
    {
    }

    {% for method in resource.methods %}
    @Test
    public void test{{method.capitalize()}}()
    {
    }
    {% endfor %}

    @AfterTest
    public void cleanup()
    {
    }

}
