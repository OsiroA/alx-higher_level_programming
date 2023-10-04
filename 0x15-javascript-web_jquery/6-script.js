<!DOCTYPE html>
<html>
<head>
    <title>Test Page</title>
    <!-- Include jQuery library -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <div id="update_header">Update Header</div>
    <header>This is the old header</header>

    <script>
        // Use jQuery to add a click event handler to the #update_header element
        $(document).ready(function() {
            $("#update_header").click(function() {
                // Update the text of the <header> element to "New Header!!!"
                $("header").text("New Header!!!");
            });
        });
    </script>
</body>
</html>
