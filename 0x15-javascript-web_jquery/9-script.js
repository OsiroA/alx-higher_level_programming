<!DOCTYPE html>
<html>
<head>
    <title>Hello Translation</title>
    <!-- Include jQuery library -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <div id="hello">Translation Will Appear Here</div>

    <script>
        // Use jQuery's $(document).ready() to ensure the script runs after the document is fully loaded
        $(document).ready(function() {
            // Use jQuery's $.get() to fetch the translation from the URL
            $.get("https://fourtonfish.com/hellosalut/?lang=fr", function(data) {
                // Extract the "hello" translation from the JSON response
                var helloTranslation = data.hello;

                // Update the content of the <div> with the translation
                $("#hello").text(helloTranslation);
            })
            .fail(function() {
                // Handle any errors if the request fails
                $("#hello").text("Error: Unable to fetch translation");
            });
        });
    </script>
</body>
</html>
