# Kunti 👸

A simple yet powerful ReST API for managing micro blogs ✍️


## Description

### Dependency

* [Docker][docker]

* [Compose][compose]

* [Python][python]


### Build 🔧

```
make docker-compose-build
```

This command will build dependent images. It is required to run this command
before running any other command.

```
make docker-compose-up
```
This command will bootstrap all required dependencies. It is required to run
`make docker-compose-build` before running this command. After firing this
command, you can browse API documentation at `http://localhost` or
`http://127.0.0.0` of your workstation.


### API Flow 🍨


* Once service is bootstrapped, got to `http://localhost/docs` for API
  documentation.

* Create new user by Posting user details like `username`, `first name`,
  `last name`, `email`, `password` at `http://localhost/signup`.

* Once new user is created, obtain an authentication token via sharing
  credentials at `http://localhost/login`.

* Attach authentication token at `Authorization` header of each HTTP request for
  accessing protected endpoints.


### API endpoints 💡


#### Posts

Posts endpoint is responsible for managing blog posts of User.

#### Comments

Comments endpoint is responsible for managing user comments.

[docker]: https://docker.com
[compose]: https://docs.docker.com/compose/
[python]: https://python.org
