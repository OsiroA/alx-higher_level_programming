<!DOCTYPE html>
<html>
<head>
    <title>Test Page</title>
    <!-- Include jQuery library -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <header>This is a header</header>

    <script>
        // Use jQuery to select the <header> element and change its text color
        $(document).ready(function() {
            $("header").css("color", "#FF0000");
        });
    </script>
</body>
</html>
