import datetime as dt

from js import document, console


def show_error(err: str):
    console.log('showing error', err)
    el = Element('pys-error')
    el.element.style.display = 'initial'
    el.write(err)


def fmt_date(event):

    # pyscript.write('result', dir(event))
    try:
        
        fmt = Element("fmt").value
        date_str = Element("date").value

        date = dt.datetime.strptime(date_str, '%Y-%m-%d')
        console.log(f'{date = }')

        res = date.strftime(fmt)
        pyscript.write('result', res)

    except Exception as err:
        show_error(str(err))
        raise

Element('loaded').element.style.display = 'initial'
