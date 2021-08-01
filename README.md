# django-model-mixins

Mixins for Django models.

## Installation

To get the latest stable release from PyPI

```
pip install django-model-mixins
```

Add `django_model_mixins` to your `INSTALLED_APPS`

```python
INSTALLED_APPS = (
    ...,
    'VAR_PACKAGE_NAME',
)
```

## Usage

### Quickstart

Inherit from mixins in your models, e.g.

```python
from django_model_mixins import mixins

class Article(mixins.CreationDateMixin, mixins.RandomIDMixin):
    # A `created_at` and `id` field is automatically generated on migrations.
    pass
```

Edit settings per model (not per instance!), e.g.

```python
import string

from django_model_mixins import mixins

class EmailVerify(mixins.TokenMixin, mixins.RandomIDMixin):
    TOKEN_LENGTH = 255
    # Token is 255 chars long for every `EmailVerify`


class PasswordReset(mixins.TokenMixin, mixins.RandomIDMixin):
    TOKEN_LENGTH = 6
    TOKEN_CHARS = string.digits
    # Token is 6 digits long for every `PasswordReset`.
```

Edit settings globally, e.g:

`settings.py`
```python
# Don't create a token automatically on model creation.
TOKEN_CREATE_ON_CREATION = False
```

Model settings overwrite global settings.

### Available models

#### RandomIDMixin

Adds a unique `id` field with `primary_key=True`. 
The id is cryptographically generated on model creation.

##### Settings

| Settings name          	| Model name  	| Default value                          	| Description                                                                 	|
|------------------------	|-------------	|----------------------------------------	|-----------------------------------------------------------------------------	|
| `RANDOM_ID_MAX_LENGTH` 	|             	| 1023                                   	| `max_length` value for the `id` field. This value can only be globally set. 	|
| `RANDOM_ID_CHARS`      	| `ID_CHARS`  	| `string.ascii_letters + string.digits` 	| Character pool the generator can choose from.                               	|
|                        	| `ID_LENGTH` 	| `RANDOM_ID_MAX_LENGTH`                 	| The length of the id.                                                       	|

##### Examples

```python
from django_model_mixins import mixins

class Article(mixins.RandomIDMixin):
    pass
```

```python
from django_model_mixins import mixins

class Profile(mixins.RandomIDMixin):
    ID_LENGTH = 20
```



#### CreationDateMixin

Adds a `created_at` field which is automatically set to current time (using `timezone.now()`)
on model creation.

##### Examples

```python
from django_model_mixins import mixins

class Article(mixins.CreationDateMixin):
    pass
```



#### EditDateMixin

Adds a `edited_at` field which is automatically set to current time (using `timezone.now()`)
on every model save.

##### Examples

```python
from django_model_mixins import mixins

class Article(mixins.EditDateMixin):
    pass
```



#### TokenMixin

Adds a `token` field which can be used as an alternative to a `id`.
The `token` can be changed anytime, whereas `id` is immutable.

The token is generated cryptographically.

#### Settings

| Settings name              	| Model name           	| Default value                          	| Description                                                                    	|
|----------------------------	|----------------------	|----------------------------------------	|--------------------------------------------------------------------------------	|
| `TOKEN_MAX_LENGTH`         	|                      	| 2047                                   	| `max_length` value for the `token` field. This value can only be globally set. 	|
| `TOKEN_CHARS`              	| `TOKEN_CHARS`        	| `string.ascii_letters + string.digits` 	| Character pool the generator can choose from.                                  	|
|                            	| `TOKEN_LENGTH`       	| `TOKEN_MAX_LENGTH`                     	| The length of the token.                                                       	|
| `TOKEN_CREATE_ON_CREATION` 	| `CREATE_ON_CREATION` 	| `True`                                 	| Whether a token should automatically be created on model creation.             	|

##### Examples

```python
import string

from django_model_mixins import mixins


class PasswordReset(mixins.TokenMixin):
    TOKEN_CHARS = string.digits
    TOKEN_LENGTH = 6
```

##### Methods

##### `token.recreate_token()`

Recreates the token and saves it.



#### TokenGeneratedAtMixin

Inherits from `TokenMixin`.

Adds a `token_generated` field which represents the last date a token was created (or recreated.)

You **need** to specify a `TOKEN_VALID_DURATION_IN_SECONDS` field per model.

#### Settings

| Settings name 	| Model name                        	| Default value 	| Description                                                                                	|
|---------------	|-----------------------------------	|---------------	|--------------------------------------------------------------------------------------------	|
|               	| `TOKEN_VALID_DURATION_IN_SECONDS` 	|               	| The duration in seconds how long a token is valid. `int` expected. This field is required. 	|
              
##### Examples

```python
import string

from django_model_mixins import mixins


class PasswordReset(mixins.TokenGeneratedAtMixin):
    TOKEN_CHARS = string.digits
    TOKEN_LENGTH = 6
    
    # Token is valid for 15 minutes
    TOKEN_VALID_DURATION_IN_SECONDS = 60 * 15

```

##### Methods

##### `token.expire_date`

The date till when the token is valid.

##### `token.is_expired`

Return whether the token is expired.
