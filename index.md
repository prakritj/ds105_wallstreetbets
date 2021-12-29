<!-- Custom JavaScript files set in YAML front matter -->
{% for js in page.customjs %}
<script async type="text/javascript" src="{{visualisation.js}}"></script>
{% endfor %}