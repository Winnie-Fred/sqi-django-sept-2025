from django.shortcuts import render, HttpResponse

# Create your views here.
def community_events(request):
    return HttpResponse("""<section class="community-events">
  <h2>Upcoming Community Events</h2>
  <ul>
    <li>
      <strong>Tech Meetup</strong> - September 10, 2025
    </li>
    <li>
      <strong>Local Farmers' Market</strong> - September 15, 2025
    </li>
    <li>
      <strong>Charity Fun Run</strong> - September 22, 2025
    </li>
    <li>
      <strong>Book Club Gathering</strong> - September 28, 2025
    </li>
  </ul>
</section>""")