from ..models import Variable


def get_variables():
    queryset = Variable.objects.all()
    return (queryset)


def create_variable(form):
    measurement = form.save()
    measurement.save()
    return ()


def get_variable_by_name(name):
    try:
        variable = Variable.objects.get(name=name)
        return (variable)
    except:
        variable = None
        return (variable)
    
def get_variable(id):
    variable = Variable.objects.raw("SELECT * FROM variables_variable WHERE id=%s" % id)[0]
    return (variable)
