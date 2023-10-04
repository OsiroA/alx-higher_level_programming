<!DOCTYPE html>
<html>
<head>
    <title>Hello Translation</title>
    <!-- Include jQuery library -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <input type="text" id="language_code" placeholder="Enter language code (e.g., es, fr, en)">
    <input type="button" id="btn_translate" value="Translate">
    <div id="hello">Translation Will Appear Here</div>

    <script>
        // Use jQuery's $(document).ready() to ensure the script runs after the document is fully loaded
        $(document).ready(function() {
            $("#btn_translate").click(function() {
                // Get the language code entered by the user
                var languageCode = $("#language_code").val();

                // Make an AJAX request to fetch the translation
                $.ajax({
                    url: "https://www.fourtonfish.com/hellosalut/hello/",
                    method: "GET",
                    data: { lang: languageCode },
                    dataType: "json",
                    success: function(data) {
                        // Extract the translation of "Hello" from the JSON response
                        var helloTranslation = data.hello;

                        // Update the content of the <div> with the translation
                        $("#hello").text(helloTranslation);
                    },
                    error: function() {
                        // Handle any errors if the request fails
                        $("#hello").text("Error: Unable to fetch translation");
                    }
                });
            });
        });
    </script>
</body>
</html>
