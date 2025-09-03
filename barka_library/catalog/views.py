from django.shortcuts import render, HttpResponse

# Create your views here.
def books(request):
    return HttpResponse("""<ul>
    <li>To Kill a Mockingbird</li>
    <li>1984</li>
    <li>The Great Gatsby</li>
    <li>Pride and Prejudice</li>
    <li>The Catcher in the Rye</li>
  </ul>""")

def special(request):
    return HttpResponse("""<div class="featured-books">
  <h3>Featured Books</h3>
  <ol>
    <li>The Alchemist</li>
    <li>Sapiens: A Brief History of Humankind</li>
  </ol>
</div>""")