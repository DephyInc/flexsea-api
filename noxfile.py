import nox


@nox.session
def lint(session):
    session.run("poetry", "run", "black", "s3cache")
    session.run("poetry", "run", "pylint", "s3cache")
