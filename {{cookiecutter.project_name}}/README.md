# How to develop
## Execute project in local
After clone project, just run the docker compose file.

`$ docker-compose up`

### Open the localhost

`http://127.0.0.1:5000/version`

### Open Swagger UI
`http://127.0.0.1:5000/swagger/`


# Add new dependencies to the project
## Add the new dependency with poetry
```bash
$ poetry add Flask
```

## Update the requirements.txt
Use the `make freeze-dependencies` command instead `pip freeze`.

# Deploy new version
Remember to work with `branches` and `Pull requests` as this way you will be sure that everything that is merging to `master` has passed the pipeline that tests the lint and the tests.

After you have merged your branch to `master` then you can run the command `make release-major|minor|patch`. These commands will generate a tag and a new commit with the updated version and will start a pipeline in Bitbucket that once finished will deploy your application.

### **There are 3 commands to generate a new version:**

**make release-major**: Usually used when new changes break compatibility with the previous version.

**make release-minor**: We generate a minor when it comes to new features.

**make release-patch**: When they are bug fixes.
