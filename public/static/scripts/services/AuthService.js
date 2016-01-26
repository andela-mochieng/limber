app.factory('sessionInjector', function ($cookies) {
    return {
        request: function(config) {
            var token = $cookies.get("token");
            config.headers = config.headers || {};
            if (token) {
                config.headers['Authorization'] = "JWT " + token;
            }

            return config;
        }
    };
});

app.factory('AuthService', function ($resource) {
    return {
        auth: $resource('/api/api-token-auth/', {}, {
            login: {
                method: 'POST'
            },
            logout: {
                method: 'DELETE'
            }
        }, {
            stripTrailingSlashes: false
        }),
        verify: $resource('/api/api-token-verify/', {}, {
            token: {
                method: 'POST'
            }
        }, {
            stripTrailingSlashes: false
        }),
        users: $resource('/api/user/', {}, {
            create: {
                method: 'POST'
            }
        }, {
            stripTrailingSlashes: false
        }),
        projects: $resource('/api/project/', {}, {
            // method to consume the api route to Projects
            // it returns an array of projects
            getProjects: {
                method: 'GET',
                isArray: true
            }
        }, {
            stripTrailingSlashes: false
        })
    };
});
