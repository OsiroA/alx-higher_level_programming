<!DOCTYPE html>
<html>
<head>
    <title>Test Page</title>
    <!-- Include jQuery library -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <div id="add_item">Add Item</div>
    <ul class="my_list">
        <!-- Existing list items -->
        <li>Item 1</li>
        <li>Item 2</li>
    </ul>

    <script>
        // Use jQuery to add a click event handler to the #add_item element
        $(document).ready(function() {
            $("#add_item").click(function() {
                // Create a new <li> element with the text "Item"
                var newItem = $("<li>Item</li>");
                
                // Append the new <li> element to UL.my_list
                $("ul.my_list").append(newItem);
            });
        });
    </script>
</body>
</html>
