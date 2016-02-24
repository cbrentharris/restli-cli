#Restli CLI [![Build Status](https://travis-ci.org/cbrentharris/restli-cli.svg?branch=master)](https://travis-ci.org/cbrentharris/restli-cli)

A python package for creating a boilerplate [restli](https://github.com/linkedin/rest.li/wiki/Rest.li-User-Guide) project

===

###SCAFFOLDING

```
restli --scaffold my_project --namespace com.example
```

Will scaffold a new restli project layout under the directory named `my_project` with the layout below:

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
