<!DOCTYPE html>
<html>
<head>
    <title>Change Text Color</title>
    <script>
        // Wait for the DOM to be fully loaded
        document.addEventListener("DOMContentLoaded", function() {
            // Select the <header> element using document.querySelector
            var headerElement = document.querySelector("header");

            // Check if the element exists before changing its style
            if (headerElement) {
                // Change the text color to red (#FF0000)
                headerElement.style.color = "#FF0000";
            }
        });
    </script>
</head>
<body>
    <header>This is a header</header>
</body>
</html>
