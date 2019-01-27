# Easy Django MicroService Framework
This is a framework for django in order to create microservice 
application more easily.  
Now, this framework only supports fast operation of database, 
but other functions will be soon.  
这是Django创建微服务的框架，它使微服务的使用更加便利。  
目前，这个框架只支持数据库的快速操作，其他功能很快就会实现。  
  

We recommend that the catalogue of the project be as follows:  
我们建议项目的目录这样来设置：
- database
    - database_name
        - model (A Django App Folder only include database design)
            - apps.py (Register your Django App, You can also write it in the file model.py)
            - models.py (Design your model, then use Django ORM migrate it)
        - manage.py
        - service.py (Everything has been done except service name and dependency, add it and start the microservice for database)
        - settings.py
    - other database service
- logic

## Database / 数据库访问层
We recommend that you write `settings.py` this way.  
我们建议你这样来写`settings.py`文件：

```python
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WSGI_APPLICATION = 'easy.database.wsgi.application'
DATABASES = {
}
from easy.database.settings import *
INSTALLED_APPS += [
    'models',
]
```
We recommend that you design your database in `models.py` in this way.
我们建议你在`models.py`中这样写:

```python
from easy.database import models
class Manager(models.Manager):
    # Model Manage
class Model(models.AdminModel):
    # Design Model
```
We recommend that you define services in file `service.py` in this way.
我们建议你在`service.py`文件中这样定义服务：
```python
import easy.database.urls
from models import models as dependences
from easy.database.service.rpc import RPCServiceModel
class ArticleService(RPCServiceModel):
    name = "article"
    __dependence__ = dependences.Article
```
In the file`service.py`, you must keep the first line, 
because the service of this project is implemented by RPC 
in nameko framework. If you remove the first line of code, 
you need to start the service by non-command line, 
which is a very difficult thing.  

在`service.py`文件中请你务必保留第一行，因为本项目的服务采用的
是nameko框架中的RPC方式实现的，如果去掉第一行的代码，你需要通
过非命令行的方式启动服务，这是一件很困难的事情。  

With the first line, you can use the service directly without 
starting the Django server.
有了第一行代码后，你就可以在不启动Django服务器的情况下直接启动微服务。  

Run this command on the console to start the service.  
在命令行直接运行这个命令就可以启动服务。
```
nameko run service
```
You can also add the following code to the end of the serivice.py 
so that it can be executed directly.  
你也可以将下面的代码添加到serivice.py文件最后，这样直接执行该文件即可。
```python
if __name__ == '__main__':
    import os
    os.system("nameko run service")
```

