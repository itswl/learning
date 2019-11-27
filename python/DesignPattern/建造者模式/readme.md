**建造者模式，将复杂对象的构造从其表示形式中分离了出来，因此可用相同的构造过程来创建不同形式的表单**。

**其最大的缺点在于，我们要为希望创建的每一种产品类型创建ConcreteBuilder建造者**


原始代码
```
def generator_webform(text_field_list=[],checkbox_field_list=[]):
    generator_fields = "\n".join(map(lambda x:'{0}：<br> <input type="text" name="{0}"> <br>'.format(x),text_field_list))
    generator_fields += "\n".join(map(lambda x:'<label><input type="checkbox" id="{0}" value={0}>{0} <br>'.format(x),checkbox_field_list))
    return "<form>{fields}</form>".format(fields=generator_fields)


def build_html_form(text_field_list=[],checkbox_field_list=[]):
    with open('form_file.html','w') as f :
        f.write('<html><body>{}</body></html>'.format(generator_webform(text_field_list=text_fields,checkbox_field_list=checkbox_fields)))


if __name__ == "__main__":
    text_fields = ["name","age","email","telephone"]
    checkbox_fields = ['awesome' , 'bad']
    print(generator_webform(text_field_list=text_fields,checkbox_field_list=checkbox_fields))
    build_html_form(text_field_list=text_fields,checkbox_field_list=checkbox_fields)

```
改造后
```
from abc import ABCMeta, abstractmethod

class Director(object, metaclass=ABCMeta):
    def __init__(self):
        self._builder =None

    def set_build(self, builder):
        self._builder = builder

    @abstractmethod
    def construct(self, field_list):
        pass

    def get_constructed_object(self):
        return self._builder.constructed_object


class AbstractFormBuilder(object,metaclass=ABCMeta):
    def __init__(self):
        self.constructed_object = None

    @abstractmethod  # 定义一个抽象基类
    def add_checkbox(self, checkbox_dict):
        pass

    @abstractmethod
    def add_text_field_dict(self,field_dict):
        pass

    @abstractmethod
    def add_button(self, button_dict):
        pass

class HtmlForm(object):
    def __init__(self):
        self.field_list = []

    def __repr__(self):
        return '<form>{}</form>'.format(''.join(self.field_list))

class HtmlFormBuilder(AbstractFormBuilder):
    def __init__(self):
        self.constructed_object =HtmlForm()

    def add_text_field(self, field_dict):
        self.constructed_object.filed_list.append(
            '{0}:<br><input type="text" name="{1}"><br>'.format(field_dict['label'],
                                                                field_dict['field_name']))

    def add_checkbox(self, checkbox_dict):
        self.constructed_object.filed_list.append(
            '<label><input type="checkbox" id="{0}" value = "{1}"> {2}<br>'.format('field_id',
                                                                                   checkbox_dict['value'],
                                                                                   checkbox_dict['label']))

    def add_button(self, button_dict):
        self.constructed_object.filed_list.append(
            '<button type="button"> {} </button>'.format(button_dict['text']))

class FormDirector(Director):
    def __init__(self):
        Director.__init__(self)

    def construct(self, field_list):
        for field in field_list:
            if field["field_type"] ==  'text_field':
                self._builder.add_text_field(field)
            elif field["field_type"] ==  'checkbox':
                self._builder.add_check(field)
            elif field["field_type"] ==  'button':
                self._builder.add_button(field)

if __name__ == '__main__':
    director = FormDirector()
    html_form_builder = HtmlFormBuilder()
    director.set_build(html_form_builder)

    field_list = [
        {
            'field_type' : 'text_field',
            'label' : 'Best text you have ever writen',
            'field_name' : 'Field One'
         },
        {
            'field_type': 'checkbox',
            'field_id' : 'check_it',
            'label': 'check for on',
            'value': '1'
        },
        {
            'field_type': 'text_field',
            'label': 'another text you have ever writen',
            'field_name': 'Field One'
        },
        {
            'field_type' : 'button',
            'text' : 'Done'
        }
    ]
    director.construct(field_list)

    with open('form_file.html', 'w') as f:
        f.write(
            '<html><body>{0!r}</body></html>'.format(
            director.get_constructed_object()
        )
    )


```
