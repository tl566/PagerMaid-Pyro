from pathlib import Path


def rename(old: Path):
    if old.exists():
        old_file_name = old.name
        new = Path("data") / old_file_name
        if new.exists():
            new.unlink()
        old.rename(new)


# move file
# session
session = Path("pagermaid.session")
rename(session)
# config
config = Path("config.yml")
rename(config)
# docker
docker = Path("install.lock")
rename(docker)
# delete file
# log
log = Path("pagermaid.log.txt")
if log.exists():
    log.unlink()
