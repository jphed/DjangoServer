from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")

def add(request):
    """
    Simple addition calculator of two numbers using query params ?a= and ?b=
    If params are missing, shows a small HTML form to input numbers.
    """
    a = request.GET.get("a")
    b = request.GET.get("b")

    html_head = """
    <html>
      <head><title>Addition Calculator</title></head>
      <body>
        <h1>Addition Calculator</h1>
        <form method="get">
          <label>Number A: <input type="number" name="a" step="any" required></label><br><br>
          <label>Number B: <input type="number" name="b" step="any" required></label><br><br>
          <button type="submit">Add</button>
        </form>
    """

    if a is None or b is None:
        return HttpResponse(html_head + "</body></html>")

    try:
        a_val = float(a)
        b_val = float(b)
        result = a_val + b_val
        result_html = f"""
        <hr>
        <p><strong>Result:</strong> {a_val} + {b_val} = <strong>{result}</strong></p>
        """
        return HttpResponse(html_head + result_html + "</body></html>")
    except ValueError:
        error_html = """
        <hr>
        <p style='color:red;'>Please enter valid numbers.</p>
        """
        return HttpResponse(html_head + error_html + "</body></html>")


def randomize(request):
    """
    Page with one button that randomizes a number between 1 and 999
    each time you click the button. Uses GET to avoid CSRF.
    """
    number = random.randint(1, 999)
    html = f"""
    <html>
      <head><title>Random Number</title></head>
      <body>
        <h1>Random Number</h1>
        <p style="font-size:24px;">Current number: <strong>{number}</strong></p>
        <form method="get">
          <button type="submit">Randomize</button>
        </form>
      </body>
    </html>
    """
    return HttpResponse(html)


def saludo(request, nombre="Mundo"):
    """
    Renderiza la plantilla de saludo pasando un nombre capitalizado.
    Se usa junto con la ruta: /MiPrimeraPagina/saludo/<str:nombre>/
    """
    return render(request, "MiPrimeraPagina/saludo.html", {"nombre": nombre.capitalize()})
