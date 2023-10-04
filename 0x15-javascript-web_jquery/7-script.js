<!DOCTYPE html>
<html>
<head>
    <title>Test Page</title>
    <!-- Include jQuery library -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <div id="character">Character Name Will Appear Here</div>

    <script>
        // Use jQuery to make an AJAX request to the URL
        $(document).ready(function() {
            $.ajax({
                url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
                method: "GET",
                dataType: "json",
                success: function(data) {
                    // Extract the character name from the JSON response
                    var characterName = data.name;

                    // Update the content of the <div> with the character name
                    $("#character").text(characterName);
                },
                error: function() {
                    // Handle any errors if the request fails
                    $("#character").text("Error: Unable to fetch character name");
                }
            });
        });
    </script>
</body>
</html>
