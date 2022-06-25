import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="kwiziz",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="kwiziz_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from kwiziz.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export kwiziz_KEY=value
export kwiziz_KEY="@int 42"
export kwiziz_KEY="@jinja {{ this.db.uri }}"
export kwiziz_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
kwiziz_ENV=production kwiziz run
```

Read more on https://dynaconf.com
"""
