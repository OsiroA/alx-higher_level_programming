<!DOCTYPE html>
<html>
<head>
    <title>Test Page</title>
    <!-- Include jQuery library -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <div id="red_header">Click to Add Class</div>
    <header>This is a header</header>

    <script>
        // Use jQuery to add a click event handler to the #red_header element
        $(document).ready(function() {
            $("#red_header").click(function() {
                // Add the "red" class to the <header> element
                $("header").addClass("red");
            });
        });
    </script>
</body>
</html>
