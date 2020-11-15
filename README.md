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
         
