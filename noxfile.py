import nox


@nox.session
def lint(session):
    session.run("poetry", "run", "black", "rsyncS3")
    session.run("poetry", "run", "pylint", "rsyncS3")
