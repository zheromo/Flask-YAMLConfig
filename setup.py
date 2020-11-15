"""
Flask-YAMLConfig
----------------

Usage
-----

::
    from flaskext.yamlconfig import AppYAMLConfig
    AppYAMLConfig(app, "main.yaml")
    
or 
    
::
    from flaskext.yamlconfig import install_yaml_config
    from flaskext.yamlconfig import AppYAMLConfig
    
    class MyConfig(AppYAMLConfig):
        def configure_mysection(self, content):
            for item in content:
                ....
                
    yaml_config = install_yaml_config(app, MyConfig)
    yaml_config("main.yaml")
    
Register a renderers
--------------------

::
    from flask import current_app
    from flaskext.yamlconfig import Renderer, register_renderer
    from werkzeug.wrappers import BaseResponse
    
    class JsonRenderer(Renderer):
        def render(self, view_result):
            return current_app.response_class(json.dumps(view_result,
                indent=None if request.is_xhr else 2), mimetype='application/json')
    
    register_renderer('json', JsonRenderer)
    
    
Config file sample
------------------

::

    index:
        view: views.index.index
        url:
            - /
            - /page/<int:page>
        renderer: actions/index/index.html

    blog_edit:
        view: views.blog.edit_blog
        url: /blog/edit/<blog_url>
        renderer: actions/blog/edit.html
        methods:
            - GET
            - POST
        context:
            w_group: empty

    ajaxBlogJoin:
        view: views.blog.ajax_blog_join
        url: /ajax/blogjoin/<int:blog_id>
        methods:
            - POST
        renderer: json
        
View example
------------

    def index(context, request, page=1):
        '''Main page
        '''
        return dict(pages = Pager(Topic.all(), page))
        

"""

from setuptools import setup
import sys
requires = ['Flask>=0.6', 'PyYAML']
if sys.version_info < (2, 6):
    requires.append('simplejson')

setup(
    name='Flask-YAMLConfig',
    version='0.0.3',
    license='MIT',
    author='Eugene Sazonov aka zheromo',
    author_email='zheromo@gmail.com',
    description='YAML configurator for Flask app.',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=requires,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
