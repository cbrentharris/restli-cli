===Restli CLI

A python package for helping with creating a boilerplate restli project

SCAFFOLDING

```
restli --scaffold my_project --namespace com.example
```

Will generate a new restli project layout under the directory named `my_project`


GENERATION

```
restli --generate Fortune --namespace com.example
```

Will generate two restli files for you, `api/src/main/pegasus/com/linkedin/fortune/Fortune.pdsc` and a `server/src/main/java/com/linkedin/fortune/impl/FortunesResource.java`
