<!DOCTYPE html>
<html>
<head>
    <title>Movie List</title>
    <!-- Include jQuery library -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <ul id="list_movies"></ul>

    <script>
        // Use jQuery to make an AJAX request to the URL
        $(document).ready(function() {
            $.ajax({
                url: "https://swapi-api.alx-tools.com/api/films/?format=json",
                method: "GET",
                dataType: "json",
                success: function(data) {
                    // Loop through the movie data and append titles to the <ul>
                    var movieList = $("#list_movies");
                    $.each(data.results, function(index, movie) {
                        movieList.append("<li>" + movie.title + "</li>");
                    });
                },
                error: function() {
                    // Handle any errors if the request fails
                    $("#list_movies").append("<li>Error: Unable to fetch movie list</li>");
                }
            });
        });
    </script>
</body>
</html>
