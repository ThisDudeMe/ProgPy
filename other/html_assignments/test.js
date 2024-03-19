document.addEventListener
(
    'DOMContentLoaded', function() 
    { 
        var image = document.getElementById("arrowgreen");
        setInterval
        (
            function()
            {
                if (image.style.visibility === "hidden")
                {   
                    image.style.visibility = "visible";
                }
                else
                {
                    image.style.visibility = "hidden";
                }
            }
            
            , 1000

    


        );
    }
);

