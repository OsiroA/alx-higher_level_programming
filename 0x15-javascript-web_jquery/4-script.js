<!DOCTYPE html>
<html>
<head>
    <title>Test Page</title>
    <!-- Include jQuery library -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <style>
        .red {
            color: red;
        }

        .green {
            color: green;
        }
    </style>
</head>
<body>
    <div id="toggle_header">Toggle Class</div>
    <header class="red">This is a header</header>

    <script>
        // Use jQuery to add a click event handler to the #toggle_header element
        $(document).ready(function() {
            $("#toggle_header").click(function() {
                // Toggle the class between "red" and "green" on the <header> element
                $("header").toggleClass("red green");
            });
        });
    </script>
</body>
</html>
