{"filter":false,"title":"urls.py","tooltip":"/products/urls.py","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":0,"column":0},"end":{"row":26,"column":14},"action":"insert","lines":["{% extends 'base.html' %}","","{% block content %}","<div class=\"row row-flex\">","    {% for product in products %}","        <div class=\"col-xs-10 col-xs-offset-1 col-sm-offset-0 col-sm-6 col-md-4 display panel panel-default\">","            <div class=\"panel-body\">","                <div class=\"product\" style=\"background-image: url('{{ MEDIA_URL }}{{ product.image }}')\"></div>","","                <h3>{{ product.name }}</h3>","                <p class=\"product-description\">{{ product.description }}</p>","                <p>{{ product.price }}</p>","","                <form method=\"post\" action=\"{% url 'add_to_cart' product.id %}\">","                    {% csrf_token %}","                    <div class=\"input-group\">","                        <input name=\"quantity\" type=\"number\" min=\"1\" max=\"999\" class=\"form-control\" placeholder=\"Quantity\">","                        <span class=\"input-group-btn\">","                            <button class=\"btn btn-success\" type=\"submit\">Add</button>","                        </span>","                    </div>","                </form>","            </div>","        </div>","    {% endfor %}","</div>","{% endblock %}"],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":26,"column":14},"action":"remove","lines":["{% extends 'base.html' %}","","{% block content %}","<div class=\"row row-flex\">","    {% for product in products %}","        <div class=\"col-xs-10 col-xs-offset-1 col-sm-offset-0 col-sm-6 col-md-4 display panel panel-default\">","            <div class=\"panel-body\">","                <div class=\"product\" style=\"background-image: url('{{ MEDIA_URL }}{{ product.image }}')\"></div>","","                <h3>{{ product.name }}</h3>","                <p class=\"product-description\">{{ product.description }}</p>","                <p>{{ product.price }}</p>","","                <form method=\"post\" action=\"{% url 'add_to_cart' product.id %}\">","                    {% csrf_token %}","                    <div class=\"input-group\">","                        <input name=\"quantity\" type=\"number\" min=\"1\" max=\"999\" class=\"form-control\" placeholder=\"Quantity\">","                        <span class=\"input-group-btn\">","                            <button class=\"btn btn-success\" type=\"submit\">Add</button>","                        </span>","                    </div>","                </form>","            </div>","        </div>","    {% endfor %}","</div>","{% endblock %}"],"id":2},{"start":{"row":0,"column":0},"end":{"row":5,"column":1},"action":"insert","lines":["from django.conf.urls import url, include","from .views import all_products","","urlpatterns = [","    url(r'^$', all_products, name='products'),","]"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":5,"column":1},"end":{"row":5,"column":1},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":131,"mode":"ace/mode/python"}},"timestamp":1561276386782,"hash":"b604cecf7240f1919bff499f7d2e250c28ef329d"}