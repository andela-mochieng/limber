app.controller('LandingController', function($scope){
    $(".animation").typed({
        strings: ["agile software development", "taking your girlfriend to shop", "better project management."],
        typeSpeed: 70,
        backDelay: 70,
        cursorChar: " | "
     });
     $('.slider').slider({height: 120, indicators: false, interval : 2000});

     
});


app.controller('DashCtrl', function($scope, $cookies, AuthService){
    //
});
