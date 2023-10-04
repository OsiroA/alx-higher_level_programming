<!DOCTYPE html>
<html>
<head>
    <title>List Operations</title>
    <!-- Include jQuery library -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <div id="add_item">Add Item</div>
    <div id="remove_item">Remove Item</div>
    <div id="clear_list">Clear List</div>
    <ul class="my_list">
        <!-- Existing list items -->
        <li>Item 1</li>
        <li>Item 2</li>
    </ul>

    <script>
        // Use jQuery's $(document).ready() to ensure the script runs after the document is fully loaded
        $(document).ready(function() {
            $("#add_item").click(function() {
                // Add a new <li> element with the text "Item" to UL.my_list
                $("ul.my_list").append("<li>Item</li>");
            });

            $("#remove_item").click(function() {
                // Remove the last <li> element from UL.my_list
                $("ul.my_list li:last-child").remove();
            });

            $("#clear_list").click(function() {
                // Clear all elements from UL.my_list
                $("ul.my_list").empty();
            });
        });
    </script>
</body>
</html>
