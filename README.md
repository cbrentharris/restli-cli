#Restli CLI

A python package for helping with creating a boilerplate restli project
===
###SCAFFOLDING

```
restli --scaffold my_project --namespace com.example
```

Will generate a new restli project layout under the directory named `my_project` with the layout below.

```
└── my_project
    ├── api
    │   ├── build.gradle
    │   └── src
    │       └── main
    │           ├── idl
    │           ├── mainGeneratedDataTemplate
    │           └── pegasus
    ├── build.gradle
    ├── client
    ├── server
    │   ├── build.gradle
    │   ├── settings.gradle
    │   └── src
    │       └── main
    │           ├── java
    │           └── mainGeneratedRest
    └── settings.gradle
```


###GENERATION

```
restli --generate Fortune --namespace com.example
```

Will generate two restli files for you, `api/src/main/pegasus/com/example/fortune/Fortune.pdsc` and a `server/src/main/java/com/example/fortune/impl/FortunesResource.java`
