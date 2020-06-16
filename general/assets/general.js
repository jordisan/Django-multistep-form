// global namespace
var general = general || {};

// module for API calls
general.API = (function(){
    'use strict';

    var _api_url = null;

    /**
     * Generic function to get JSON data from API
     * @param {string} path 
     */
    function _getJson(path) {
        return fetch(_api_url + '/' + path)
            .then(function(response) {
                if (response.ok) {
                    return response.json();
                } else {
                    // if not found, just return null
                    return Promise.resolve(null);
                }
            })
            .catch(function(err) {
                console.log(err);
                return Promise.reject();
            })
    }

    /**
     * Get JSON customer data
     * @param {string} email 
     */
    function _getCustomerData(email) {
        return _getJson('customers/' + encodeURIComponent(email));
    };

    /**
     * Initialize
     */
    function _init(api_url) {
        _api_url = api_url;
    };

    return {
        getJson: _getJson,
        getCustomerData: _getCustomerData,
        init: _init
    };
})();
